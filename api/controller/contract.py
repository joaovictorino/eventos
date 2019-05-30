from flask import request, jsonify
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.contract
@app.route("/api/contract", methods=["GET", "POST"])
@app.route("/api/contract/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def contract(id=None):
    return api.model.contract.Contract.HandleRequest(request, id=id)
