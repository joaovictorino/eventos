import common
common.app.config["ENSURE_PERMISSIONS"] = True

class LazyGet(object):
    def __getitem__(self, item):
        return identity[item]
    def __contains__(self, item):
        return item in identity

import flask_jwt
flask_jwt.current_identity = LazyGet()

from api.lib.ownershipModels import *
from api.lib.security import *

class RequestMock(object):
    def __init__(self, method, args={}):
        self.method = method
        self.args = args
        
    def get_json():
        return args

global objects
class AbstractionMock():
    @classmethod
    def objects(cls, *args, **kwargs):
        return objects

class AbstractionUserGroupMock(AbstractionMock, UserGroupOwnership):
    pass

class AbstractionUserMock(AbstractionMock, UserOwnership):
    pass
    
class AbstractionCitizenMock(AbstractionMock, CitizenOwnership):
    pass

class AbstractionInstanceMock(object):
    def __init__(self, dataMap):
        self.data = dataMap
        
    def __getattribute__(self, attr):
        return object.__getattribute__(self, "data")[attr]

userMock1 = AbstractionInstanceMock({
    "id": "userid",
    "name": "root"
})

userMock2 = AbstractionInstanceMock({
    "id": "citizenid",
    "name": "toor"
})

groupMock1 = AbstractionInstanceMock({
    "id": "456",
    "name": "group"
})

groupMock2 = AbstractionInstanceMock({
    "id": "654",
    "name": "puorg"
})

identityUser = {
    "identity": "userid",
    "permissions": [['group', common.app.config["ADMIN_ROLE_NAME"]]],
    "actor": "user"
}

identityUserLowp = {
    "identity": "userid",
    "permissions": [['group', 'Ordinary']],
    "actor": "user"
}

identityCitizen = {
    "identity": "citizenid",
    "actor": "citizen"
}

identitySysadmin = {
    "identity": "adminid",
    "permissions": [[common.app.config["ADMIN_GROUP_NAME"], common.app.config["ADMIN_ROLE_NAME"]]],
    "actor": "user"
}

################
print("##TestCase Owner Citizen, filter (pass): ", end="")
request = RequestMock("GET", {"owner_citizen": userMock2.id})
identity = identityCitizen
abstraction = AbstractionCitizenMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
assert ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
print("OK")
################
print("##TestCase Owner Citizen, filter (fail): ", end="")
request = RequestMock("GET", {"owner_citizen": "invalid_id"})
identity = identityCitizen
abstraction = AbstractionCitizenMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase Owner Citizen, id (pass): ", end="")
request = RequestMock("GET")
identity = identityCitizen
abstraction = AbstractionCitizenMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
assert ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
print("OK")
################
print("##TestCase Owner Citizen, id (fail): ", end="")
request = RequestMock("GET")
identity = identityCitizen
abstraction = AbstractionCitizenMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock1,
    "owner_user": userMock1
})]
id = 1
try:
    ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
