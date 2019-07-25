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
    
@app.route("/api/categoryListInfo")
@ErrorHandlerAndJsonifier
def categoryListInfor():
    info = {}
    info["categoryGroups"] = api.model.categoryGroup.CategoryGroup.objects(state = "ACTIVE").only("name", "description").all()
    info["categories"] = api.model.category.Category.objects(state = "ACTIVE").all()
    return info
    
