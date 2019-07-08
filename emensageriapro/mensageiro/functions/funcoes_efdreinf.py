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

import datetime

from constance import config
from django.contrib import messages

from emensageriapro.esocial.models import STATUS_EVENTO_AGUARD_ENVIO
from emensageriapro.mensageiro.functions.funcoes import TRANSMISSOR_STATUS_CADASTRADO, \
     TRANSMISSOR_STATUS_ENVIADO, TRANSMISSOR_STATUS_ENVIADO_ERRO, \
     TRANSMISSOR_STATUS_CONSULTADO, TRANSMISSOR_STATUS_CONSULTADO_ERRO

from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import definir_status_evento
from emensageriapro.mensageiro.models import *
from emensageriapro.mensageiro.functions.funcoes import send

REQUEST_RECEBER_LOTE_EVENTOS_EFDREINF = u"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sped="http://sped.fazenda.gov.br/">
   <soapenv:Header/>
   <soapenv:Body>
      <sped:ReceberLoteEventos>
         <!--Optional:-->
         <sped:loteEventos>
            <Reinf xmlns="http://www.reinf.esocial.gov.br/schemas/envioLoteEventos/v1_04_00">
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

REQUEST_CONSULTA_INFORMACOES_CONSOLIDADES_EFDREINF = u"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sped="http://sped.fazenda.gov.br/">
   <soapenv:Header/>
   <soapenv:Body>
      <sped:ConsultaInformacoesConsolidadas>
         <sped:tipoInscricaoContribuinte>%(contribuinte_tpinsc)s</sped:tipoInscricaoContribuinte>
         <sped:numeroInscricaoContribuinte>%(contribuinte_nrinsc)s</sped:numeroInscricaoContribuinte>
         <sped:numeroProtocoloFechamento>%(numero_protocolo_fechamento)s</sped:numeroProtocoloFechamento>
      </sped:ConsultaInformacoesConsolidadas>
   </soapenv:Body>
