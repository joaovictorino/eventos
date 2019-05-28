import json
from mongoengine import *
from datetime import datetime
from lib.modelBase import CRUD
import bcrypt
import base64

class User(Document, CRUD):
    login = StringField(required=True, unique=True, max_length=20)
    password = StringField(required=False, max_length=100)
    hashedPassword = BinaryField(required=True, max_length=100)
    name = StringField(required=True, max_length=200)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())
        
    def setPassword(self, val):
        encoded = val.encode("utf-8", errors="ignore")
        self.hashedPassword = bcrypt.hashpw(encoded, bcrypt.gensalt(5))
        
    def verify(self, candidate):
        encoded = candidate.encode("utf-8", errors="ignore")
        valid = bcrypt.checkpw(encoded, self.hashedPassword)
        return valid
        
    @classmethod
    def authenticate(cls, login, password):
        users = cls.objects(login=login)
        if len(users) > 0:
            user = users[0]
            if user.verify(password):
                return TokenUser(user)
                
    @classmethod
    def identity(cls, payload):        
        uid = payload["identity"]
        users = cls.objects(id=uid)
        if len(users) > 0:
            user = users[0]
            return user
            
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        if document.password is not None:
            document.setPassword(document.password)
            document.password = None
        if document.name is not None:
            document.name = document.name.lower()
        
class TokenUser(object):
    def __init__(self, user):
        self.id = str(user.id)
        self.name = user.name
        
    def toDict(self):
        dic = {}
        for key, value in self.__dict__.items():
            if not callable(value) and "id" != key:
                dic[key] = value
        return dic
    
from mongoengine import signals
signals.pre_save.connect(User.pre_save, sender=User)

