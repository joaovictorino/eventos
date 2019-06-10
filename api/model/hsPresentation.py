from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.file import File

class Presentation(EmbeddedDocument, CRUD):
    title = StringField(required=True, max_length=200)
    subtitle = StringField(required=True, max_length=200)
    description = StringField(required=True, max_length=1024)
    pic = ReferenceField(File)
    places = IntField(default=0)
    events = IntField(default=0)
