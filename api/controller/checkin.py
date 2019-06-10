from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.checkin
@app.route("/api/checkin", methods=["GET", "POST"])
@app.route("/api/checkin/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def checkin(id=None):
    return api.model.checkin.Checkin.HandleRequest(request, id=id)
