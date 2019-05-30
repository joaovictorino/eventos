from flask import request, jsonify
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.place
@app.route("/api/place", methods=["GET", "POST"])
@app.route("/api/place/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def place(id=None):
    return api.model.place.Place.HandleRequest(request, id=id)
