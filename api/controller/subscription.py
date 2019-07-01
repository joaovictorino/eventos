from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.subscription
@app.route("/api/subscription", methods=["GET", "POST"])
@app.route("/api/subscription/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def subscription(id=None):
	abstraction = api.model.subscription.Subscription
	ValidateRequestPermissions(abstraction, request, id, UserPermission, SysAdminPermission, SysAdminPermission)
	return abstraction.HandleRequest(request, id=id)
