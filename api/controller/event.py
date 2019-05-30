from flask import request, jsonify
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.event
@app.route("/api/event", methods=["GET", "POST"])
@app.route("/api/event/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def event(id=None):
    return api.model.event.Event.HandleRequest(request, id=id)
