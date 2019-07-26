from flask import request
from common import app
from api.model.file import File
import uuid
import os
import re
import json

def Upload(request, acceptedExtensions = []):
    uploadReferences = []
    
    acceptedExtensions = [extension.lower() for extension in acceptedExtensions]
    
    if request.method == 'POST':
        if len(request.files) == 0:
            raise Exception('File not sent')
        if "meta" not in request.form:
            raise Exception('Meta not sent')
            
        else:
            uploadedFiles = 0
            for fileField in request.files:
                meta = json.loads(request.form["meta"])
                file = request.files[fileField]
                if file.name == '':
                    continue
                    
                if file:
                    extension = GetFileExtension(file.name) or ""
                    if len (acceptedExtensions) == 0  or extension in acceptedExtensions:
                        filename = GetUUID()
                        if len(extension) > 0:
                            filename += "." + extension
                        
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        
                        f = SaveFileMeta(file, fileField, filename, meta)                        
                        uploadReferences.append(f)
                    else:
                        raise Exception("Invalid file(s) extension")
                    
                    uploadedFiles += 1
            if 0 == uploadedFiles:
                raise Exception("No file(s) uploaded")
    else:
        raise Exception("Invalid request type")
    return uploadReferences

def GetFileExtension(filename):
    extension = None
    extRe = re.search("\.(\w+)$", filename)
    if extRe is not None:
        extension = extRe.group(1).lower()
    return extension
    
def GetUUID():
    id = uuid.uuid1().hex
    return id
    
def SaveFileMeta(file, fileField, filename, meta):
    f = File()
    f.name = file.name
    f.origin = fileField
    f.localPath = filename
    f.mime = file.mimetype
    
    if "description" in meta:
        f.description = meta["description"]
    if "alt" in meta:
        f.alt = meta["alt"]
    if "author" in meta:
        f.author = meta["author"]
            
    f.save()
    
    return f
