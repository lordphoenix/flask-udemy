from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3
from models.store import StoreModel

class Store(Resource):

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    @jwt_required()
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message" : "An store with name {} already exisits".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message" : "An error occured while inserting the store"}, 500
        return store.json(),201
    
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:    
            item.delete_from_db()
        return {'message' : 'Item has been deleted'}

class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}