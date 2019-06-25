from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.hotsite
@app.route("/api/hotsite", methods=["GET", "POST"])
@app.route("/api/hotsite/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def hotsite(id=None):
	abstraction = api.model.hotsite.Hotsite
	ValidateRequestPermissions(abstraction, request, id, GroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
