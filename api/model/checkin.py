from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.lib.ownershipModels import *
from api.model.event import Event
from api.model.citizen import Citizen

class Checkin(Document, CRUD, CitizenOwnership):
    event = ReferenceField(Event)
    created_on = DateTimeField(default=datetime.now())
