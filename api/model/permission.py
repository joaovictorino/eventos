from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.profile import Profile

class Permission(EmbeddedDocument, CRUD):
    profile = ReferenceField(Profile)
    group = ReferenceField('UserGroup')
    
