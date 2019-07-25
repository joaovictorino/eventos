from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.userGroup import UserGroup
import re

class District(Document, CRUD):
    name = StringField(required=True, unique=True, max_length=200)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(District.pre_save, sender=District)

