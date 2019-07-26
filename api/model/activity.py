from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD

class Activity(EmbeddedDocument, CRUD):
    name = StringField(required=True, max_length=150)
    startDate = StringField(required=False, length=5)
    endDate = StringField(required=False, length=5)
    
