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
#from emensageriapro.settings import BASE_DIR
from emensageriapro.mensageiro.functions.funcoes_status import atualizar_status_efdreinf
from emensageriapro.mensageiro.models import *


REQUEST_RECEBER_LOTE_EVENTOS_EFDREINF = u"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sped="http://sped.fazenda.gov.br/">
   <soapenv:Header/>
   <soapenv:Body>
      <sped:ReceberLoteEventos>
         <!--Optional:-->
         <sped:loteEventos>
         <Reinf xmlns="http://www.reinf.esocial.gov.br/schemas/envioLoteEventos/v1_03_02">
              <loteEventos>
                  <!--You may enter ANY elements at this point-->
              </loteEventos>
            </Reinf>
         </sped:loteEventos>
      </sped:ReceberLoteEventos>
   </soapenv:Body>
</soapenv:Envelope>
"""

CABECALHO_EVENTO = u"""<evento id="%(identidade_evento)s"><!--evento--></evento>"""

REQUEST_CONSULTA_INFORMACOES_CONSOLIDADES_EFDREINF = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sped="http://sped.fazenda.gov.br/"><soapenv:Header/><soapenv:Body><sped:ConsultaInformacoesConsolidadas><sped:tipoInscricaoContribuinte>%(contribuinte_tpinsc)s</sped:tipoInscricaoContribuinte><!--Optional:--><sped:numeroInscricaoContribuinte>%(contribuinte_nrinsc)s</sped:numeroInscricaoContribuinte><!--Optional:--><sped:numeroProtocoloFechamento>%(numero_protocolo_fechamento)s</sped:numeroProtocoloFechamento></sped:ConsultaInformacoesConsolidadas></soapenv:Body></soapenv:Envelope>"""


#https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc?singleWSDL

#https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/ConsultasReinf.svc?singleWSDL



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


def salvar_arquivo_efdreinf(arquivo, texto, permite_recuperacao):
    from emensageriapro.settings import BASE_DIR
    arquivo1 = BASE_DIR+'/'+arquivo
    arquivo1 = arquivo1.replace('//', '/').replace('//', '/')
    try:
        file = open(arquivo1, "w")
        file.write( texto )
        file.close()
    except:
        import codecs
        file = codecs.open(arquivo1, "w", "utf-8")
        file.write(texto)
        file.close()
    gravar_nome_arquivo(arquivo, permite_recuperacao)


def ler_arquivo(arquivo):
    from emensageriapro.settings import BASE_DIR
    arquivo = BASE_DIR+'/'+arquivo
    file = open(arquivo, 'r')
    texto = file.read()
    file.close()
    return texto


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


def get_identidade_evento(xml):
    a = xml.split('id="')
    b = a[1].split('"')
    return b[0]


def assinar_efdreinf(xml):
    from lxml import etree
    from emensageriapro.settings import FORCE_PRODUCAO_RESTRITA, BASE_DIR
    from signxml import XMLSigner, methods
    from emensageriapro.settings import CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE

    cert_host = BASE_DIR + '/' + CERT_HOST
    cert_pem_file = CERT_PEM_FILE
    key_pem_file = KEY_PEM_FILE


    if FORCE_PRODUCAO_RESTRITA:
        xml = xml.replace('<tpAmb>1</tpAmb>','<tpAmb>2</tpAmb>')

    identidade = get_identidade_evento(xml)

    create_pem_files(cert_host, CERT_PASS, cert_pem_file, key_pem_file)

    cert_str = ler_arquivo(cert_pem_file)
    key_str = ler_arquivo(key_pem_file)
    root = etree.fromstring(xml)

    signed_root = XMLSigner(
        method=methods.enveloped,
        signature_algorithm=u'rsa-sha256',
        digest_algorithm=u'sha256',
        c14n_algorithm=u'http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
        ).sign(root,
               reference_uri='#' + identidade,
               key=key_str,
               cert=cert_str)

    return etree.tostring(signed_root)






def get_transmissor_name(transmissor_id):
    number = str(transmissor_id)
    while len(number) < 9:
        number = '0'+number
    return number




