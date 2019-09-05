from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HandleBuyer(Resource):
    def post(self):

        json_data = request.get_json(force=True)
        print(json_data)
        pass

    def create_buyer_id(self):


class HandleSeller(Resource):
    def post(self):
        pass


class HandleSellerLocation(Resource):
    def post(self):
        pass


class HandleTransaction(Resource):
    def post(self):
        pass

api.add_resource(HandleBuyer, '/buyer')

api.add_resource(HandleSeller, '/seller')

api.add_resource(HandleSellerLocation, '/seller/location')

api.add_resource(HandleTransaction, '/transaction')

if __name__ == '__main__':
    app.run(debug=True)