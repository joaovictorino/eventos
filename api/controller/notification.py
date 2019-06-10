from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.notification
@app.route("/api/notification", methods=["GET", "POST"])
@app.route("/api/notification/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def notification(id=None):
    return api.model.notification.Notification.HandleRequest(request, id=id)