def create_request(dados):

    if dados['service'] == 'RecepcaoLoteReinf':

        xml_temp = ''

        eventos = TransmissorEventosEfdreinf.objects.using('default'). \
            filter(transmissor_lote_efdreinf_id=dados['transmissor_id'],
                   status=4, validacao_precedencia=1).all()

        # eventos = executar_sql("""
        #   SELECT evento, id, identidade, tabela
        #     FROM public.transmissor_eventos_efdreinf
        #    WHERE transmissor_lote_efdreinf_id = %(transmissor_id)s
        #      AND status=4 AND validacao_precedencia=1
        #    ORDER BY identidade;""" % dados, True)

        for e in eventos:

            dados =  e.__dict__

            xml_temp += '<evento id="%(identidade)s">' % dados
            xml_temp += ler_arquivo('/arquivos/Eventos/%(tabela)s/%(identidade)s.xml' % dados)
            xml_temp += '</evento>'

        text = REQUEST_RECEBER_LOTE_EVENTOS_EFDREINF.replace('<!--You may enter ANY elements at this point-->', xml_temp)

    elif dados['service'] == 'ConsultasReinf':

        a = TransmissorLoteEfdreinf.objects.using('default'). \
            get(id=dados['transmissor_id'])

        # a = executar_sql("""
        #   SELECT contribuinte_tpinsc, contribuinte_nrinsc, numero_protocolo_fechamento
        #     FROM public.transmissor_lote_efdreinf
        #    WHERE id= %(transmissor_id)s;""" % dados, True)
        # dados['contribuinte_tpinsc'] = a.[0][0]
        # dados['contribuinte_nrinsc'] = a[0][1]
        # dados['numero_protocolo_fechamento'] = a[0][2]

        text = REQUEST_CONSULTA_INFORMACOES_CONSOLIDADES_EFDREINF % a.__dict__

    salvar_arquivo_efdreinf(dados['request'], text, 0)



#https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc?singleWSDL
#https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/ConsultasReinf.svc?singleWSDL


