from mongoengine import *

class UserGroupOwnership(object):
    owner_user = ReferenceField('User')
    owner_class = ReferenceField('UserGroup')
    
class UserOwnership(object):
    owner_user = ReferenceField('User')
    
class CitizenOwnership(object):
    owner_citizen = ReferenceField('Citizen')
    

