from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.file
@app.route("/api/file", methods=["GET", "POST"])
@app.route("/api/file/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def file(id=None):
    return api.model.file.File.HandleRequest(request, id=id)
