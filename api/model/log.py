from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.user import User
from api.model.userGroup import UserGroup

class Log(Document, CRUD, UserGroupOwnership):
    operation = StringField(required=True, max_lenght=100)
    description = StringField(required=False, max_length=2000)
    created_on = DateTimeField(default=datetime.now())
