import common
import api.model
from api.lib.routeDecorators import *

app = common.app

@app.route("/api/eventEditInfo")
@ErrorHandlerAndJsonifier
def eventEditInfo():
    info = {}
    info["districts"] = api.model.district.District.objects(state = "ACTIVE").only("name").all()
    info["categoryGroups"] = api.model.categoryGroup.CategoryGroup.objects(state = "ACTIVE").only("name", "description").all()
    
    return info
    
@app.route("/api/categoryEditInfo")
@ErrorHandlerAndJsonifier
def categoryEditInfor():
    info = {}
    info["categoryGroups"] = api.model.categoryGroup.CategoryGroup.objects(state = "ACTIVE").only("name", "description").all()
    return info
    
    
@app.route("/api/placeEditInfo")
@ErrorHandlerAndJsonifier
def placeEditInfor():
    info = {}
    info["uf"] = api.model.uf.UF.objects(state = "ACTIVE").all()
    info["districts"] = api.model.district.District.objects(state = "ACTIVE").all()
    return info

@app.route("/api/categoryListInfo")
@ErrorHandlerAndJsonifier
def categoryListInfor():
    info = {}
    info["categoryGroups"] = api.model.categoryGroup.CategoryGroup.objects(state = "ACTIVE").only("name", "description").all()
    info["categories"] = api.model.category.Category.objects().all()
    return info
    
@app.route("/api/placeListInfo")
@ErrorHandlerAndJsonifier
def placeListInfor():
    info = {}
    info["uf"] = api.model.uf.UF.objects(state = "ACTIVE").all()
    info["districts"] = api.model.district.District.objects(state = "ACTIVE").all()
    info["places"] = api.model.place.Place.objects().all()
    return info
