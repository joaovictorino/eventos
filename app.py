from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
import common

app = Flask("Plataforma de Eventos")
CORS(app)
common.app = app

app.config.from_pyfile('config.cfg')

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
    app.run()
