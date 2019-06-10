from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD

class Banner(EmbeddedDocument, CRUD):
    title = StringField(required=True, max_length=200)
    subtitle = StringField(required=True, max_length=200)
    description = StringField(required=True, max_length=1024)
    actionTitle = StringField(required=True, max_length=25)
    hasCounter = BooleanField(default=False)
