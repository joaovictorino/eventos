from flask import request, jsonify
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.permission
@app.route("/api/permission", methods=["GET", "POST"])
@app.route("/api/permission/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def permission(id=None):
    return api.model.permission.Permission.HandleRequest(request, id=id)
