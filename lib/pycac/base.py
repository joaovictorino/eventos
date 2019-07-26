"""
    A classe abaixo é responsável por encapsular toda a parte de integração com o webservice via protocolo SOAP
"""

import zeep
from zeep.cache import SqliteCache
from zeep.transports import Transport

class Base(object):
    def __init__(self, chaveAcesso, cd_sistema, dc_sigla, ci_sistema):
        self.chaveAcesso = chaveAcesso
        self.cd_sistema = cd_sistema
        self.dc_sigla = dc_sigla
        self.ci_sistema = ci_sistema


    def getClient(self):
        try:
            transport = Transport(cache=SqliteCache())
            return zeep.Client(self.wsdl, transport=transport)
        except Exception as err:
            print("Erro na conexão com o webservice: {}".format(err))
    
    def setWsdl(self, wsdl):
        self.wsdl = wsdl

