from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.category import Category
from api.model.categoryGroup import CategoryGroup
from api.model.place import Place

class Featured(EmbeddedDocument, CRUD):
    title = StringField(required=True, max_length=200)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    category = ReferenceField(Category)
    categoryGroups = ReferenceField(CategoryGroup)
    place = ReferenceField(Place)
