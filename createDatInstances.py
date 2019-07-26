#coding: utf-8
import app
import common
import api.model

c = api.model.categoryGroup.CategoryGroup()
c.drop_collection()
c.name="Esportes e Lazer"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Educação"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Cultura"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Comunicação"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Accesibilidade"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Saúde"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Segurança Urbana"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Mobilidade"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Inovação e Tecnologia"
c.save()

c = api.model.categoryGroup.CategoryGroup()
c.name="Verde e do Meio Ambiente"
c.save()

#########################3
u = api.model.user.User()
u.drop_collection()
u.name = "root"
u.email = "root"
u.login = "root"
u.password = "123456"
u.save()

##########################

d = api.model.district.District()
d.drop_collection()
d.name = "Aricanduva/Formosa/Carrão"
d.save()

d = api.model.district.District()
d.name = "Butantã"
d.save()

d = api.model.district.District()
d.name = "Campo Limpo"
d.save()

d = api.model.district.District()
d.name = "Capela do Socorro"
d.save()

d = api.model.district.District()
d.name = "Casa Verde"
d.save()

d = api.model.district.District()
d.name = "Cidade Ademar "
d.save()

d = api.model.district.District()
d.name = "Cidade Tiradentes Ermelino Matarazzo Freguesia/Brasilândia"
d.save()

d = api.model.district.District()
d.name = "Guaianases"
d.save()

d = api.model.district.District()
d.name = "Ipiranga"
d.save()

d = api.model.district.District()
d.name = "Itaim"
d.save()

d = api.model.district.District()
d.name = "Paulista"
d.save()

d = api.model.district.District()
d.name = "Itaquera"
d.save()

d = api.model.district.District()
d.name = "Jabaquara"
d.save()

d = api.model.district.District()
d.name = "Jaçanã/Tremembé"
d.save()

d = api.model.district.District()
d.name = "Lapa"
d.save()

d = api.model.district.District()
d.name = "Mboi Mirim"
d.save()

d = api.model.district.District()
d.name = "Mooca"
d.save()

d = api.model.district.District()
d.name = "Parelheiros"
d.save()

d = api.model.district.District()
d.name = "Penha"
d.save()

d = api.model.district.District()
d.name = "Perus"
d.save()

d = api.model.district.District()
d.name = "Pinheiros"
d.save()

d = api.model.district.District()
d.name = "Pirituba/Jaraguá"
d.save()

d = api.model.district.District()
d.name = "Santana/Tucuruvi"
d.save()

d = api.model.district.District()
d.name = "Santo Amaro"
d.save()

d = api.model.district.District()
d.name = "São Mateus"
d.save()

d = api.model.district.District()
d.name = "São Miguel Paulista"
d.save()

d = api.model.district.District()
d.name = "Sapopemba"
d.save()

d = api.model.district.District()
d.name = "Sé"
d.save()

d = api.model.district.District()
d.name = "Vila Maria/Vila Guilherme"
d.save()

d = api.model.district.District()
d.name = "Vila Mariana"
d.save()

d = api.model.district.District()
d.name = "Vila Prudente"
d.save()

d = api.model.district.District()
d.name = ""
d.save()

##############################
uf = api.model.uf.UF()
uf.name = "RO"
uf.save()

uf = api.model.uf.UF()
uf.name = "AC"
uf.save()

uf = api.model.uf.UF()
uf.name = "AM"
uf.save()

uf = api.model.uf.UF()
uf.name = "RR"
uf.save()

uf = api.model.uf.UF()
uf.name = "PA"
uf.save()

uf = api.model.uf.UF()
uf.name = "AP"
uf.save()

uf = api.model.uf.UF()
uf.name = "TO"
uf.save()

uf = api.model.uf.UF()
uf.name = "MA"
uf.save()

uf = api.model.uf.UF()
uf.name = "PI"
uf.save()

uf = api.model.uf.UF()
uf.name = "CE"
uf.save()

uf = api.model.uf.UF()
uf.name = "RN"
uf.save()

uf = api.model.uf.UF()
uf.name = "PB"
uf.save()

uf = api.model.uf.UF()
uf.name = "PE"
uf.save()

uf = api.model.uf.UF()
uf.name = "AL"
uf.save()

uf = api.model.uf.UF()
uf.name = "SE"
uf.save()

uf = api.model.uf.UF()
uf.name = "BA"
uf.save()

uf = api.model.uf.UF()
uf.name = "MG"
uf.save()

uf = api.model.uf.UF()
uf.name = "ES"
uf.save()

uf = api.model.uf.UF()
uf.name = "RJ"
uf.save()

uf = api.model.uf.UF()
uf.name = "PR"
uf.save()

uf = api.model.uf.UF()
uf.name = "SC"
uf.save()

uf = api.model.uf.UF()
uf.name = "RS"
uf.save()

uf = api.model.uf.UF()
uf.name = "MS"
uf.save()

uf = api.model.uf.UF()
uf.name = "MT"
uf.save()

uf = api.model.uf.UF()
uf.name = "GO"
uf.save()

uf = api.model.uf.UF()
uf.name = "DF"
uf.save()