def send_xml(request, transmissor_id, service):
    from emensageriapro.settings import BASE_DIR
    from datetime import datetime
    data_atual = str(datetime.now()).replace(':','-').replace(' ','-').replace('.','-')

    from datetime import datetime
    import os
    from emensageriapro.settings import CERT_PEM_FILE, KEY_PEM_FILE, CA_CERT_PEM_FILE, FORCE_PRODUCAO_RESTRITA, TP_AMB, CERT_HOST, CERT_PASS

    CERT_HOST = BASE_DIR + '/' + CERT_HOST
    if TP_AMB == '1': # Produção
        if service == 'RecepcaoLoteReinf':
            URL = "https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos"
        elif service == 'ConsultasReinf':
            URL = "https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/ConsultasReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/ConsultasReinf/ConsultaInformacoesConsolidadas"
    elif TP_AMB == '2': # Produção-Restrita
        if service == 'RecepcaoLoteReinf':
            URL = "https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos"
        elif service == 'ConsultasReinf':
            URL = "https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/ConsultasReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/ConsultasReinf/ConsultaInformacoesConsolidadas"
    dados = {}
    name = get_transmissor_name(transmissor_id)

    tra = TransmissorLoteEfdreinf.objects.using('default'). \
            get(id=transmissor_id).all()

    # tra = executar_sql("""
    #     SELECT te.contribuinte_tpinsc, te.contribuinte_nrinsc,
    #                t.transmissor_tpinsc, t.transmissor_nrinsc,
    #                t.efdreinf_lote_min, t.efdreinf_lote_max,
    #                t.efdreinf_timeout, t.efdreinf_certificado, t.efdreinf_senha
    #           FROM public.transmissor_lote_efdreinf te
    #           JOIN public.transmissores t ON t.id = te.transmissor_id
    #          WHERE te.id=%s;
    # """ % transmissor_id, True)

    dados['contribuinte_tpinsc'] = tra.contribuinte_tpinsc
    dados['contribuinte_nrinsc'] = tra.contribuinte_nrinsc
    dados['transmissor_id'] = transmissor_id
    dados['efdreinf_lote_min'] = tra.transmissor.efdreinf_lote_min
    dados['efdreinf_lote_max'] = tra.transmissor.efdreinf_lote_max
    dados['efdreinf_timeout'] = int(tra.transmissor.efdreinf_timeout)
    # dados['efdreinf_certificado'] = 'uploads/'+tra.transmissor.efdreinf_certificado
    # dados['efdreinf_senha'] = tra.transmissor.efdreinf_senha

    cert_pem_file = BASE_DIR+'/'+ CERT_PEM_FILE
    key_pem_file = BASE_DIR+'/'+ KEY_PEM_FILE

    if not os.path.isfile(cert_pem_file):
        create_pem_files(CERT_HOST, CERT_PASS,
                         cert_pem_file, key_pem_file)

    dados['transmissor_id'] = transmissor_id
    dados['header'] = 'arquivos/Comunicacao/%s/header/%s_%s.xml' % (service, name, data_atual)
    dados['request'] = 'arquivos/Comunicacao/%s/request/%s_%s.xml' % (service, name, data_atual)
    dados['response'] = 'arquivos/Comunicacao/%s/response/%s_%s.xml' % (service, name, data_atual)
    dados['header_completo'] = '%s/arquivos/Comunicacao/%s/header/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['request_completo'] = '%s/arquivos/Comunicacao/%s/request/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['response_completo'] = '%s/arquivos/Comunicacao/%s/response/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['service'] = service
    dados['url'] = URL
    dados['cert'] = cert_pem_file
    dados['cacert'] = '%s/%s' % (BASE_DIR, CA_CERT_PEM_FILE)
    dados['key'] = KEY_PEM_FILE
    dados['action'] = ACTION
    dados['timeout'] = dados['efdreinf_timeout']

    # qt_ev_validados = executar_sql("""
    #     SELECT count(*) FROM transmissor_eventos_efdreinf
    #      WHERE transmissor_lote_efdreinf_id=%s AND status=4""" % transmissor_id, True)
    # quant_eventos_validados = qt_ev_validados[0][0]

    quant_eventos_validados = TransmissorEventosEfdreinf.objects.using('default'). \
        filter(transmissor_lote_efdreinf_id=transmissor_id,
               status=4).count()

    if quant_eventos_validados or service == 'ConsultasReinf':

        quant_eventos = TransmissorEventosEfdreinf.objects.using('default'). \
            filter(transmissor_lote_efdreinf_id=transmissor_id).count()

        # qt_ev = executar_sql("""
        # SELECT count(*) FROM transmissor_eventos_efdreinf
        #  WHERE transmissor_lote_efdreinf_id=%s""" % transmissor_id, True)
        # quant_eventos = qt_ev[0][0]

        if (quant_eventos >= dados['efdreinf_lote_min'] and \
                quant_eventos <= dados['efdreinf_lote_max'] and \
                service == 'RecepcaoLoteReinf') or service == 'ConsultasReinf':

            create_request(dados)

            command = '''curl --connect-timeout %(timeout)s
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
                return None

            if service == 'RecepcaoLoteReinf':
                from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import read_envioLoteEventos
                read_envioLoteEventos(dados['response'], transmissor_id)
                messages.success(request, 'Lote enviado com sucesso!')

            elif service == 'ConsultasReinf':
                from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import read_consultaLoteEventos
                read_consultaLoteEventos(dados['response'], transmissor_id)
                messages.success(request, 'Lote consultado com sucesso!')

            gravar_nome_arquivo(dados['header'], 0)
            gravar_nome_arquivo(dados['request'], 0)
            gravar_nome_arquivo(dados['response'], 0)

            if 'HTTP/1.1 200 OK' not in ler_arquivo(dados['header']):
                messages.warning(request, 'Retorno do servidor: ' + ler_arquivo(dados['header']) )

            if service == 'RecepcaoLoteReinf':
                TransmissorEventosEfdreinf.objects.using('default').filter(id=transmissor_id).update(status=7)
                #alterar_status_transmissor(transmissor_id, 7)

            elif service == 'ConsultasReinf':
                TransmissorEventosEfdreinf.objects.using('default').filter(id=transmissor_id).update(status=9)
                #alterar_status_transmissor(transmissor_id, 9)

        elif (quant_eventos < dados['efdreinf_lote_min'] and \
                    service == 'RecepcaoLoteReinf'):
            messages.error(request, 'Lote com quantidade inferior a mínima permitida!')
            TransmissorEventosEfdreinf.objects.using('default').filter(id=transmissor_id).update(status=0)
            #alterar_status_transmissor(transmissor_id, 0)

        elif (quant_eventos > dados['efdreinf_lote_max'] and \
                  service == 'RecepcaoLoteReinf'):
            messages.error(request, 'Lote com quantidade de eventos superior a máxima permitida!')
            TransmissorEventosEfdreinf.objects.using('default').filter(id=transmissor_id).update(status=0)
            #alterar_status_transmissor(transmissor_id, 0)

        else:
            messages.error(request, 'Erro ao enviar o lote!')
            if service == 'RecepcaoLoteReinf':
                TransmissorEventosEfdreinf.objects.using('default').filter(id=transmissor_id).update(status=5)
                #alterar_status_transmissor(transmissor_id, 5)

            elif service == 'ConsultasReinf':
                TransmissorEventosEfdreinf.objects.using('default').filter(id=transmissor_id).update(status=8)
                #alterar_status_transmissor(transmissor_id, 8)

    else:
        messages.error(request, 'Não possuem eventos validados para envio neste lote!')

    atualizar_status_efdreinf()




