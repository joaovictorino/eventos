from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.event import Event

class Calendar(EmbeddedDocument, CRUD):
    events = ListField(ReferenceField(Event))
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Calendar.pre_save, sender=Calendar)

