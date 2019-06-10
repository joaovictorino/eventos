from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD

class Activity(EmbeddedDocument, CRUD):
    name = StringField(required=True, max_length=150)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    
