from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.user import User

class Place(Document, CRUD):
    name = StringField(required=True, unique=True, max_length=200)
    description = StringField(required=False, max_length=2000)
    coordinates = GeoPointField()
    street = StringField()
    number = StringField()
    cep = LongField()
    neighborhood = StringField()
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Place.pre_save, sender=Place)

