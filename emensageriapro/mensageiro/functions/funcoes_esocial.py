#coding:utf-8

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

import psycopg2
import datetime
import os
from django.contrib import messages
from emensageriapro.settings import BASE_DIR
#from emensageriapro.mensageiro.functions.funcoes_status import atualizar_status_esocial
from emensageriapro.mensageiro.models import *

from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


TRANSMISSOR_STATUS_CADASTRADO = 0
TRANSMISSOR_STATUS_ENVIADO = 1
TRANSMISSOR_STATUS_ENVIADO_ERRO = 2
TRANSMISSOR_STATUS_CONSULTADO = 3
TRANSMISSOR_STATUS_CONSULTADO_ERRO = 4



REQUEST_ENVIA_LOTE = u"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:v1="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0">
    <soapenv:Header/>
    <soapenv:Body>
        <v1:EnviarLoteEventos><!--Optional:-->
            <v1:loteEventos>
                <eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/v1_1_1">
                    <envioLoteEventos grupo="%(grupo)s">
                        <ideEmpregador>
                            <tpInsc>%(empregador_tpinsc)s</tpInsc>
                            <nrInsc>%(empregador_nrinsc)s</nrInsc>
                        </ideEmpregador>
                        <ideTransmissor>
                            <tpInsc>%(transmissor_tpinsc)s</tpInsc>
                            <nrInsc>%(transmissor_nrinsc)s</nrInsc>
                        </ideTransmissor>
                        <eventos><!--You may enter ANY elements at this point--></eventos>
                    </envioLoteEventos>
                </eSocial>
            </v1:loteEventos>
        </v1:EnviarLoteEventos>
    </soapenv:Body>
</soapenv:Envelope>

"""

REQUEST_CONSULTA_LOTE = u"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:v1="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0">
    <soapenv:Header/>
    <soapenv:Body>
        <v1:ConsultarLoteEventos><!--Optional:-->
            <v1:consulta><!--You may enter ANY elements at this point--></v1:consulta>
        </v1:ConsultarLoteEventos>
    </soapenv:Body>
</soapenv:Envelope>
"""

BASE_XML_CONSULTA_LOTE = u"""
<eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoProcessamento/v1_0_0"
         xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <consultaLoteEventos>
        <protocoloEnvio>%s</protocoloEnvio>
    </consultaLoteEventos>
</eSocial>
"""



def gravar_nome_arquivo(arquivo, permite_recuperacao):

    dados = {}
    dados['arquivo'] = arquivo.replace('//', '/').replace('//', '/')
    dados['data_criacao'] = datetime.datetime.now()
    dados['permite_recuperacao'] = permite_recuperacao
    dados['criado_em'] = datetime.datetime.now()
    dados['excluido'] = False
    dados['criado_por_id'] = 1

    obj = Arquivos(**dados)
    obj.save(using='default')


def salvar_arquivo_esocial(arquivo, texto, permite_recuperacao):
    from emensageriapro.settings import BASE_DIR
    arquivo1 = BASE_DIR+'/'+arquivo
    arquivo1 = arquivo1.replace('//', '/').replace('//', '/')
    # try:
    #     file = open(arquivo1, "w")
    #     file.write( texto )
    #     file.close()
    # except:
    import codecs
    file = codecs.open(arquivo1, "w", "utf-8")
    file.write(texto)
    file.close()
    gravar_nome_arquivo(arquivo, permite_recuperacao)



# def ler_arquivo(arquivo):
#     from emensageriapro.settings import BASE_DIR
#     arquivo = BASE_DIR+'/'+arquivo
#     file = open(arquivo, 'r')
#     texto = file.read()
#     file.close()
#     return texto


def ler_arquivo(arquivo):
    from emensageriapro.settings import BASE_DIR
    arquivo = BASE_DIR+'/'+arquivo
    import codecs
    file = codecs.open(arquivo, "r", "utf-8")
    texto = file.read()
    file.close()
    return texto.encode('utf-8')


def create_pem_files(CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE):
    import os.path
    from emensageriapro.padrao import salvar_arquivo
    from OpenSSL import crypto

    pkcs12 = crypto.load_pkcs12(open(CERT_HOST, 'rb').read(), CERT_PASS)

    if not os.path.isfile(CERT_PEM_FILE):
        cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
        salvar_arquivo(CERT_PEM_FILE, cert_str)

    if not os.path.isfile(KEY_PEM_FILE):
        key_str = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
        salvar_arquivo(KEY_PEM_FILE, key_str)




