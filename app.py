from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from db import get_max_buyer_id, get_max_seller_id, get_max_location_id, create_buyer, create_seller, create_seller_location

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
        pass


class HandleItems(Resource):
    def post(self):
        pass

    def get(self):
        pass

api.add_resource(HandleBuyer, '/buyer')

api.add_resource(HandleSeller, '/seller')

api.add_resource(HandleSellerLocation, '/seller/location')

api.add_resource(HandleTransaction, '/transaction')

if __name__ == '__main__':
    app.run(debug=True)