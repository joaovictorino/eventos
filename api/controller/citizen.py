from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.citizen
@app.route("/api/citizen", methods=["GET", "POST"])
@app.route("/api/citizen/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def citizen(id=None):
    return api.model.citizen.Citizen.HandleRequest(request, id=id)
