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
            log.error("Error returning serializing repsonse")
            objResponse = "Was not possible to serialize response"
        return objResponse
    return wrapper
    
from flask_jwt import jwt_required
def EnsureCredentials(func):
    @jwt_required()
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrapper
