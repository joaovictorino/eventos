from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.file
@app.route("/api/file", methods=["GET", "POST"])
@app.route("/api/file/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def file(id=None):
	abstraction = api.model.file.File
	ValidateRequestPermissions(abstraction, request, id, None, GroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
