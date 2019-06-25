from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.log
@app.route("/api/log", methods=["GET", "POST"])
@app.route("/api/log/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def log(id=None):
	abstraction = api.model.log.Log
	ValidateRequestPermissions(abstraction, request, id, GroupPermission, DeniedPermission, DeniedPermission)
	return abstraction.HandleRequest(request, id=id)
