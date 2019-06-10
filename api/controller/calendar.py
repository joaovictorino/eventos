from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.calendar
@app.route("/api/calendar", methods=["GET", "POST"])
@app.route("/api/calendar/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def calendar(id=None):
    return api.model.calendar.Calendar.HandleRequest(request, id=id)
