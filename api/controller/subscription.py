from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.subscription
@app.route("/api/subscription", methods=["GET", "POST"])
@app.route("/api/subscription/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def subscription(id=None):
    return api.model.subscription.Subscription.HandleRequest(request, id=id)
