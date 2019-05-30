from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.plan import Plan

class File(Document, CRUD):
    name = StringField(required=True, max_length=200)
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

