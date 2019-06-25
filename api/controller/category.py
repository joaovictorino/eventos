from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.category
@app.route("/api/category", methods=["GET", "POST"])
@app.route("/api/category/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def category(id=None):
	abstraction = api.model.category.Category
	ValidateRequestPermissions(abstraction, request, id, None, GroupPermission, GroupPermission)
	return abstraction.HandleRequest(request, id=id)
