from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.eventGroup
@app.route("/api/eventGroup", methods=["GET", "POST"])
@app.route("/api/eventGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def eventGroup(id=None):
	abstraction = api.model.eventGroup.EventGroup
	ValidateRequestPermissions(abstraction, request, id, GroupAdminCreateGroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
