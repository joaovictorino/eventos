from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.profile
@app.route("/api/profile", methods=["GET", "POST"])
@app.route("/api/profile/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def profile(id=None):
    return api.model.profile.Profile.HandleRequest(request, id=id)
