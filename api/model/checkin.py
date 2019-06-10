from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.event import Event
from api.model.citizen import Citizen

class Checkin(Document, CRUD):
    event = ReferenceField(Event)
    citizen = ReferenceField(Citizen)
    created_on = DateTimeField(default=datetime.now())