def assinar_esocial(xml):
    from lxml import etree
    from signxml import XMLSigner, methods
    from emensageriapro.settings import CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE
    from emensageriapro.settings import FORCE_PRODUCAO_RESTRITA, BASE_DIR

    cert_host = BASE_DIR + '/' + CERT_HOST
    cert_pem_file = CERT_PEM_FILE
    key_pem_file = KEY_PEM_FILE

    if FORCE_PRODUCAO_RESTRITA:
        xml = xml.replace('<tpAmb>1</tpAmb>','<tpAmb>2</tpAmb>')

    if CERT_HOST:

        create_pem_files(cert_host, CERT_PASS, cert_pem_file, key_pem_file)
        cert_str = ler_arquivo(cert_pem_file)
        key_str = ler_arquivo(key_pem_file)
        root = etree.fromstring(xml)

        signed_root = XMLSigner(
            method=methods.enveloped,
            signature_algorithm='rsa-sha256',
            digest_algorithm='sha256',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315').\
                sign(root, key=key_str, cert=cert_str)

        return etree.tostring(signed_root)

    else:

        return xml


def get_transmissor_name(transmissor_id):
    number = str(transmissor_id)

    while len(number) < 9:
        number = '0'+number

    return number



def create_request(dados, transmissor_dados):

    if dados['service'] == 'WsEnviarLoteEventos':

        xml = u''

        eventos = TransmissorEventosEsocial.objects.using('default').\
            filter(transmissor_lote_esocial_id=dados['transmissor_id'],
                   status=STATUS_EVENTO_AGUARD_ENVIO).all()

        dados_evento = {}
        for e in eventos:

            dados_evento['evento'] = e.evento
            dados_evento['id'] = e.id
            dados_evento['identidade'] = e.identidade
            dados_evento['grupo'] = e.grupo
            dados_evento['tabela'] = e.tabela
            dados_evento['empregador_tpinsc'] = e.transmissor_lote_esocial.empregador_tpinsc
            dados_evento['empregador_nrinsc'] = e.transmissor_lote_esocial.empregador_nrinsc
            dados_evento['transmissor_tpinsc'] = e.transmissor_lote_esocial.transmissor.transmissor_tpinsc
            dados_evento['transmissor_nrinsc'] = e.transmissor_lote_esocial.transmissor.transmissor_nrinsc

            xml += '<evento Id="%s">' % e.identidade
            xml += ler_arquivo('/arquivos/Eventos/%(tabela)s/%(identidade)s.xml' % dados_evento)
            xml += '</evento>'

        base_request = REQUEST_ENVIA_LOTE % dados_evento

    elif dados['service'] == 'WsConsultarLoteEventos':

        a = TransmissorLoteEsocial.objects.using('default').\
                get(id=dados['transmissor_id'])

        xml = BASE_XML_CONSULTA_LOTE % a.protocolo
        base_request = REQUEST_CONSULTA_LOTE % transmissor_dados

    text = base_request.replace('<!--You may enter ANY elements at this point-->', xml)
    salvar_arquivo_esocial(dados['request'], text, 0)





def send_xml(request, transmissor_id, service):
    from emensageriapro.settings import BASE_DIR
    from datetime import datetime
    data_atual = str(datetime.now()).replace(':','-').replace(' ','-').replace('.','-')

    import os
    from emensageriapro.settings import FORCE_PRODUCAO_RESTRITA, \
        TP_AMB, CA_CERT_PEM_FILE, CERT_HOST, CERT_PASS, \
        CERT_PEM_FILE, KEY_PEM_FILE

    CERT_HOST = BASE_DIR + '/' + CERT_HOST

    if TP_AMB == '1': # Produção
        if service == 'WsEnviarLoteEventos':
            URL_WS = "https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0/ServicoEnviarLoteEventos/EnviarLoteEventos"
        elif service == 'WsConsultarLoteEventos':
            URL_WS = "https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0/ServicoConsultarLoteEventos/ConsultarLoteEventos"

    elif TP_AMB == '2': # Produção-Restrita
        if service == 'WsEnviarLoteEventos':
            URL_WS = "https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0/ServicoEnviarLoteEventos/EnviarLoteEventos"
        elif service == 'WsConsultarLoteEventos':
            URL_WS = "https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc"
            ACTION = "http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0/ServicoConsultarLoteEventos/ConsultarLoteEventos"

    name = get_transmissor_name(transmissor_id)

    tle = TransmissorLoteEsocial.objects.using('default').\
                get(id=transmissor_id)

    transmissor_dados = {}
    transmissor_dados['empregador_tpinsc'] = tle.empregador_tpinsc
    transmissor_dados['empregador_nrinsc'] = tle.empregador_nrinsc
    transmissor_dados['transmissor_tpinsc'] = tle.transmissor.transmissor_tpinsc
    transmissor_dados['transmissor_nrinsc'] = tle.transmissor.transmissor_nrinsc
    transmissor_dados['esocial_lote_min'] = tle.transmissor.esocial_lote_min
    transmissor_dados['esocial_lote_max'] = tle.transmissor.esocial_lote_max
    transmissor_dados['esocial_timeout'] = int(tle.transmissor.esocial_timeout)

    cert_pem_file = BASE_DIR + '/' + CERT_PEM_FILE
    key_pem_file = BASE_DIR + '/' + KEY_PEM_FILE

    if not os.path.isfile(cert_pem_file) and CERT_HOST:
        create_pem_files(CERT_HOST, CERT_PASS, cert_pem_file, key_pem_file)

    dados = {}
    dados['transmissor_id'] = transmissor_id
    dados['header'] = 'arquivos/Comunicacao/%s/header/%s_%s.xml' % (service, name, data_atual)
    dados['request'] = 'arquivos/Comunicacao/%s/request/%s_%s.xml' % (service, name, data_atual)
    dados['response'] = 'arquivos/Comunicacao/%s/response/%s_%s.xml' % (service, name, data_atual)
    dados['header_completo'] = '%s/arquivos/Comunicacao/%s/header/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['request_completo'] = '%s/arquivos/Comunicacao/%s/request/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['response_completo'] = '%s/arquivos/Comunicacao/%s/response/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['service'] = service
    dados['url'] = URL_WS
    dados['cert'] = cert_pem_file
    dados['cacert'] = '%s/certificados/webservicesproducaorestritaesocialgovbr.crt' % BASE_DIR
    dados['key'] = key_pem_file
    dados['action'] = ACTION
    dados['timeout'] = transmissor_dados['esocial_timeout']

    quant_eventos =  TransmissorEventosEsocial.objects.using('default'). \
                                    filter(transmissor_lote_esocial_id=transmissor_id,
                                           status=STATUS_EVENTO_AGUARD_ENVIO).count()

    if CERT_HOST and (quant_eventos or service == 'WsConsultarLoteEventos'):

        if (quant_eventos >= transmissor_dados['esocial_lote_min'] and \
                quant_eventos <= transmissor_dados['esocial_lote_max'] and \
                service == 'WsEnviarLoteEventos') or service == 'WsConsultarLoteEventos':

            create_request(dados, transmissor_dados)

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

            command = command.replace('\n', '')
            for n in range(10):
                command = command.replace('  ', ' ')

            os.system(command)

            if not os.path.isfile(BASE_DIR + '/' + dados['response']):

                messages.error(request, '''O servidor demorou mais que o esperado 
                                            para efetuar a conexão! Caso necessário solicite ao 
                                            administrador do sistema para que aumente o tempo do 
                                            Timeout. Timeout atual %(timeout)s''' % dados)

                TransmissorLoteEsocial.objects.using('default').filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_ENVIADO_ERRO)
                return None

            if service == 'WsEnviarLoteEventos':

                from emensageriapro.mensageiro.functions.funcoes_esocial_comunicacao import read_envioLoteEventos, definir_status_evento
                read_envioLoteEventos(dados['response'], transmissor_id)
                definir_status_evento(transmissor_id)
                TransmissorLoteEsocial.objects.using('default').filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_ENVIADO)
                messages.success(request, 'Lote enviado com sucesso!')

            elif service == 'WsConsultarLoteEventos':

                from emensageriapro.mensageiro.functions.funcoes_esocial_comunicacao import read_consultaLoteEventos
                messages.success(request, 'Lote consultado com sucesso!')
                TransmissorLoteEsocial.objects.using('default').filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_CONSULTADO)
                read_consultaLoteEventos(dados['response'], transmissor_id)

            gravar_nome_arquivo(dados['header'], 0)
            gravar_nome_arquivo(dados['request'], 0)
            gravar_nome_arquivo(dados['response'], 0)

            if 'HTTP/1.1 200 OK' not in ler_arquivo(dados['header']):
                messages.warning(request, 'Retorno do servidor: ' + ler_arquivo(dados['header']) )


        elif (quant_eventos < transmissor_dados['esocial_lote_min'] and \
                    service == 'WsEnviarLoteEventos'):
            messages.error(request, 'Lote com quantidade inferior a mínima permitida!')

        elif (quant_eventos > transmissor_dados['esocial_lote_max'] and \
                  service == 'WsEnviarLoteEventos'):
            messages.error(request, 'Lote com quantidade de eventos superior a máxima permitida!')

        else:

            if service == 'WsEnviarLoteEventos':
                TransmissorLoteEsocial.objects.using('default').filter(id=transmissor_id).update(status=TRANSMISSOR_STATUS_ENVIADO_ERRO)
                messages.error(request, 'Erro ao enviar o lote!')

            elif service == 'WsConsultarLoteEventos':
                TransmissorLoteEsocial.objects.using('default').filter(id=transmissor_id).update(status=TRANSMISSOR_STATUS_CONSULTADO_ERRO)
                messages.error(request, 'Erro ao consultar o lote!')

    else:

        messages.error(request, 'O certificado não está configurado ou não possuem eventos validados para envio neste lote!')





