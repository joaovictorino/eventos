from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.file import File

class Partner(EmbeddedDocument, CRUD):
    level = StringField(required=True)
    name = StringField(required=True, max_length=200)
    description = StringField(max_length=1024)
    logoPic = ReferenceField(File)
