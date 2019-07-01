from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.checkin
@app.route("/api/checkin", methods=["GET", "POST"])
@app.route("/api/checkin/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def checkin(id=None):
	abstraction = api.model.checkin.Checkin
	ValidateRequestPermissions(abstraction, request, id, OwnerPermission, OwnerPermission, SysAdminPermission)
	return abstraction.HandleRequest(request, id=id)
