from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.file import File

class Gallery(EmbeddedDocument, CRUD):
    name = StringField(required=True, max_length=200)
    pics = ListField(ReferenceField(File))
    
    
