from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.hotsite
@app.route("/api/hotsite", methods=["GET", "POST"])
@app.route("/api/hotsite/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def hotsite(id=None):
    return api.model.hotsite.Hotsite.HandleRequest(request, id=id)
