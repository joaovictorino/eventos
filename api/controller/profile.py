from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.profile
@app.route("/api/profile", methods=["GET", "POST"])
@app.route("/api/profile/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def profile(id=None):
    return api.model.profile.Profile.HandleRequest(request, id=id)
