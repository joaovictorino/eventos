from mongoengine import *
from datetime import datetime
from lib.modelBase import CRUD
from model.plan import Plan

class Contract(Document, CRUD):
    name = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    plan = ReferenceField(Plan)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Contract.pre_save, sender=Contract)

