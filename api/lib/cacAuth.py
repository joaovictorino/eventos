from lib.pycac.login import Login
from lib.pycac.usuario import Usuario
from common import app

config = app.config
authenticator = Login(config["CAC_KEY"], config["CAC_SYSCODE"], config["CAC_LEMMA"], config["CAC_SYSTEM"], config["CAC_WSDL_LOGIN"])

def LoginUser(username, password):
    ret = None
    retry = 1
    try:
        ret = authenticator.verificaLogin(username, password, 1)
    except Exception as ex:
        print(ex)
        raise Exception("Authentication unavailable")
    return ret
