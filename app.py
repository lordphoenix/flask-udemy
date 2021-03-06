import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList
from resources.home import HomePage

def create_app():
    app1 = Flask(__name__)
    app1.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
    app1.config['TESTING'] = True
    app1.secret_key = os.environ.get('SECRET_KEY')
    return app1

app = create_app()
api = Api(app)

jwt = JWT(app,authenticate,identity) #new endpoint - /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(HomePage,'/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)