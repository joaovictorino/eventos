from flask import request
from api.lib.routeDecorators import *
from api.lib.security import *

import common
app = common.app
jwt = common.jwt

from flask_jwt import jwt_required
import api.model.user
@app.route("/api/user", methods=["GET", "POST"])
@app.route("/api/user/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
@EnsureCredentials
def user(id=None):
    abstraction = api.model.user.User
    return abstraction.HandleRequest(request, id=id)
