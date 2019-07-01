from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.event
@app.route("/api/event", methods=["GET", "POST"])
@app.route("/api/event/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def event(id=None):
	abstraction = api.model.event.Event
	ValidateRequestPermissions(abstraction, request, id, None, GroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
