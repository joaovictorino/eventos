from flask import request, jsonify
from lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

@app.route("/testOk")
@ErrorHandlerAndJsonifier
def testOk():
    return "API Data"

@app.route("/testEmpty")
@ErrorHandlerAndJsonifier
def testEmpty():
    return None
    
@app.route("/testFail")
@ErrorHandlerAndJsonifier
def testeFail():
    raise Exception("Exception Message")

import model.plan
@app.route("/plan", methods=["GET", "POST"])
@app.route("/plan/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def plan(id=None):
    return model.plan.Plan.HandleRequest(request, id=id)

import model.contract
@app.route("/contract", methods=["GET", "POST"])
@app.route("/contract/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def contract(id=None):
    return model.contract.Contract.HandleRequest(request, id=id)

import model.domain
@app.route("/domain", methods=["GET", "POST"])
@app.route("/domain/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def domain(id=None):
    return model.domain.Domain.HandleRequest(request, id=id)

import model.eventGroup
@app.route("/eventGroup", methods=["GET", "POST"])
@app.route("/eventGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def eventGroup(id=None):
    return model.eventGroup.EventGroup.HandleRequest(request, id=id)

import model.event
@app.route("/event", methods=["GET", "POST"])
@app.route("/event/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def event(id=None):
    return model.event.Event.HandleRequest(request, id=id)
    
import model.user
@app.route("/user", methods=["GET", "POST"])
@app.route("/user/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def user(id=None):
    return model.user.User.HandleRequest(request, id=id)

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
