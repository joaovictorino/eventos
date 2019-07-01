use portalDeEventos
db.subscription.insert({"id":ObjectId("5d0a24f7812d74751423b780"),"name":"Master","description":"This is platform admistration subscription"})
db.userGroup.insert({"id":ObjectId("5d0a24f7812d74751423b781"),"name":"Administrator","description":"This is admin group","subscription":ObjectId("5d0a24f7812d74751423b780")})
db.profile.insert({"id":ObjectId("5d0a24f7812d74751423b782"),"name":"Administrator","description":"This is admin profile"})
db.user.insert({"id":ObjectId("5d0a24f7812d74751423b783"),"name":"administrator","email":"root@localhost.com","login":"admin","accessToken":{"$binary":"JDJiJDA1JEVnODVZWldjc1VtRkp5SGxBb2ZCOGVUeU13eTNJY1NTZXE3N0c4UnlyUHdjNVkubk1sc2ZP","$type":"00"},"permissions":[{"profile":ObjectId("5d0a24f7812d74751423b782"),"group":ObjectId("5d0a24f7812d74751423b781")}]})
