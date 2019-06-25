from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.userGroup
@app.route("/api/userGroup", methods=["GET", "POST"])
@app.route("/api/userGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def userGroup(id=None):
	abstraction = api.model.userGroup.UserGroup
	ValidateRequestPermissions(abstraction, request, id, SubscriptionAdminPermission, SubscriptionAdminPermission, SubscriptionAdminPermission)
	return abstraction.HandleRequest(request, id=id)
