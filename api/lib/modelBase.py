from mongoengine import *
from bson import ObjectId

class CRUD(object):
    deleted = BooleanField(default = False)
    
    @classmethod
    def HandleRequest(cls, request, **kwargs):
        ret = None
        if request.method == "GET":
            ret = cls.DoRead(request, **kwargs)
        elif request.method == "POST":
            ret = cls.DoWrite(request, **kwargs)
        elif request.method == "DELETE":
            ret = cls.DoDelete(request, **kwargs)
        else:
            raise Exception("No such operation")
        return ret
        
    @classmethod
    def DoRead(cls, request, **kwargs):
        ret = None
        if "id" in kwargs and kwargs["id"] is not None:
            instances = cls.objects(id=kwargs['id'], deleted=False)
            if len(instances) > 0:
                ret = instances[0]
            else:
                raise Exception("Object not found")
        else:                
            params = {k: v for k, v in request.args.items()}
            if "__raw__" in params:
                raise Exception("Invalid query")
            instances = cls.objects(**params, deleted=False)
            ret = list(instances)
        return ret
        
    @classmethod
    def DoWrite(cls, request, **kwargs):
        ret = None
        instance = None
        if "id" in kwargs and kwargs["id"] is not None:
            instances = cls.objects(id=kwargs['id'], deleted=False)
            if len(instances) > 0:
                instance = instances[0]
        
        if instance is None:
            instance = cls()
        
        data = request.get_json()
        for key in data:
            fieldValue = data[key]
            FillInInstanceWithData(instance, key, fieldValue)
        
        instance.save()
        instance.cascade_save()
        ret = instance
        return ret
        
    @classmethod
    def DoDelete(cls, request, **kwargs):
        ret = None
        if "id" in kwargs and kwargs["id"] is not None:
            instances = cls.objects(id=kwargs['id'])
            if len(instances) > 0:
                instance = instances[0]
                #Never delete
                instance.deleted=True
                instance.save()
            else:
                raise Exception("Object not found")
        else:
                raise Exception("Object not selected")
        return ret
        

def FillInInstanceWithData(instance, fieldName, fieldValue):
    if fieldName in instance._fields:
        field = instance._fields[fieldName]
        #Handle ReferenceField
        if type(field) is ReferenceField:
            referredInstance = field.document_type.objects(id=ObjectId(fieldValue))
            if len(referredInstance) > 0:
                fieldValue = referredInstance[0].to_dbref()
            else:
                raise Exception("Referred object not found")
            setattr(instance, fieldName, fieldValue)
        #Handle ListField(ReferenceField)
        elif type(field) is ListField and type(field.field) is ReferenceField and type(fieldValue) == list:
            instanceList = getattr(instance, fieldName)
            for singleValue in fieldValue:
                referredInstance = field.field.document_type.objects(id=ObjectId(singleValue))
                if len(referredInstance) > 0:
                    fieldValue = referredInstance[0].to_dbref()
                    instanceList.append(fieldValue)                                
                else:
                    raise Exception("Referred object not found")
        #Handle EmbeddedDocument
        elif type(field) is EmbeddedDocumentField:
            embeddedInstance = field.field.document_type(fieldValue)
            setattr(instance, fieldName, embeddedInstance)
        #Handle EmbeddedListDocument
        elif type(field) is EmbeddedDocumentListField:
            if type(fieldValue) is not list:
                fieldValue = [fieldValue]
            classField = getattr(instance, fieldName)
            for embedded in fieldValue:
                embeddedInstance = field.field.document_type(**embedded)
                classField.append(embeddedInstance)                
        else:
            setattr(instance, fieldName, fieldValue)
