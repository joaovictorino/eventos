from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
import common

app = Flask(__name__)
CORS(app)
common.app = app

app.config.from_pyfile('config.cfg')

import lib.log
log = lib.log.SetupLog(__name__)
common.log = log

from flask_mongoengine import MongoEngine
db = MongoEngine(app)
common.db = db

from flask_mongoengine import MongoEngineSessionInterface
app.session_interface = MongoEngineSessionInterface(db)
import model

jwt = JWT(app, model.user.User.authenticate, model.user.User.identity)
common.jwt = jwt

import lib.routes
if __name__ == "__main__":
    app.debug = True
    log.info("App running in debug mode")
    app.run()
    
    
