from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.event
@app.route("/api/event", methods=["GET", "POST"])
@app.route("/api/event/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def event(id=None):
    return api.model.event.Event.HandleRequest(request, id=id)
