from flask import request, jsonify
from api.lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

@app.route("/api/testOk")
@ErrorHandlerAndJsonifier
def testOk():
    return "API Data"

@app.route("/api/testEmpty")
@ErrorHandlerAndJsonifier
def testEmpty():
    return None
    
@app.route("/api/testFail")
@ErrorHandlerAndJsonifier
def testFail():
    raise Exception("Exception Message")

@jwt.jwt_error_handler
@ErrorHandlerAndJsonifier
def jwtError(e):
    raise e
    
@jwt.auth_response_handler
@ErrorHandlerAndJsonifier
def authenticationHandler(token, user):
    return {"token": token.decode(), 
            "user": user.toDict()}
    
@app.route("/<path:path>")
@ErrorHandlerAndJsonifier
def default(path):
    return None
