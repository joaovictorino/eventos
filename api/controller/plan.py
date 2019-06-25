from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.plan
@app.route("/api/plan", methods=["GET", "POST"])
@app.route("/api/plan/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def plan(id=None):
	abstraction = api.model.plan.Plan
	ValidateRequestPermissions(abstraction, request, id, None, SysAdminPermission, SysAdminPermission)
	return abstraction.HandleRequest(request, id=id)
