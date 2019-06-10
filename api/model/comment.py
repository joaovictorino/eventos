from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.citizen import Citizen
from api.model.event import Event

class Comment(Document, CRUD):
    owner = ReferenceField(Citizen)
    event = ReferenceField(Event)
    visible = BooleanField(default=True)
    content = StringField(required=False, max_length=5000)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Comment.pre_save, sender=Comment)

