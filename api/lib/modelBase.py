from mongoengine import *
from bson import ObjectId

class CRUD(object):
    @classmethod
    def HandleRequest(cls, request, **kwargs):
        ret = None
        if request.method == "GET":
            if "id" in kwargs and kwargs["id"] is not None:
                instances = cls.objects(id=kwargs['id'])
                if len(instances) > 0:
                    ret = instances[0]
                else:
                    raise Exception("Object not found")
            else:
                instances = cls.objects()
                ret = instances
            
        elif request.method == "POST":
            instance = None
            if "id" in kwargs and kwargs["id"] is not None:
                instances = cls.objects(id=kwargs['id'])
                if len(instances) > 0:
                    instance = instances[0]
            
            if instance is None:
                instance = cls()
            
            data = request.get_json()
            for key in data:
                if key in cls._fields:
                    field = cls._fields[key]
                    fieldValue = data[key]
                    if type(field) is ReferenceField:
                        print ("oK")
                        print (str(ObjectId(fieldValue)))
                        referredInstance = field.document_type.objects(id=ObjectId(fieldValue))
                        print (referredInstance)
                        if len(referredInstance) > 0:
                            fieldValue = referredInstance[0].to_dbref()
                        else:
                            raise Exception("Referred object not found")
                    setattr(instance, key, fieldValue)
            instance.save()
            instance.cascade_save()
            ret = instance
        
        elif request.method == "DELETE":
            if "id" in kwargs and kwargs["id"] is not None:
                instances = cls.objects(id=kwargs['id'])
                if len(instances) > 0:
                    instance = instances[0]
                    instance.delete()
                else:
                    raise Exception("Object not found")
            else:
                    raise Exception("Object not selected")
        else:
            raise Exception("No such operation")
        return ret
