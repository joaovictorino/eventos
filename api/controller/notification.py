from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.notification
@app.route("/api/notification", methods=["GET", "POST"])
@app.route("/api/notification/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def notification(id=None):
	abstraction = api.model.notification.Notification
	ValidateRequestPermissions(abstraction, request, id, GroupPermission, GroupPermission, SysAdminPermission)
	return abstraction.HandleRequest(request, id=id)
