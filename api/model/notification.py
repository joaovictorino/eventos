from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.user import User

class Notification(Document, CRUD):
    owner = ReferenceField(User)
    content = StringField(required=True, unique=True, max_length=2048)
    created_on = DateTimeField(default=datetime.now())
    
