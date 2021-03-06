from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD

class Plan(Document, CRUD):
    name = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    isTemplate = BooleanField(default=False)
    events = IntField(required=True)
    eventGroups = IntField(required=True)
    activities = IntField(required=True)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Plan.pre_save, sender=Plan)

