from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.place
@app.route("/api/place", methods=["GET", "POST"])
@app.route("/api/place/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def place(id=None):
	abstraction = api.model.place.Place
	ValidateRequestPermissions(abstraction, request, id, None, GroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
