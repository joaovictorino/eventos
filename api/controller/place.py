from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.place
@app.route("/api/place", methods=["GET", "POST"])
@app.route("/api/place/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def place(id=None):
    return api.model.place.Place.HandleRequest(request, id=id)
