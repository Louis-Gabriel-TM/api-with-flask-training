from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from blacklist import BLACKLIST
from db import db
from resources.user import TokenRefresh, User, UserLogin, UserLogout, UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True  # To see Flask JWT errors
app.config['JWT_BLASKLIST_ENABLED'] = True  # enable blacklist feature
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # allow blacklisting for access and refresh tokens
app.config['JWT_SECRET_KEY'] = 'A First Secret Key for JWT Tokens'
app.secret_key = 'Another Secret Key'

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)  # don't create '/auth' endpoint


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:  # better should read from a config file or a db
        return {'is_admin': True}

    return {'is_admin': False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': "The token has expired.",
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'message': "signature verification failed.",
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': "Request does not contain an access token.",
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': "The token is not fresh.",
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': "The token has been revoked.",
        'error': 'token_revoked'
    }), 401


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserRegister, '/register')
api.add_resource(TokenRefresh, '/refresh')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
