from functools import wraps
from flask import jsonify
from common import log

def ErrorHandlerAndJsonifier(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = {}
        try:
            ret = func(*args, **kwargs)
            if ret is not None:
                response["data"] = ret
            response["status"] = "ok"
        except Exception as ex:
            try:
                log.error("Error: " + str(ex))
                response["data"] = str(ex)
            except:
                log.error("Error returning information")
                response["data"] = "Was not able to stringfigy exception"
            response["status"] = "fail"
            
        try:
            objResponse = jsonify(response)
        except Exception as ex:
            print(ret)
            log.error("Error returning serializing repsonse")
            objResponse = "Was not possible to serialize response"
        return objResponse
    return wrapper
    
from flask_jwt import jwt_required, current_identity
def EnsurePermissions(*requiredPermissions):
    def decoWrapper(func):
        @jwt_required()
        @wraps(func)
        def wrapper(*args, **kwargs):            
            ret = None
            
            if hasattr(current_identity, "permissions"):
                userPermissions = [permission.name for permission in current_identity.permissions]
                print(userPermissions)
                hasNecessaryPermission = False
                for perm in requiredPermissions:
                    if perm in userPermissions:
                        hasNecessaryPermission = True
                        break
                
                if hasNecessaryPermission:
                    ret = func(*args, **kwargs)
                else:
                    if current_identity and hasattr(current_identity, "name"):
                        log.info("User " + str(current_identity.id) + " attempted to access " + func.__name__)
                    raise Exception("User does not have the necessary permission")
            else:
                if current_identity and hasattr(current_identity, "name"):
                    log.info("Unpermissioned user " + str(current_identity.id) + " attempted to access " + func.__name__)
                raise Exception("User has no permissions")
            return ret
        return wrapper
    return decoWrapper