</soapenv:Envelope>"""




def assinar_efdreinf(request, xml, transmissor_id):

    from lxml import etree
    from emensageriapro.settings import BASE_DIR
    from signxml import XMLSigner, methods
    from emensageriapro.mensageiro.functions.funcoes import get_identidade_evento, create_pem_files, ler_arquivo

    if transmissor_id:

        tra = TransmissorLoteEfdreinf.objects. \
            get(id=transmissor_id)

        if tra.transmissor:

            if tra.transmissor.certificado:

                cert_host = '%s/certificado/%s' % (BASE_DIR, tra.transmissor.certificado.certificado)
                cert_pass = tra.transmissor.certificado.senha
                cert_pem_file = '/certificado/cert_%s.pem' % tra.transmissor.certificado.id
                key_pem_file = '/certificado/key_%s.pem' % tra.transmissor.certificado.id

                create_pem_files(cert_host, cert_pass, cert_pem_file, key_pem_file)

                cert_str = ler_arquivo(cert_pem_file)
                key_str = ler_arquivo(key_pem_file)
                root = etree.fromstring(xml)
                identidade = get_identidade_evento(xml)

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

            else:

                messages.error(request,
                               '''O certificado não está configurado,
                                  configure pelo menos um transmissor para o respectivo empregador!''')

        else:

            messages.error(request,
                           '''O transmissor não está configurado!''')

    return xml






def create_request(dados):

    from emensageriapro.mensageiro.functions.funcoes import ler_arquivo, salvar_arquivo_efdreinf

    if dados['service'] == 'RecepcaoLoteReinf':

        xml_temp = ''
        eventos = TransmissorEventosEfdreinf.objects. \
            filter(transmissor_lote_efdreinf_id=dados['transmissor_id'],
                   status=STATUS_EVENTO_AGUARD_ENVIO).all()

        for e in eventos:
            dados_evento =  e.__dict__
            xml_temp += '<evento id="%(identidade)s">' % dados_evento
            xml_temp += ler_arquivo('/arquivos/Eventos/%(tabela)s/%(identidade)s.xml' % dados_evento)
            xml_temp += '</evento>'

        text = REQUEST_RECEBER_LOTE_EVENTOS_EFDREINF.replace('<!--You may enter ANY elements at this point-->', xml_temp)

    elif dados['service'] == 'ConsultasReinf':
        a = TransmissorLoteEfdreinf.objects. \
            get(id=dados['transmissor_id'])

        text = REQUEST_CONSULTA_INFORMACOES_CONSOLIDADES_EFDREINF % a.__dict__

    salvar_arquivo_efdreinf(dados['request'], text, 0)



def send_xml(request, transmissor_id, service):

    import os
    from datetime import datetime
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import ler_arquivo, \
        get_transmissor_name, create_pem_files, send, gravar_nome_arquivo, create_folders

    CA_CERT_PEM_FILE = config.EFDREINF_CA_CERT_PEM_FILE
    TP_AMB = config.EFDREINF_TP_AMB

    create_folders()

    data_atual = str(datetime.now()).replace(':', '-').replace(' ', '-').replace('.', '-')

    if TP_AMB == '1':  # Produção

        if service == 'RecepcaoLoteReinf':

            URL = "https://reinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos"

        elif service == 'ConsultasReinf':

            URL = "https://reinf.receita.fazenda.gov.br/WsReinfConsultas/ConsultasReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/ConsultasReinf/ConsultaInformacoesConsolidadas"

    elif TP_AMB == '2':  # Produção-Restrita

        if service == 'RecepcaoLoteReinf':

            URL = "https://preprodefdreinf.receita.fazenda.gov.br/wsreinf/RecepcaoLoteReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos"

        elif service == 'ConsultasReinf':

            URL = "https://preprodefdreinf.receita.fazenda.gov.br/WsReinfConsultas/ConsultasReinf.svc"
            ACTION = "http://sped.fazenda.gov.br/ConsultasReinf/ConsultaInformacoesConsolidadas"

    tra = TransmissorLoteEfdreinf.objects.\
            get(id=transmissor_id)

    if tra.transmissor:

        if tra.transmissor.certificado:

            cert_host = '%s/certificado/%s' % (BASE_DIR, tra.transmissor.certificado.certificado)
            cert_pass = tra.transmissor.certificado.senha
            cert_pem_file = '/certificado/cert_%s.pem' % tra.transmissor.certificado.id
            key_pem_file = '/certificado/key_%s.pem' % tra.transmissor.certificado.id

            create_pem_files(cert_host, cert_pass,
                             cert_pem_file, key_pem_file)

        else:

            messages.error(request, 'O certificado não está configurado ou não possuem eventos validados para envio neste lote!')

            return None

    else:

        messages.error(request,
                       'O Transmissor não está configurado!')
        return None


    dados = {}
    dados['contribuinte_tpinsc'] = tra.contribuinte_tpinsc
    dados['contribuinte_nrinsc'] = tra.contribuinte_nrinsc
    dados['transmissor_id'] = transmissor_id
    dados['efdreinf_lote_min'] = config.EFDREINF_LOTE_MIN
    dados['efdreinf_lote_max'] = config.EFDREINF_LOTE_MIN
    dados['efdreinf_timeout'] = int(config.EFDREINF_TIMEOUT)

    name = get_transmissor_name(transmissor_id)

    dados['transmissor_id'] = transmissor_id
    dados['header'] = '/arquivos/Comunicacao/%s/header/%s_%s.xml' % (service, name, data_atual)
    dados['request'] = '/arquivos/Comunicacao/%s/request/%s_%s.xml' % (service, name, data_atual)
    dados['response'] = '/arquivos/Comunicacao/%s/response/%s_%s.xml' % (service, name, data_atual)
    dados['header_completo'] = '%s/arquivos/Comunicacao/%s/header/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['request_completo'] = '%s/arquivos/Comunicacao/%s/request/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['response_completo'] = '%s/arquivos/Comunicacao/%s/response/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['service'] = service
    dados['url'] = URL
    dados['cert'] = BASE_DIR + cert_pem_file
    dados['cacert'] = BASE_DIR + CA_CERT_PEM_FILE
    dados['key'] = BASE_DIR + key_pem_file
    dados['action'] = ACTION
    dados['timeout'] = dados['efdreinf_timeout']

    quant_eventos = TransmissorEventosEfdreinf.objects. \
        filter(transmissor_lote_efdreinf_id=transmissor_id,
               status=STATUS_EVENTO_AGUARD_ENVIO).count()

    if tra.transmissor.certificado and (quant_eventos or service == 'ConsultasReinf'):

        if (quant_eventos >= dados['efdreinf_lote_min'] and \
                quant_eventos <= dados['efdreinf_lote_max'] and \
                service == 'RecepcaoLoteReinf') or service == 'ConsultasReinf':

            create_request(dados)
            send(dados)
            gravar_nome_arquivo(dados['header'], 0)
            gravar_nome_arquivo(dados['request'], 0)
            gravar_nome_arquivo(dados['response'], 0)

            if not os.path.isfile(BASE_DIR + dados['response']):

                messages.error(request, '''O servidor demorou mais que o esperado 
                    para efetuar a conexão! Caso necessário solicite ao 
                    administrador do sistema para que aumente o tempo do 
                    Timeout. Timeout atual %(timeout)s''' % dados)

                return None

            elif 'HTTP/1.1 200 OK' not in ler_arquivo(dados['header']):

                messages.warning(request, 'Retorno do servidor: ' + ler_arquivo(dados['header']))

            elif service == 'RecepcaoLoteReinf':

                from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import read_envioLoteEventos, definir_status_evento

                read_envioLoteEventos(request, dados['response'], transmissor_id)
                messages.success(request, 'Lote enviado com sucesso!')

                TransmissorLoteEfdreinf.objects.\
                    filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_ENVIADO)
                definir_status_evento(transmissor_id)

            elif service == 'ConsultasReinf':

                from emensageriapro.mensageiro.functions.funcoes_efdreinf_comunicacao import read_consultaLoteEventos, definir_status_evento

                read_consultaLoteEventos(request, dados['response'], transmissor_id)
                messages.success(request, 'Lote consultado com sucesso!')

                TransmissorLoteEfdreinf.objects.\
                    filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_CONSULTADO)
                definir_status_evento(transmissor_id)

        elif quant_eventos < dados['efdreinf_lote_min'] and service == 'RecepcaoLoteReinf':

            messages.error(request, 'Lote com quantidade inferior a mínima permitida!')
            
            TransmissorLoteEfdreinf.objects.\
                filter(id=transmissor_id).\
                update(status=TRANSMISSOR_STATUS_CADASTRADO)

        elif quant_eventos > dados['efdreinf_lote_max'] and service == 'RecepcaoLoteReinf':

            messages.error(request, 'Lote com quantidade de eventos superior a máxima permitida!')
            
            TransmissorLoteEfdreinf.objects.\
                filter(id=transmissor_id).\
                update(status=TRANSMISSOR_STATUS_CADASTRADO)

        else:
            
            messages.error(request, 'Erro ao enviar o lote!')
            
            if service == 'RecepcaoLoteReinf':
                
                TransmissorLoteEfdreinf.objects.\
                    filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_ENVIADO_ERRO)

            elif service == 'ConsultasReinf':
                
                TransmissorLoteEfdreinf.objects.\
                    filter(id=transmissor_id).\
                    update(status=TRANSMISSOR_STATUS_CONSULTADO_ERRO)


    else:

        messages.error(request, 'O certificado não está configurado ou não possuem eventos validados para envio neste lote!')





