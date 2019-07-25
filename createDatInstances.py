#coding: utf-8
import app
import common
import api.model

d = api.model.district.District()
d.drop_collection()
d.name = "Butantã"
d.save()

d = api.model.district.District()
d.name = "Lapa"
d.save()

d = api.model.district.District()
d.name = "Parelheiros"
d.save()

d = api.model.district.District()
d.name = "Sé"
d.save()


c = api.model.categoryGroup.CategoryGroup()
c.drop_collection()
c.name="Esportes"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Saúde"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Educação"
c.save()

u = api.model.user.User()
u.drop_collection()
u.name = "root"
u.email = "root"
u.login = "root"
u.password = "123456"
u.save()
