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
import api.lib.cacAuth
import api.lib.ldapAuth
@common.app.route("/api/auth", methods=["POST"])
@ErrorHandlerAndJsonifier
def JWTAuthHandler():
    userObj = None
    data = request.get_json()
    username = data.get(common.app.config.get('JWT_AUTH_USERNAME_KEY'), None).lower()
    password = data.get(common.app.config.get('JWT_AUTH_PASSWORD_KEY'), None)
    actor = data.get(common.app.config.get('JWT_AUTH_ACTOR_KEY'), None)
    criterion = [username, password, actor]

    if not all(criterion):
        raise Exception("Bad request: invalid credentials")

    identity = None
    if actor == "user":
        if username == "root":
            identity = api.model.user.User.authenticate(username, password)
        else:
            userInstances = api.model.user.User.objects(login = username).all()
            if len(userInstances):
                userInstance = userInstances[0]
                if userInstance.state != "ACTIVE":
                    raise Exception("Bad request: invalid credentials")
                
                if userInstance.auth_method == "CAC":
                    cacLoginId = api.lib.cacAuth.LoginUser(username, password)
                    if "status" in cacLoginId and cacLoginId["status"] == "OK":
                        identity = userInstance.getUserAbstraction()
                        
                elif userInstance.auth_method == "LDAP":
                    userInfo = api.lib.ldapAuth.LoginUser(username, password)
                    print(userInfo)
                    if userInfo is not None:
                        userInstance.name=userInfo["name"].decode("utf-8", errors="ignore")
                        userInstance.email=userInfo["email"].decode("utf-8", errors="ignore")
                        userInstance.password=password
                        userInstance.save()
                        identity = userInstance.getUserAbstraction()
                 
            else:
                cacLoginId = api.lib.cacAuth.LoginUser(username, password)
                if "status" in cacLoginId and cacLoginId["status"] == "OK":
                    userInstance = api.model.user.User.objects(login = username).first()
                    if not userInstance:
                        common.log.info("Creating instance for user: " + username)
                        userInstance = api.model.user.User()
                        userInstance.name = cacLoginId["usuario"]["nm_usuario"]
                        userInstance.login = username
                        userInstance.auth_method = "CAC"
                        userInstance.password = password
                        userInstance.email = "user@cac"
                        userInstance.save()
                    identity = userInstance.getUserAbstraction()
    
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
    
    
