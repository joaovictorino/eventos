from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

import api.model.comment
@app.route("/api/comment", methods=["GET", "POST"])
@app.route("/api/comment/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def comment(id=None):
	abstraction = api.model.comment.Comment
	ValidateRequestPermissions(abstraction, request, id, None, OwnerPermission, OwnerPermission)
	return abstraction.HandleRequest(request, id=id)
