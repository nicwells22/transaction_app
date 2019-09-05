from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from db import get_max_buyer_id, get_max_seller_id, get_max_location_id, get_max_transaction_id, get_max_item_id
from db import create_buyer, create_seller, create_seller_location, create_item, create_transcation

app = Flask(__name__)
api = Api(app)


class HandleBuyer(Resource):
    def post(self):
        id = self.create_buyer_id()
        create_buyer(id)
        return {'buyer_id': id}

    def create_buyer_id(self):
        return get_max_buyer_id() + 1

class HandleSeller(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        seller_name = json_data['name']
        seller_id = self.create_seller_id()
        create_seller(seller_id, seller_name)
        return {'id': seller_id, 'name': seller_name}

    def create_seller_id(self):
        return get_max_seller_id() + 1


class HandleSellerLocation(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        seller_id = json_data['seller_id']
        lat = json_data.get('lat')
        long = json_data.get('long')
        location_id = self.create_location_id()
        create_seller_location(location_id, seller_id, lat, long)
        return {'location_id': location_id, 'seller_id': seller_id, 'lat': lat, 'long': long}

    def create_location_id(self):
        return get_max_location_id() + 1


class HandleTransaction(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        transaction_id = self.create_transaction_id()
        location_id = json_data['location_id']
        buyer_id = json_data['buyer_id']
        sub_total = json_data['sub_total']
        tax = json_data['tax']
        total = json_data['total']
        lat = json_data.get('lat')
        long = json_data.get('long')
        create_transcation(transaction_id, location_id, buyer_id, sub_total, tax, total, lat, long)

        # create items associated with transaction
        items = json_data['items']
        return_items = []
        for item in items:
            item_id = self.create_item_id()
            name = item['name']
            common_name = item['common_name']
            cost = item['cost']
            create_item(item_id, transaction_id, name, common_name, cost)
            return_items.append({'item_id': item_id, 'name': name, 'common_name': common_name, 'cost': cost})

        return {'transaction_id': transaction_id, 'location_id': location_id, 'buyer_id': buyer_id,
                'items': return_items, 'sub_total': sub_total, 'tax': tax, 'total': total, 'lat': lat, 'long': long}


    def create_transaction_id(self):
        return get_max_transaction_id() + 1


    def create_item_id(self):
        return get_max_item_id() + 1


class HandleItems(Resource):
    def post(self):
        json_data = request.get_json(force=True)

    def get(self):
        pass

api.add_resource(HandleBuyer, '/buyer')

api.add_resource(HandleSeller, '/seller')

api.add_resource(HandleSellerLocation, '/seller/location')

api.add_resource(HandleTransaction, '/transaction')

if __name__ == '__main__':
    app.run(debug=True)