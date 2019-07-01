from flask_jwt import current_identity
import common

def ValidateRequestPermissions(abstraction, request, id=None, readFunc=None, writeFunc=None, deleteFunc=None):
	ret = False
	if common.app.config["ENSURE_PERMISSIONS"]:
		reason = "Unauthorized"
		try:
			if request.method == "GET" and readFunc is not None:
				params = dict(request.args)
				if id is not None:
					params["id"] = id
				ret = readFunc(abstraction, params)
			elif request.method == "POST" and writeFunc is not None:
				ret = writeFunc(abstraction, request.get_json())
			elif request.method == "DELETE" and deleteFunc is not None:
				params = dict(request.args)
				if id is not None:
					params["id"] = id
				ret = deleteFunc(abstraction, params)
		except Exception as ex:
			if hasattr(ex, "message") and ex.message is not None and len(ex.message) > 0:
				reason = ex.message
			
		if not ret:
			raise Exception("Insufficient Permissions: " + reason)
		return ret

from api.lib.ownershipModels import *
from api.model.user import User
from api.model.citizen import Citizen
import pdb
def OwnerPermission(abstraction, params):
	valid = False
	if issubclass(abstraction, CitizenOwnership):
		if "owner_citizen" in params and ("id" not in params or params["id"] is None):
			valid = _RequireIdentity(params["owner_citizen"])
			if not valid:
				raise Exception("invalid identity")
		elif "id" in params and params["id"] is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireIdentity(objs[0].owner_citizen.id):
				valid = True
			else:
				raise Exception("Object not found")
	elif issubclass(abstraction, UserOwnership) or issubclass(abstraction, UserGroupOwnership):
		if "owner_user" in params and ("id" not in params or params["id"] is None):
			valid = _RequireIdentity(params["owner_user"])
			if not valid:
				raise Exception("invalid identity")
		elif  "id" in params and params["id"] is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireIdentity(objs[0].owner_user.id):
				valid = True
			else:
				raise Exception("Object not found")
	elif issubclass(abstraction, Citizen) or issubclass(abstraction, User):
		if  "id" in params and params["id"] is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireIdentity(objs[0].id):
				valid = True
	return valid
		
def GroupPermission(abstraction, params):
	valid = False
	if issubclass(abstraction, UserGroupOwnership):
		if "owner_group" in params and ("id" not in params or params["id"] is None):
			valid = _RequireGroup(params["owner_group"])
			if not valid:
				raise Exception("invalid identity")
		elif  "id" in params and params["id"] is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireGroup(objs[0].owner_group.name):
				valid = True
			else:
				raise Exception("Object not found")
	return valid
				
def GroupAdminPermission(abstraction, params):
	valid = False
	if issubclass(abstraction, UserGroupOwnership):
		if "owner_group" in params and ("id" not in params or params["id"] is None):
			valid = _RequireGroupRole(params["owner_group"])
			if not valid:
				raise Exception("invalid identity")
		elif id is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireGroupRole(objs[0].owner_group.name):
				valid = True
			else:
				raise Exception("Object not found")
	return valid
				
def GroupAdminCreateGroupPermission(abstraction, params):
	valid = False
	if issubclass(abstraction, UserGroupOwnership):
		if "owner_group" in params and ("id" not in params or params["id"] is None):
			valid = _RequireGroupRole(params["owner_group"])
			if not valid:
				raise Exception("invalid identity")
		elif id is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireGroup(objs[0].owner_group.name):
				valid = True
			else:
				raise Exception("Object not found")
	return valid

def SubscriptionAdminPermission(abstraction, params):
	valid = False
	if issubclass(abstraction, UserOwnership):
		if "subscription" in params and ("id" not in params or params["id"] is None):
			valid = _RequireSubscriptionAdmin(params["subscription"])
			if not valid:
				raise Exception("invalid subscriptions")
		elif  "id" in params and params["id"] is not None:
			objs = abstraction.objects(id=params["id"])
			if len(objs) > 0 and _RequireIdentity(objs[0].owner_user):
				valid = True
			else:
				raise Exception("Object not found")
	return valid

def SysAdminPermission(abstraction = None, params = None):
	valid = _RequireSysAdmin()
	if not valid:
		raise Exception("Not sysadmin")
	return valid
	
def DeniedPermission(abstraction = None, params = None):
	valid = False
	return valid
		
def UserPermission(abstraction = None, params = None):
	valid = _RequireActor("user")
	if not valid:
		raise Exception("Not user")
	return valid

def _RequireActor(actorName):
	valid = False
	if current_identity is not None and "actor" in current_identity:
		if current_identity["actor"] == actorName:
			valid = True
	return valid

def _RequireGroup(groupName):
	valid = False
	if current_identity is not None and "permissions" in current_identity:
		for permission in current_identity["permissions"]:
			userGroup, userRole = permission
			if groupName == userGroup:
				valid = True
				break
	return valid
	
def _RequireGroupRole(groupName, roleName = common.app.config["ADMIN_ROLE_NAME"]):
	valid = False
	if current_identity is not None and "permissions" in current_identity:
		for permission in current_identity["permissions"]:
			userGroup, userRole = permission
			if groupName == userGroup and roleName == userRole:
				valid = True
				break
	return valid
	
def _RequireIdentity(selfId):
	valid = False
	if current_identity is not None and "identity" in current_identity:
		valid = str(selfId) == current_identity["identity"]
	return valid
	
from api.model.subscription import Subscription
def _RequireSubscriptionAdmin(subscriptionId):
	valid = False
	if current_identity is not None and "identity" in current_identity:
		subs = Subscription.objects({id: subscriptionId, admin.id: current_identity["identity"]})
		valid = len(subs) > 0
	return valid
	
def _RequireSysAdmin():
	valid = False
	if current_identity is not None and "permissions" in current_identity:
		for permission in current_identity["permissions"]:
			userGroup, userRole = permission
			if userGroup == common.app.config["ADMIN_GROUP_NAME"] and userRole == common.app.config["ADMIN_ROLE_NAME"]:
				valid = True
				break
	return valid
