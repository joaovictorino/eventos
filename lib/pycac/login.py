from lib.pycac.base import Base

class Login(Base):

    def __init__(self, chaveAcesso, cd_sistema, dc_sigla, ci_sistema, wsdl_url_login):
        super(Login, self).__init__(chaveAcesso, cd_sistema, dc_sigla, ci_sistema)
        self.setWsdl(wsdl_url_login)   

    def verificaLogin(self, cd_usuario, cd_senha, qtd_tentativas):
        client = self.getClient()
        service = client.service
        retorno = {}
        try:
            print("INICIANDO LOGIN NO CAC")
            requisicao = service.VerificaLogin(self.chaveAcesso, self.cd_sistema, self.dc_sigla, cd_usuario, cd_senha, qtd_tentativas)
            print("FINALIZANDO LOGIN NO CAC")
            propriedades_filtrar = ["ci_hierarquia", "nm_hierarquia", "ci_usuario", "nm_usuario", "ci_hierarquia_usuario", "LoginStatus"]
            
            if(requisicao['CodErro'] == 0):
                user = {}
                for i in requisicao['Atributos']['Atributo']:
                    if (i["Nome"] in propriedades_filtrar):
                        for res in propriedades_filtrar:
                            if(res == i["Nome"]):
                                user[res] = i["Valor"]
                    else:
                        continue
                status_login = self.trataLoginStatus(user['LoginStatus'])
                retorno['usuario'] = user
                if requisicao['MsgErro'] is None:
                    retorno['msg'] = status_login['msg']
                else:
                    retorno['msg'] = (requisicao['MsgErro'] if len(requisicao['MsgErro']) > 0 else status_login['msg'])

                if status_login['status'] == 'OK':
                    retorno['status'] = 'OK'
                else:
                    retorno['status'] = 'NOK'
            else:
                raise Exception(format(requisicao['MsgErro']))
        except Exception as ex:        
            print("Erro na verificação de login: {}".format(ex))
            retorno['msg'] = str(ex)
            retorno['status'] = 'NOK'
        return retorno

    def trataLoginStatus(self, status):
        controle_status = {'0': "Login válido", 
                           '1': "Login válido mas senha está expirando. Faltam alguns dias para a senha expirar.",
                          '2': "Login expirado", 
                          '3': "Login fora de horário permitido", 
                          '4': "Hierarquia não informada", 
                          '5': "Hierarquia não existe", 
                          '6': "Usuário não informado", 
                          '7': "Usuário não existe", 
                          '8': "Usuário não existe nesta hierarquia", 
                          '9': "Usuário está excluído", 
                          '10': "Usuário está inativo", 
                          '11': "Usuário está inativo nesta hierarquia", 
                          '12': "Usuário está bloqueado", 
                          '13': "Usuário está bloqueado nesta hierarquia", 
                          '14': "Senha não informada", 
                          '15': "Senha está expirada", 
                          '16': "Senha Inválida", 
                          '17': "Acesso ao sistema não permitido", 
                          '18': "Erro ao acessar dados"}

        if status == '0':
            return {'status': 'OK', 'msg': controle_status[status], 'cod_status': status}
        else:
            if status == '1':
                return {'status': 'OK', 'msg': controle_status[status], 'cod_status': status}
            else:
                return {'status': 'NOK', 'msg': controle_status[status], 'cod_status': status} 

    def listaRestricoes(self, ci_hierarquia_usuario):
        retorno = {}
        client = self.getClient()
        service = client.service
        colunas_uteis = ['cd_recurso', 'in_visivel', 'in_habilitado', 'cd_tipo_recurso']
        restricoes = []
        try:
            print("INICIANDO LISTAGEM DE RESTRIÇÕES DO USUÁRIO")
            requisicao = service.SelecRestricoes(self.chaveAcesso, ci_hierarquia_usuario, self.cd_sistema)
            print("FINALIZANDO LISTAGEM DE RESTRIÇÕES DO USUÁRIO")
            if requisicao['CodErro'] == 0:
                # TODO: Recuperar as restrições
                if requisicao['RecordSets']['RecordSet'] != None:
                    for i in requisicao['RecordSets']['RecordSet']:
                        if(i['Linhas'] != None):
                            for x in i['Linhas']['Linha']:
                                restricao = {}
                                for y in x['Colunas']['Coluna']:
                                    if y['Nome'] in colunas_uteis:
                                        restricao[y['Nome']] = y['Valor']
                                restricoes.append(restricao)
                    retorno['recursos'] = restricoes
                    retorno['status'] = 'OK'
               
            else:
                raise Exception(requisicao['MsgErro']) 
        except Exception as ex:
            print("Erro na listagem de restrições: {}".format(ex))
            retorno['status'] = 'NOK'
            retorno['msg'] = str(ex)
        return retorno

    def alterarSenhaUsuario(self, cd_usuario, cd_senha_anterior, cd_senha_nova1, cd_senha_nova2 ):
        retorno = {}
        client = self.getClient()
        service = client.service
        try:
            print("INICIANDO TROCA DE SENHA")
            requisicao = service.AlteraSenha(self.chaveAcesso, self.dc_sigla, cd_usuario, cd_senha_anterior, cd_senha_nova1, cd_senha_nova2)
            print("FINALIZANDO TROCA DE SENHA")
            if requisicao['CodErro'] == 0:
                if requisicao['Atributos']['Atributo'] != None:
                    for i in requisicao['Atributos']['Atributo']:
                        if i['Nome'] == 'AlteracaoSenhaStatus':
                            if i['Valor'] == '0':
                                retorno['status'] = 'OK'
                            else:
                                raise Exception(self.trataStatusAlteracaoSenha(i['Valor']))
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro na funcionalidade de alteração de senha: {}".format(ex))
            retorno['status'] = 'NOK'
            retorno['msg'] = str(ex)
        return retorno

    def recuperarSenhaUsuario(self, cd_usuario):
        retorno = {}
        client = self.getClient()
        service = client.service
        try:
            print("INICIANDO RECUPERAÇÃO DE SENHA")
            requisicao = service.RecuperarSenha(self.chaveAcesso, cd_usuario)
            print("FINALIZANDO RECUPERAÇÃO DE SENHA")
            if requisicao['CodErro'] == 0:
                retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro na funcionalidade de recuperação de senha: {}".format(ex))        
            retorno['status'] = 'NOK'
            retorno['msg'] = str(ex)
        return retorno

    def trataStatusAlteracaoSenha(status):
        conf_status = {'0': 'Senha Trocada',
                       '1': 'Hierarquia não informada',
                       '2': 'Usuário não informado', 
                       '3': 'Usuário não existe', 
                       '4': 'Senha anterior não informada', 
                       '5': 'Senha nova igual a anterior', 
                       '6': 'Senha nova não são iguais', 
                       '7': 'Senha nova não informada', 
                       '8': 'Senha nova abaixo do tamanho mínimo', 
                       '9': 'Senha nova acima do tamanho máximo', 
                       '10': 'Senha nova já usada', 
                       '11': 'Erro validação login', 
                       '12': 'Erro ao acessar dados',}
        return conf_status[status]
