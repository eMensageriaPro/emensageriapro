#coding:utf-8
from emensageriapro.padrao import executar_sql

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

TRANSMISSOR_STATUS_CADASTRADO = 0
TRANSMISSOR_STATUS_ENVIADO = 1
TRANSMISSOR_STATUS_ENVIADO_ERRO = 2
TRANSMISSOR_STATUS_CONSULTADO = 3
TRANSMISSOR_STATUS_CONSULTADO_ERRO = 4


def retirar_pontuacao_cpf_cnpj(cpf_cnpj):
    for a in './-_':
        cpf_cnpj = cpf_cnpj.replace(a, '')
    return cpf_cnpj


def create_folders():
    import os
    from emensageriapro.settings import BASE_DIR

    services = [
        'RecepcaoLoteReinf',
        'ConsultasReinf',
        'WsEnviarLoteEventos',
        'WsConsultarLoteEventos',
    ]

    for service in services:
        lista_pastas = [
            '%s/arquivos/Comunicacao/%s/header/' % (BASE_DIR, service),
            '%s/arquivos/Comunicacao/%s/request/' % (BASE_DIR, service),
            '%s/arquivos/Comunicacao/%s/response/' % (BASE_DIR, service),
        ]

        for pasta in lista_pastas:
            if not os.path.exists(pasta):
                os.system('mkdir -p %s' % pasta)


def create_insert(tabela, dados):

    from emensageriapro.get_username import get_username
    req = get_username()
    user_id = req.user.id

    variaveis = dados.keys()
    campos_numericos = executar_sql("""
        SELECT column_name FROM information_schema.columns
        WHERE table_name ='%s'
        AND data_type in ('numeric', 'integer');
        """ % tabela, True)
    campos_numericos_lista = []
    for a in campos_numericos:
        campos_numericos_lista.append(a[0])
    valores = ''
    for a in variaveis:
        if dados[a] or dados[a] == 0 or dados[a] == '':
            if (a in campos_numericos_lista):
                valores += "%s, " % str(dados[a]).replace('.','').replace(',','.')
            else:
                valores += "'%s', " % dados[a]
        else:
            valores += "Null, "
    texto = "INSERT INTO public.%s (%s, criado_em, criado_por_id, ativo) VALUES (%s now(), %s, True) RETURNING id;" % (tabela, ', '.join(variaveis), valores, user_id)
    return texto



def gravar_nome_arquivo(arquivo, permite_recuperacao):

    from datetime import datetime
    from emensageriapro.mensageiro.models import Arquivos

    from emensageriapro.get_username import get_username
    req = get_username()
    user_id = req.user.id

    dados = {}
    dados['arquivo'] = arquivo.replace('//', '/').replace('//', '/')
    dados['data_criacao'] = datetime.now()
    dados['permite_recuperacao'] = permite_recuperacao
    dados['criado_em'] = datetime.now()
    dados['ativo'] = True
    dados['criado_por_id'] = user_id

    obj = Arquivos(**dados)
    obj.save(using='default')



def salvar_arquivo_esocial(arquivo, texto, permite_recuperacao):

    import codecs
    from emensageriapro.settings import BASE_DIR

    arquivo1 = BASE_DIR + arquivo

    file = codecs.open(arquivo1, "w", "utf-8")
    try:
        file.write(texto)
    except:
        file.write(texto.decode())
    file.close()

    gravar_nome_arquivo(arquivo, permite_recuperacao)




def salvar_arquivo_efdreinf(arquivo, texto, permite_recuperacao):

    import codecs
    from emensageriapro.settings import BASE_DIR

    arquivo1 = BASE_DIR + arquivo

    file = codecs.open(arquivo1, "w", "utf-8")
    try:
        file.write(texto)
    except:
        file.write(texto.decode())
    file.close()

    gravar_nome_arquivo(arquivo, permite_recuperacao)


def ler_arquivo(arquivo):

    import codecs
    from emensageriapro.settings import BASE_DIR

    arquivo = BASE_DIR + arquivo

    file = codecs.open(arquivo, "r", "utf-8")
    texto = file.read()
    file.close()

    return texto.encode('utf-8')


def create_pem_files(cert_host, cert_pass, cert_pem_file, key_pem_file):

    import os.path
    from emensageriapro.padrao import salvar_arquivo
    from OpenSSL import crypto

    pkcs12 = crypto.load_pkcs12(open(cert_host, 'rb').read(), cert_pass)

    if not os.path.isfile(cert_pem_file):

        cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
        salvar_arquivo(cert_pem_file, cert_str)

    if not os.path.isfile(key_pem_file):

        key_str = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
        salvar_arquivo(key_pem_file, key_str)


def get_identidade_evento(xml):

    xml = xml.replace('Id="', 'id="')
    a = xml.split('id="')
    b = a[1].split('"')

    return b[0]



def get_transmissor_name(transmissor_id):
    number = str(transmissor_id)
    while len(number) < 9:
        number = '0'+number
    return number




def send(dados):
    import os
    command = '''curl --connect-timeout %(timeout)s --insecure 
                    --cert %(cert)s 
                    --key %(key)s 
                    --cacert %(cacert)s 
                    -H "Content-Type: text/xml;charset=UTF-8" 
                    -H "SOAPAction:%(action)s" 
                    --dump-header %(header_completo)s 
                    --output %(response_completo)s 
                    -d@%(request_completo)s 
                    %(url)s''' % dados

    os.system(command.replace('\n', ''))

