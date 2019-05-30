from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD

class EventCategory(Document, CRUD):
    name = StringField(required=True, unique=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(EventCategory.pre_save, sender=EventCategory)

