import common
from flask import request, jsonify
import flask_jwt

def SetupJwt():
    common.jwt.jwt_payload_handler(JWTExtendedInfoMaker)
    
def JWTExtendedInfoMaker(identity):
    tokenInfo = flask_jwt._default_jwt_payload_handler(identity)
    if "permissions" in identity.__dict__:
        tokenInfo["permissions"] = identity.permissions
    tokenInfo["actor"] = identity.actor
    return tokenInfo

import api.model.user
from api.lib.routeDecorators import *
@common.app.route("/api/auth", methods=["POST"])
@ErrorHandlerAndJsonifier
def JWTAuthHandler():
    userObj = None
    data = request.get_json()
    username = data.get(common.app.config.get('JWT_AUTH_USERNAME_KEY'), None)
    password = data.get(common.app.config.get('JWT_AUTH_PASSWORD_KEY'), None)
    actor = data.get(common.app.config.get('JWT_AUTH_ACTOR_KEY'), None)
    criterion = [username, password, actor]

    if not all(criterion):
        raise Exception("Bad request: invalid credentials")

    identity = None
    if actor == "user":
        identity = api.model.user.User.authenticate(username, password)
    elif actor == "citizen":
        identity = api.model.citizen.Citizen.authenticate(username, password)
    else:
        raise Exception("Bad Request: Invalid actor")
    
    if identity:
        access_token = common.jwt.jwt_encode_callback(identity)
        id = identity.toDict()
        id["token"] = access_token.decode('utf-8')
        userObj = id
    else:
        raise Exception("Bad request: invalid credentials")
    
    return userObj
        
def Identity(payload):
    if common.app.debug:
        print(payload)
    return payload
    
    
