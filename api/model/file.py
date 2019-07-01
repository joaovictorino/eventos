from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.userGroup import UserGroup

class File(Document, CRUD, UserGroupOwnership):
    name = StringField(required=True, max_length=200)
    description = StringField(required=True, max_length=1024)
    alt = StringField(required=True, max_length=200)
    author = StringField(required=True, max_length=200)
    origin = StringField(required=True, max_length=200)
    localPath = StringField(required=True, max_length=200)    
    mime = StringField(required=True, max_length=200)    
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(File.pre_save, sender=File)

