from functools import wraps
from flask import jsonify

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
                response["data"] = str(ex)
            except:
                response["data"] = "Was not able to stringfigy exception"
            response["status"] = "fail"
            
        try:
            objResponse = jsonify(response)
        except Exception as ex:
            print(ret)
            objResponse = "Was not possible to serialize response"
        return objResponse
    return wrapper
