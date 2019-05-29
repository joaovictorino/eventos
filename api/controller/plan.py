from flask import request, jsonify
from api.lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.plan
@app.route("/api/plan", methods=["GET", "POST"])
@app.route("/api/plan/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def plan(id=None):
    return api.model.plan.Plan.HandleRequest(request, id=id)