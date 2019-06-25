from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.user import User
from api.model.userGroup import UserGroup

class Notification(Document, CRUD, UserGroupOwnership):
    content = StringField(required=True, unique=True, max_length=2048)
    created_on = DateTimeField(default=datetime.now())
    
