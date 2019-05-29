from flask import request, jsonify
from api.lib.responseDecorators import ErrorHandlerAndJsonifier

import common
app = common.app
jwt = common.jwt


import api.model.domain
@app.route("/api/domain", methods=["GET", "POST"])
@app.route("/api/domain/<id>", methods=["GET", "POST", "DELETE"])
@ErrorHandlerAndJsonifier
def domain(id=None):
    return api.model.domain.Domain.HandleRequest(request, id=id)
