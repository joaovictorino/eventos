from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.log
@app.route("/api/log", methods=["GET", "POST"])
@app.route("/api/log/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def log(id=None):
    return api.model.log.Log.HandleRequest(request, id=id)
