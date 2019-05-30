from flask import request, jsonify
from api.lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.eventCategory
@app.route("/api/category", methods=["GET", "POST"])
@app.route("/api/category/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def event(id=None):
    return api.model.eventCategory.EventCategory.HandleRequest(request, id=id)
