from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.plan
@app.route("/api/plan", methods=["GET", "POST"])
@app.route("/api/plan/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def plan(id=None):
    return api.model.plan.Plan.HandleRequest(request, id=id)
