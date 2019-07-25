from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.lib.socialIntegration import *
from api.model.calendar import Calendar

class Citizen(Document, CRUD):
    name = StringField(required=True, max_length=200)
    login = StringField(required=True, unique=True, max_length=100)
    email = EmailField(max_length=100)
    loginMethod = StringField(required=True, unique=True, max_length=10)
    password = StringField(required=False, max_length=100)
    accessToken = StringField(required=False, max_length=2048)
    profilePic = URLField()
    calendar = EmbeddedDocumentField(Calendar)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())
    
    def setPassword(self, val):
        encoded = val.encode("utf-8", errors="ignore")
        self.accessToken = bcrypt.hashpw(encoded, bcrypt.gensalt(5))
        
    def verify(self, candidate):
        encoded = candidate.encode("utf-8", errors="ignore")
        valid = bcrypt.checkpw(encoded, self.accessToken)
        return valid
        
    @classmethod
    def authenticate(cls, login, password):
        ret = None
        if login.startswith("ma:"):
            citizens = cls.objects(login=login)
            if len(citizens) > 0:
                citizen = citizens[0]
                if citizen.verify(password):
                    ret = TokenUser(citizen)
        else:
            userInfo = None
            loginMethod = None
            if login == "fb:":
                userInfo = FacebookTokenValidate(password)
                loginMethod = "facebook"
            elif login == "go:":
                userInfo = GoogleTokenValidate(password)
                loginMethod = "google"
            
            if userInfo is not None:
                citizens = cls.objects(login=userInfo.login)
                if len(citizens) > 0:
                    citizen = citizens[0]
                else:
                    citizen = Citizen()
                    citizen.name = userInfo.name
                    citizen.email = userInfo.email
                    citizen.profilePic = userInfo.picture
                    citizen.login = userInfo.login
                    citizen.loginMethod = loginMethod
                    citizen.save()
                ret = TokenUser(citizen)
        
        if ret is None:
            raise("Bad user")
        return ret
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        if document.password is not None:
            document.setPassword(document.password)
            document.password = None
        if document.login is None:
            document.login = "ma:" + document.email.lower()
        if document.loginMethod is None:
            document.loginMethod = "credentials"

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

