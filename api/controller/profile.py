from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.profile
@app.route("/api/profile", methods=["GET", "POST"])
@app.route("/api/profile/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def profile(id=None):
	abstraction = api.model.profile.Profile
	ValidateRequestPermissions(abstraction, request, id, UserPermission, SysAdminPermission, SysAdminPermission)
	return abstraction.HandleRequest(request, id=id)
