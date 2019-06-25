from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.categoryGroup
@app.route("/api/categoryGroup", methods=["GET", "POST"])
@app.route("/api/categoryGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def categoryGroup(id=None):
	abstraction = api.model.categoryGroup.CategoryGroup
	ValidateRequestPermissions(abstraction, request, id, None, GroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
