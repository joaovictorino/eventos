from flask import request
from api.lib.routeDecorators import *

import common
app = common.app
jwt = common.jwt

import api.model.categoryGroup
@app.route("/api/categoryGroup", methods=["GET", "POST"])
@app.route("/api/categoryGroup/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def categoryGroup(id=None):
    return api.model.categoryGroup.CategoryGroup.HandleRequest(request, id=id)
