from lib.pycac.base import Base

class Hierarquia(Base):
    def __init__(self, chaveAcesso, cd_sistema, dc_sigla, ci_sistema, wsdl_url_hierarquia):
        super(Hierarquia, self).__init__(chaveAcesso, cd_sistema, dc_sigla, ci_sistema)
        self.setWsdl(wsdl_url_hierarquia)

    def getUsuarios(self, ci_hierarquia):
        client = self.getClient()
        service = client.service
        retorno = {}
        usuarios = []
        colunas_uteis = ['cd_integrante', 'nm_integrante', 'in_administrador_hierarquia', 'in_tipo_integrante', 'dc_tipo_integrante']
        try:
            print("INICIANDO BUSCA DE USUÁRIOS")
            requisicao = service.SelecIntegrantes(self.chaveAcesso, ci_hierarquia)
            print("FINALIZANDO BUSCA DE USUÁRIOS")
            if requisicao['CodErro'] == 0:
                for i in requisicao['RecordSets']['RecordSet']:
                    if i['Nome'] == 'Integrantes':
                        for x in i['Linhas']['Linha']:
                            usuario = {}
                            for y in x['Colunas']['Coluna']:
                                if y['Nome'] in colunas_uteis:
                                    usuario[y['Nome']] = y['Valor']
                            usuarios.append(usuario)
                        if len(usuarios) > 0:
                            # TODO: Remover os integrantes que não forem usuários
                            for usuario in usuarios:
                                if usuario['in_tipo_integrante'] == 'G':
                                    del usuarios[usuarios.index(usuario)]
                            retorno['usuarios'] = usuarios
                            retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro no acesso á funcionalidade de listagem de usuários: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'
        return retorno

    def getGrupos(self, ci_hierarquia):
        client = self.getClient()
        service = client.service
        retorno = {}
        grupos = []
        colunas_uteis = ['cd_integrante', 'nm_integrante', 'in_administrador_hierarquia', 'in_tipo_integrante', 'dc_tipo_integrante']
        try:
            print("INICIANDO BUSCA DE GRUPOS")
            requisicao = service.SelecIntegrantes(self.chaveAcesso, ci_hierarquia)
            print("FINALIZANDO BUSCA DE GRUPOS")
            if requisicao['CodErro'] == 0:
                for i in requisicao['RecordSets']['RecordSet']:
                    if i['Nome'] == 'Integrantes':
                        for x in i['Linhas']['Linha']:
                            grupo = {}
                            for y in x['Colunas']['Coluna']:
                                if y['Nome'] in colunas_uteis:
                                    grupo[y['Nome']] = y['Valor']
                            grupos.append(grupo)
                        if len(grupos) > 0:
                            gg = []
                            # TODO: Remover os integrantes que não forem usuários
                            for grupo in grupos:
                                if grupo['in_tipo_integrante'] == 'G':
                                    gg.append(grupo)
                            retorno['grupos'] = gg
                            retorno['status'] = 'OK'
            else:
                raise Exception(requisicao['MsgErro'])
        except Exception as ex:
            print("Erro no acesso á funcionalidade de listagem de usuários: {}".format(ex))
            retorno['msg'] = ex
            retorno['status'] = 'NOK'
        return retorno
