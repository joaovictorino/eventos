from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.activity import Activity
from api.model.category import Category
from api.model.place import Place
from api.model.file import File

class Event(Document, CRUD, UserGroupOwnership):
    name = StringField(required=True, max_length=200)
    preview = ReferenceField(File)
    description = StringField(required=False, max_length=2000)
    publishDate = DateTimeField(required=True)
    unpublishDate = DateTimeField(required=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    activities = EmbeddedDocumentListField(Activity)
    category = ReferenceField(Category)
    capacity = StringField(max_length=30)
    tags = ListField(StringField(max_length=20))
    hashtags = ListField(StringField(max_length=20))
    externalUrl = StringField(required=False, max_lenght=200)
    hasSubscription = BooleanField(default=False)
    place = ReferenceField(Place)
    complement = StringField(required=False, max_lenght=200)
    isPaid = BooleanField(default=False)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    meta = {'indexes': 
         [{'fields': ['$name']}]
    }
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
            
from mongoengine import signals
signals.pre_save.connect(Event.pre_save, sender=Event)

