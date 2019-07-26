import common
import api.model
from api.lib.routeDecorators import *

app = common.app

@app.route("/api/eventEditInfo")
@ErrorHandlerAndJsonifier
def eventEditInfo():
    info = {}
    info["places"] = api.model.place.Place.objects(state = "ACTIVE").only("name").all()
    info["uf"] = api.model.uf.UF.objects(state = "ACTIVE").all()
    info["districts"] = api.model.district.District.objects(state = "ACTIVE").only("name").all()
    info["categories"] = api.model.category.Category.objects(state = "ACTIVE").only("name", "group").all()
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

@app.route("/api/eventListInfo")
@ErrorHandlerAndJsonifier
def eventListInfor():
    info = {}
    info["categoryGroups"] = api.model.categoryGroup.CategoryGroup.objects(state = "ACTIVE").only("name", "description").all()
    info["categories"] = api.model.category.Category.objects().all()
    info["districts"] = api.model.district.District.objects(state = "ACTIVE").all()
    info["places"] = api.model.place.Place.objects().only("name").all()
    info["events"] = api.model.event.Event.objects().only("name", "place", "category", "publishDate", "startDate", "state").all()
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
    info["places"] = api.model.place.Place.objects(category = "GLOBAL").all()
    return info
    
from flask import request
import json
from bson import ObjectId, json_util
from datetime import datetime
@app.route("/api/fullSearchEvent")
@ErrorHandlerAndJsonifier
def fullSearchEvent():
    event = api.model.event.Event

    params = {}
    for k, v in request.args.items():
        if k == "places.district" or  k == "places._id" or k == "category":
            params[k] = ObjectId(v)
        elif k == "fromDate":
            fromDate = v
            if "toDate" in request.args:
                toDate = request.args["toDate"]
                params["startDate"] = {"$gte": datetime.strptime(fromDate, "%Y-%m-%d"), "$lt": datetime.strptime(toDate, "%Y-%m-%d")}
            else:
                params["startDate"] = {"$gte": datetime.strptime(fromDate, "%Y-%m-%d")}
        elif k == "toDate":
            pass
        else:
            params[k] = v
            
    search_text = ""
    if "search_text" in params:
        search_text = params["search_text"]
        del params["search_text"]
        instances = event.objects().search_text(search_text)
    else:
        instances = event.objects()
    if "__raw__" in params:
        raise Exception("Invalid query")
    
    instances = instances.aggregate({
        "$lookup": {
            "from": "place",
            "localField": "place",
            "foreignField": "_id",
            "as": "places",
        }
        },
        {
            "$unwind": "$places" 
        },
        {
            "$match": params
        }
    )
    print(params)
    #workaround for serializing objectIds
    info = json.loads(json_util.dumps(list(instances)))
    
    return info
