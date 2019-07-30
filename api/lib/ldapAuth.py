import ldap
from common import app

config = app.config


def LoginUser(login, password):
    addr = config["LDAP_ADDR"]
    base = config["LDAP_BASE"]

    user = login + config["LDAP_LOGIN_SUFFIX"]
    search_filter = config["LDAP_USER_INFO_FILTER"] + "=" + login

    connection = ldap.initialize(addr)
    connection.protocol_version = ldap.VERSION3  #define versao 3 do protocolo ldap (recomendado)
    
    userInfo = None
    try:
        connection.bind_s(user,password)
        allInfo = connection.search_s(base,ldap.SCOPE_SUBTREE,search_filter)[0][1]
        userInfo = {
            "name": allInfo["displayName"][0],
            "email": allInfo["mail"][0]
        }
        connection.unbind_s()
    except Exception as ex:
        userInfo = None
    return userInfo
