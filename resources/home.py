from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class HomePage(Resources):
    def get(self, name):
        return {'message': 'Please use Postman to test the endpoints'}, 200