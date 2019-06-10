from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.category
@app.route("/api/category", methods=["GET", "POST"])
@app.route("/api/category/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def category(id=None):
    return api.model.category.Category.HandleRequest(request, id=id)
