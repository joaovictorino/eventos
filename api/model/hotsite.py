from mongoengine import *
from datetime import datetime
from api.lib.modelBase import CRUD
from api.model.userGroup import UserGroup
from api.model.file import File
from api.model.hsBanner import Banner
from api.model.hsPresentation import Presentation
from api.model.hsFeatured import Featured
from api.model.hsGallery import Gallery
from api.model.hsPartner import Partner

class Hotsite(Document, CRUD):
    owner = ReferenceField(UserGroup)
    ownerAddress = StringField(required=True, max_length=2048)
    ownerContact = StringField(required=True, max_length=2048)
    logoPic = ReferenceField(File)
    publishDate = DateTimeField(required=True)
    removeDate = DateTimeField(required=True)
    banner = EmbeddedDocumentField(Banner)
    presentation = EmbeddedDocumentField(Presentation)
    featured = EmbeddedDocumentListField(Presentation)
    galleries = EmbeddedDocumentListField(Gallery)
    partners = EmbeddedDocumentListField(Partner)
    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField(default=datetime.now())

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_on = datetime.now()
        
from mongoengine import signals
signals.pre_save.connect(Hotsite.pre_save, sender=Hotsite)

