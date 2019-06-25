from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.calendar import Calendar

class Citizen(Document, CRUD):
    name = StringField(required=True, max_length=200)
    email = EmailField(required=True, unique=True, max_length=100)
    loginMethod = StringField(required=True, unique=True, max_length=10)
    accessToken = StringField(required=False, max_length=2048)
    profilePic = URLField()
    calendar = EmbeddedDocumentField(Calendar)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
class TokenCitizen(object):
    def __init__(self, user):
        self.id = str(user.id)
        self.name = user.name
        self.actor = "citizen"
        
    def toDict(self):
        dic = {}
        for key, value in self.__dict__.items():
            if not callable(value) and "id" != key:
                dic[key] = value
        return dic
        
from mongoengine import signals
signals.pre_save.connect(Citizen.pre_save, sender=Citizen)

