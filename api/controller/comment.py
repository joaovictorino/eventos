from flask import request
from api.lib.routeDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt

import api.model.comment
@app.route("/api/comment", methods=["GET", "POST"])
@app.route("/api/comment/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def comment(id=None):
    return api.model.comment.Comment.HandleRequest(request, id=id)
