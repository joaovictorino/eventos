from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.subscription import Subscription
from api.model.user import User

class UserGroup(Document, CRUD, UserOwnership):
    name = StringField(required=True, unique=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    subscription = ReferenceField(Subscription)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
 
from mongoengine import signals
signals.pre_save.connect(UserGroup.pre_save, sender=UserGroup)

