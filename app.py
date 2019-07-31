from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity


app = Flask(__name__)
# Turn off the Flask-SQLAlchemy tracker because SQLAlchemy tracker is better
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'a_secret_key_to_keep_secret...'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # create /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == "__main__":
    from db import db  # to avoid circular import

    db.init_app(app)
    app.run(debug=True)
