from mongoengine import *
from api.lib.modelBase import CRUD

class UF(Document, CRUD):
    name = StringField(required=True, unique=False, max_length=200)
    

    
