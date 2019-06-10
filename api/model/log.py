from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.user import User

class Log(Document, CRUD):
    user = ReferenceField(User)
    operation = StringField(required=True, max_lenght=100)
    description = StringField(required=False, max_length=2000)
    created_on = DateTimeField(default=datetime.now())

    
