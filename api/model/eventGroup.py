from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.domain import Domain

class EventGroup(Document, CRUD):
    name = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    domain = ReferenceField(Domain)
    events = ListField(ReferenceField('Event'))
    start_on = DateTimeField()
    end_on = DateTimeField()
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(EventGroup.pre_save, sender=EventGroup)

