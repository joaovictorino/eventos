from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.notification
@app.route("/api/notification", methods=["GET", "POST"])
@app.route("/api/notification/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def notification(id=None):
    return api.model.notification.Notification.HandleRequest(request, id=id)
