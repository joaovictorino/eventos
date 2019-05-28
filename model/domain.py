from mongoengine import *
from datetime import datetime
from lib.modelBase import CRUD
from model.contract import Contract

class Domain(Document, CRUD):
    name = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    contract = ReferenceField(Contract)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Domain.pre_save, sender=Domain)

