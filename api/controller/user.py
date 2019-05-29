from flask import request, jsonify
from api.lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.user
@app.route("/api/user", methods=["GET", "POST"])
@app.route("/api/user/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def user(id=None):
    return api.model.user.User.HandleRequest(request, id=id)