################
print("##TestCase Owner User, filter (pass): ", end="")
request = RequestMock("GET", {"owner_user": userMock1.id})
identity = identityUser
abstraction = AbstractionUserMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
assert ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
print("OK")
################
print("##TestCase Owner User, filter (fail): ", end="")
request = RequestMock("GET", {"owner_user": "invalid_id"})
identity = identityUser
abstraction = AbstractionUserMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase Owner User, id (pass): ", end="")
request = RequestMock("GET")
identity = identityUser
abstraction = AbstractionUserMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
assert ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
print("OK")
################
print("##TestCase Owner User, id (fail): ", end="")
request = RequestMock("GET")
identity = identityUser
abstraction = AbstractionUserMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock2
})]
id = 1
try:
    ValidateRequestPermissions(abstraction, request, id, OwnerPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
################
print("##TestCase Group, wrong abstraction (fail): ", end="")
request = RequestMock("GET", {"owner_user": userMock1.id})
identity = identityUser
abstraction = AbstractionUserMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    assert ValidateRequestPermissions(abstraction, request, id, GroupPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase Group, filter (ok): ", end="")
request = RequestMock("GET", {"owner_group": groupMock1.name})
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
ValidateRequestPermissions(abstraction, request, id, GroupPermission)
print("OK")
################
print("##TestCase Group, filter (fail): ", end="")
request = RequestMock("GET", {"owner_group": "invalid_id"})
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    ValidateRequestPermissions(abstraction, request, id, GroupPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase Group, id (ok): ", end="")
request = RequestMock("GET")
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
ValidateRequestPermissions(abstraction, request, id, GroupPermission)
print("OK")
################
print("##TestCase Group, id (fail): ", end="")
request = RequestMock("GET")
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock2,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
try:
    ValidateRequestPermissions(abstraction, request, id, GroupPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
################
print("##TestCase GroupAdmin, wrong abstraction (fail): ", end="")
request = RequestMock("GET", {"owner_user": groupMock1.id})
identity = identityUser
abstraction = AbstractionUserMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    assert ValidateRequestPermissions(abstraction, request, id, GroupAdminPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase GroupAdmin, filter (ok): ", end="")
request = RequestMock("GET", {"owner_group": groupMock1.name})
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
ValidateRequestPermissions(abstraction, request, id, GroupAdminPermission)
print("OK")
################
print("##TestCase GroupAdmin, filter non admin (fail): ", end="")
request = RequestMock("GET", {"owner_group": groupMock1.name})
identity = identityUserLowp
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    ValidateRequestPermissions(abstraction, request, id, GroupAdminPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase GroupAdmin, id (ok): ", end="")
request = RequestMock("GET")
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
ValidateRequestPermissions(abstraction, request, id, GroupAdminPermission)
print("OK")
################
print("##TestCase GroupAdmin, id non admin (fail): ", end="")
request = RequestMock("GET")
identity = identityUserLowp
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
try:
    ValidateRequestPermissions(abstraction, request, id, GroupAdminPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
################
print("##TestCase GroupAdminCreate, ordinay user (fail): ", end="")
request = RequestMock("GET", {"owner_user": groupMock1.id})
identity = identityUserLowp
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    assert ValidateRequestPermissions(abstraction, request, id, GroupAdminCreateGroupPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase GroupAdminCreate, filter (ok): ", end="")
request = RequestMock("GET", {"owner_group": groupMock1.name})
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
ValidateRequestPermissions(abstraction, request, id, GroupAdminCreateGroupPermission)
print("OK")
################
print("##TestCase GroupAdminCreate, id (ok): ", end="")
request = RequestMock("GET")
identity = identityUserLowp
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
ValidateRequestPermissions(abstraction, request, id, GroupAdminCreateGroupPermission)
print("OK")
################
################
print("##TestCase Sysadmin, ordinay user (fail): ", end="")
request = RequestMock("GET", {"owner_user": groupMock1.id})
identity = identityUser
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    assert ValidateRequestPermissions(abstraction, request, id, SysAdminPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase Sysadmin, id (ok): ", end="")
request = RequestMock("GET")
identity = identitySysadmin
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
ValidateRequestPermissions(abstraction, request, id, SysAdminPermission)
print("OK")
################
################
print("##TestCase User, citizen (fail): ", end="")
request = RequestMock("GET", {"owner_user": groupMock1.id})
identity = identityCitizen
abstraction = AbstractionCitizenMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = None
try:
    assert ValidateRequestPermissions(abstraction, request, id, UserPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
print("##TestCase User, (ok): ", end="")
request = RequestMock("GET")
identity = identityUserLowp
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
ValidateRequestPermissions(abstraction, request, id, UserPermission)
print("OK")
################
################
print("##TestCase Denied (fail): ", end="")
request = RequestMock("GET")
identity = identitySysadmin
abstraction = AbstractionUserGroupMock
objects = [AbstractionInstanceMock({
    "owner_group": groupMock1,
    "owner_citizen": userMock2,
    "owner_user": userMock1
})]
id = 1
try:
    assert ValidateRequestPermissions(abstraction, request, id, DeniedPermission)
    print("Fail")
    exit(1)
except Exception as ex:
    if "Insufficient Permission" in str(ex):
        print("OK")
    else:
        print("Fail")
        print(ex)
        exit(1)
################
