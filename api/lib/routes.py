from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier, EnsurePermissions

import common
app = common.app
jwt = common.jwt

@app.route("/api/testOk")
@ErrorHandlerAndJsonifier
def testOk():
    if app.debug:
        return "API Data"

@app.route("/api/testEmpty")
@ErrorHandlerAndJsonifier
def testEmpty():
    if app.debug:
        return None
    
@app.route("/api/testFail")
@ErrorHandlerAndJsonifier
def testFail():
    if app.debug:
        raise Exception("Exception Message")
        
@app.route("/api/testPermissionsOk")
@ErrorHandlerAndJsonifier
@EnsurePermissions("p1")
def testPermissionsOk():
    return "Access Granted"
    
@app.route("/api/testPermissionsFail")
@ErrorHandlerAndJsonifier
@EnsurePermissions("undefined permission")
def testPermissionsFail():
    return "Access Denied"

import api.lib.upload
@app.route("/api/testUpload", methods=["POST"])
@ErrorHandlerAndJsonifier
def upload():
    if app.debug:
        return api.lib.upload.Upload(request)
        
@jwt.jwt_error_handler
@ErrorHandlerAndJsonifier
def jwtError(e):
    raise e
    
@jwt.auth_response_handler
@ErrorHandlerAndJsonifier
def authenticationHandler(token, user):
    return {"token": token.decode(), 
            "user": user.toDict()}

@app.route("/")
@app.route("/<path:path>")
def default(path = None):
    ret = None
    if app.debug:
        ret = "<pre>Available routes:\n"
        routes = [el for el in app.url_map.iter_rules()]
        for route in routes:
            methods = filter(lambda m: m != "HEAD" and m != "OPTIONS", route.methods)
            rule = route.rule.replace("<", "&lt;").replace(">", "&gt;")
            ret += "\t" + rule + "(" + ",".join(methods) + ")\n"  
        ret += "</pre>"
    return ret
    
