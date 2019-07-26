from lib.pycac.base import Base

class Usuario(Base):
    def __init__(self, chaveAcesso, cd_sistema, dc_sigla, ci_sistema, wsdl_url_usuario):
        super(Usuario, self).__init__(chaveAcesso, cd_sistema, dc_sigla, ci_sistema)
        self.setWsdl(wsdl_url_usuario)

    def getUsuario(self, cd_usuario):
        client = self.getClient()
        service = client.service
        retorno = {}
        colunas_chave = ['ci_usuario', 'cd_usuario', 'nm_usuario']
        try:
            print("INICIANDO BUSCA DE INFORMAÇÕES DO USUÁRIO")
            requisicao = service.SelecUsuarioFiltro(self.chaveAcesso, cd_usuario, "", 0)
            print("FINALIZANDO BUSCA DE INFORMAÇÕES DO USUÁRIO")
            if(requisicao['CodErro'] == 0):
                # print(requisicao['RecordSets'])
                for i in requisicao['RecordSets']['RecordSet']:
                    for x in i['Linhas']['Linha']:
                        for y in x['Colunas']['Coluna']:
                            if y['Nome'] in colunas_chave:
                                retorno[y['Nome']] = y['Valor']
                retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])            
        except Exception as ex:
            print("Erro no acesso ás informações do usuário: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'
        return retorno            

    def getRecursosUsuario(self, ci_hierarquia_usuario):
        client = self.getClient()
        service = client.service
        retorno = {}
        recursos = []
        colunas_uteis = ['cd_recurso', 'in_visivel', 'in_habilitado', 'situacao']
        try:
            print("INICIANDO BUSCA DE RECURSOS DO USUÁRIO")
            requisicao = service.SelecUsuarioRecursos(self.chaveAcesso, self.ci_sistema, ci_hierarquia_usuario)
            print("FINALIZANDO BUSCA DE RECURSOS DO USUÁRIO")
            if requisicao['CodErro'] == 0:
                for i in requisicao['RecordSets']['RecordSet']:
                    if i['Nome'] == 'UsuarioRecursos':
                        if i['Linhas'] != None:
                            # TODO: Implementar retorno de recursos
                            for x in i['Linhas']['Linha']:
                                recurso = {}
                                for y in x['Colunas']['Coluna']:
                                    if y['Nome'] in colunas_uteis:
                                        recurso[y['Nome']] = y['Valor']
                                recursos.append(recurso)
                retorno['recursos'] = recursos 
                retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro no acesso aos recursos do usuário: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'
        return retorno
    
    def getHierarquiaUsuario(self, cd_usuario):
        client = self.getClient()
        service = client.service
        retorno = {}
        colunas_uteis = ['ci_hierarquia_usuario', 'nm_usuario',]
        usuario = {}
        try:
            print("INICIANDO BUSCA DE HIERARQUIA DO USUÁRIO")
            requisicao = service.SelecUsuarioHierarquia(self.chaveAcesso, cd_usuario, self.dc_sigla)
            print("FINALIZANDO BUSCA DE HIERARQUIA DO USUÁRIO")
            if requisicao['CodErro'] == 0:
                for i in requisicao['RecordSets']['RecordSet']:
                    if i['Nome'] == 'UsuarioHierarquia':
                        if i['Linhas'] != None:
                            for x in i['Linhas']['Linha']:
                                for y in x['Colunas']['Coluna']:
                                    if y['Nome'] in colunas_uteis:
                                        usuario[y['Nome']] = y['Valor']
                                
                retorno['usuario'] = usuario
                retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro no acesso á hierarquia do usuário: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'

        return retorno

    def getUsuarioInformacao(self, cd_usuario, ci_hierarquia):
        client = self.getClient()
        service = client.service
        colunas_uteis = ['tx_email_usuario', 'nm_usuario', 'tx_complemento_usuario']
        retorno = {}
        usuario = {}
        requisicao = service.SelecUm(self.chaveAcesso, cd_usuario, ci_hierarquia)
        try:
            if requisicao['CodErro'] == 0:
                for i in requisicao['RecordSets']['RecordSet']:
                    if i['Nome'] == 'UmUsuario':
                        if i['Linhas'] != None:
                            for x in i['Linhas']['Linha']:
                                for y in x['Colunas']['Coluna']:
                                    if y['Nome'] in colunas_uteis:
                                        usuario[y['Nome']] = y['Valor']
                retorno['usuario'] = usuario
                retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro no acesso á hierarquia do usuário: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'
        return retorno

    def getUsuarioGrupos(self, cd_hierarquia, cd_hierarquia_usuario):
        client = self.getClient()
        service = client.service
        retorno = {}
        grupos = []
        grupos_relacionados = []
        try:
            print("FINALIZANDO BUSCA DE GRUPOS RELACIONADOS")
            requisicao = service.SelecUsuarioGrupos(self.chaveAcesso, cd_hierarquia, cd_hierarquia_usuario)
            print(requisicao)
            print("FINALIZANDO BUSCA DE GRUPOS RELACIONADOS")
            if requisicao['CodErro'] == 0:
                for i in requisicao['RecordSets']['RecordSet']:
                    if i['Nome'] == 'UsuarioGrupos':
                        if i['Linhas'] != None:
                            for x in i['Linhas']['Linha']:
                                grupo = {}
                                for y in x['Colunas']['Coluna']:
                                    grupo[y['Nome']] = y['Valor']
                                grupos.append(grupo)
                        if(len(grupos) > 0):
                            for g in grupos:
                                if g['situacao'] == 'R':
                                    grupos_relacionados.append(g)             
                retorno['status'] = 'OK'
                retorno['grupos'] = grupos_relacionados
                                                   
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro no acesso á hierarquia do usuário: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'
        return retorno
