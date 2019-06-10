from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.userGroup
@app.route("/api/userGroup", methods=["GET", "POST"])
@app.route("/api/userGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def userGroup(id=None):
    return api.model.userGroup.UserGroup.HandleRequest(request, id=id)
