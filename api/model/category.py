from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.userGroup import UserGroup
from api.model.categoryGroup import CategoryGroup

class Category(Document, CRUD, UserGroupOwnership):
    name = StringField(required=True, unique=False, max_length=200)
    description = StringField(required=False, max_length=2000)
    group = ReferenceField(CategoryGroup)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())
    
    meta = {'indexes': 
         [{'fields': ['$name', '$description']}]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Category.pre_save, sender=Category)

