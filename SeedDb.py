import requests
import json

baseAddr = "http://localhost:5000/api"


def DoRequest(endpoint, data):
    print("On endpoint '%s'" % (endpoint,))
    href = baseAddr + "/" + endpoint
    headers = {'Content-Type': 'application/json'}
    response = json.loads(requests.post(href, data=json.dumps(data), headers=headers).content)
    status = response["status"]
    print("Status: %s" % (status,))
    id = None
    if status == "ok":
        id = response["data"]["_id"]["$oid"]
        print("Id: %s" % (id,))
    return id

data = {
    "name": "Essential",
    "description": "Plano essential"
}
idPlano = DoRequest("plan", data)
if idPlano is not None:
    data = {
        "name": "SEME",
        "description": "Contrato de SEME",
        "plan": idPlano
    }
    idContrato = DoRequest("contract", data)
    
    if idContrato is not None:
        data = {
            "name": "DSEME",
            "description": "Dominio de SEME",
            "contract": idContrato
        }
        idDominio = DoRequest("domain", data)
        if idDominio is not None:
            data = {
                "name": "EVSEME",
                "description": "Evento de SEME",
                "domain": idDominio
            }
            idEvento = DoRequest("event", data)

data = {
    "name": "p1",
}
perm1 = DoRequest("permission", data)

data = {
    "name": "p2",
}
perm2 = DoRequest("permission", data)

data = {
    "login": "user",
    "name": "Bicho",
    "password": "123456",
    "permissions": [perm1, perm2]
}
idUser = DoRequest("user", data)
