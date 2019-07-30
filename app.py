from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_compress import Compress
import common

app = Flask(__name__)
common.app = app

app.config.from_pyfile('config.cfg')

CORS(app)
Compress(app)

from lib.util import SetupEnv
SetupEnv()

import lib.log
log = lib.log.SetupLog(__name__)
common.log = log

from flask_mongoengine import MongoEngine
db = MongoEngine(app)
common.db = db

from flask_mongoengine import MongoEngineSessionInterface
app.session_interface = MongoEngineSessionInterface(db)

import api.model

import api.lib.jwt
jwt = JWT(app, None, api.lib.jwt.Identity)
common.jwt = jwt
api.lib.jwt.SetupJwt()

import api.lib.routes
import api.controller
if __name__ == "__main__":
    app.debug = True
    log.info("App running in debug mode")
    app.run(host="localhost", port=80)
