from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.district import District
import re

class Place(Document, CRUD, UserGroupOwnership):
    name = StringField(required=True, unique=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    coordinates = GeoPointField()
    street = StringField(required=True, max_length=300)
    number = StringField(required=True, max_length=15)
    cep = LongField()
    neighborhood = StringField(required=True, max_length=200)
    district = ReferenceField(District)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.cep = re.sub("\D", "", document.cep)
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Place.pre_save, sender=Place)

