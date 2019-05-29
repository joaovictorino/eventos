from flask import request, jsonify
from api.lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.eventGroup
@app.route("/api/eventGroup", methods=["GET", "POST"])
@app.route("/api/eventGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def eventGroup(id=None):
    return api.model.eventGroup.EventGroup.HandleRequest(request, id=id)