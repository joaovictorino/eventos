from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.district import District
from api.model.uf import UF
import re

class Place(Document, CRUD, UserGroupOwnership):
    name = StringField(required=True, unique=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    city = StringField(required=False, max_length=2000)
    uf = ReferenceField(UF)
    complement = StringField(required=False, max_length=2000)
    coordinates = GeoPointField()
    street = StringField(required=True, max_length=300)
    number = StringField(required=True, max_length=15)
    cep = LongField()
    neighborhood = StringField(max_length=200)
    district = ReferenceField(District)
    category = StringField(default="GLOBAL", max_length=10)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())


    meta = {'indexes': 
         [{'fields': ['$name', '$description', '$city', '$complement', '$street', '$neighborhood']}]
    }
    
    
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if (document.cep and type(document.cep) != int):
            document.cep = re.sub("\D", "", document.cep)
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Place.pre_save, sender=Place)

