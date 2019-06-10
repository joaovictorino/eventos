from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.userGroup import UserGroup
from api.model.activity import Activity
from api.model.category import Category
from api.model.category import CategoryGroup

class Event(Document, CRUD):
    name = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    owner = ReferenceField(UserGroup)
    publishDate = DateTimeField(required=True)
    unpublishDate = DateTimeField(required=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    associatedGroup = ReferenceField(UserGroup)
    activities = EmbeddedDocumentListField(Activity)
    categories = ListField(ReferenceField(Category))
    categoryGroups = ListField(ReferenceField(CategoryGroup))
    tags = ListField(StringField(max_length=20))
    externalUrl = URLField()
    hasSubscription = BooleanField(default=False)
    isPaid = BooleanField(default=False)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Event.pre_save, sender=Event)

