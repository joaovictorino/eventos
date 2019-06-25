from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.calendar
@app.route("/api/calendar", methods=["GET", "POST"])
@app.route("/api/calendar/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def calendar(id=None):
    return api.model.calendar.Calendar.HandleRequest(request, id=id)
