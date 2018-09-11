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
from emensageriapro.funcoes_status import atualizar_status_esocial

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

def criar_diretorio_arquivos():
    lista = [
        'arquivos/Comunicacao/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/header/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/request/',
        'arquivos/Comunicacao/WsConsultarLoteEventos/response/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/header/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/request/',
        'arquivos/Comunicacao/WsEnviarLoteEventos/response/',
    ]
    for a in lista:
        if not os.path.isdir(a):
            os.system('mkdir -p %s/%s' % (BASE_DIR,a ) )

def executar_sql(select, array):
    from emensageriapro.settings import DATABASES
    database = DATABASES['default']
    try:
        conn = psycopg2.connect("user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s' dbname='%(NAME)s'" % database)
        conn.autocommit = True
    except:
        print "I am unable to connect to the database"
    if select:
        cur = conn.cursor()
        select = select.replace("'Null'", 'Null')
        cur.execute(select)
        if array: lista = cur.fetchall()
        else: lista = None
        cur.close()
        return lista
    else:
        return None


def alterar_status_transmissor(transmissor_id, status):
    if status == 7:
        executar_sql("""
            UPDATE public.transmissor_lote_esocial 
            SET status=%s, resposta_codigo=Null, resposta_descricao=Null
            WHERE id=%s;""" % (status, transmissor_id), False)
    else:
        executar_sql("""
            UPDATE public.transmissor_lote_esocial 
            SET status=%s 
            WHERE id=%s;""" % (status, transmissor_id), False)


def gravar_nome_arquivo(arquivo, permite_recuperacao):
    #print arquivo, permite_recuperacao
    arquivo = arquivo.replace('//', '/').replace('//', '/')
    executar_sql("""
        INSERT INTO public.arquivos(
            arquivo, data_criacao, permite_recuperacao, criado_em, 
            excluido, criado_por_id)
    VALUES ('%s', now(), %s, now(), 
            False, 1);
      """ % (arquivo, permite_recuperacao), False)


def salvar_arquivo_esocial(arquivo, texto, permite_recuperacao):
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




def assinar_esocial(xml):
    from emensageriapro.certificado import CERT, CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE
    from lxml import etree
    from emensageriapro.settings import FORCE_PRODUCAO_RESTRITA, BASE_DIR
    from signxml import XMLSigner, methods
    CERT_HOST = BASE_DIR + '/' + CERT_HOST
    CERT_PEM_FILE = CERT_PEM_FILE
    KEY_PEM_FILE = KEY_PEM_FILE
    # a = executar_sql("""
    # SELECT esocial_certificado, esocial_senha
    #   FROM public.transmissores where id=%s;
    # """ % transmissor_id, True)
    if FORCE_PRODUCAO_RESTRITA:
        xml = xml.replace('<tpAmb>1</tpAmb>','<tpAmb>2</tpAmb>')
    #try:
    create_pem_files(CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE)
    cert_str = ler_arquivo(CERT_PEM_FILE)
    key_str = ler_arquivo(KEY_PEM_FILE)
    root = etree.fromstring(xml)
    signed_root = XMLSigner(
        method=methods.enveloped,
        signature_algorithm=u'rsa-sha256',
        digest_algorithm=u'sha256',
        c14n_algorithm=u'http://www.w3.org/TR/2001/REC-xml-c14n-20010315').sign(root, key=key_str, cert=cert_str)
    return etree.tostring(signed_root)
    #except:
    #    return xml





def get_transmissor_name(transmissor_id):
    number = str(transmissor_id)
    while len(number) < 9:
        number = '0'+number
    return number



def create_request(dados, transmissor_dados):
    n = 0

    if dados['service'] == 'WsEnviarLoteEventos':

        xml = u''
        eventos = executar_sql("""
            SELECT tee.evento, tee.id, tee.identidade, tee.grupo, tee.tabela,
            tle.empregador_tpinsc, tle.empregador_nrinsc,
            t.tipo_inscricao, t.cpf_cnpj
            
            FROM public.transmissor_eventos_esocial tee
            JOIN public.transmissor_lote_esocial tle ON tle.id = tee.transmissor_lote_esocial_id
            JOIN public.transmissores t ON tle.transmissor_id = t.id
            WHERE tee.transmissor_lote_esocial_id = %(transmissor_id)s 
             AND tee.status=4 AND validacao_precedencia=1
            ORDER BY  tee.identidade;""" % dados, True)

        dados_evento = {}
        for e in eventos:
            n += 1
            dados_evento['evento'] = e[0]
            dados_evento['id'] = e[1]
            dados_evento['identidade'] = e[2]
            dados_evento['grupo'] = e[3]
            dados_evento['tabela'] = e[4]
            dados_evento['empregador_tpinsc'] = e[5]
            dados_evento['empregador_nrinsc'] = e[6]
            dados_evento['transmissor_tpinsc'] = e[7]
            dados_evento['transmissor_nrinsc'] = e[8]
            xml += '<evento Id="%s">' % e[2]
            xml += ler_arquivo('/arquivos/Eventos/%(tabela)s/%(identidade)s.xml' % dados_evento)
            xml += '</evento>'
        base_request = REQUEST_ENVIA_LOTE % dados_evento

    elif dados['service'] == 'WsConsultarLoteEventos':
        base_request = REQUEST_CONSULTA_LOTE
        a = executar_sql("""
          SELECT protocolo 
            FROM public.transmissor_lote_esocial 
           WHERE id= %(transmissor_id)s;""" % dados, True)
        xml = BASE_XML_CONSULTA_LOTE % a[0][0]
        base_request = REQUEST_CONSULTA_LOTE % transmissor_dados

    text = base_request.replace('<!--You may enter ANY elements at this point-->', xml)
    #print dados['request']
    salvar_arquivo_esocial(dados['request'], text, 0)
    return n




def send_xml(request, transmissor_id, service):
    from emensageriapro.settings import BASE_DIR
    from datetime import datetime
    data_atual = str(datetime.now()).replace(':','-').replace(' ','-').replace('.','-')
    criar_diretorio_arquivos()
    import os
    from emensageriapro.settings import FORCE_PRODUCAO_RESTRITA, TP_AMB, CA_CERT_PEM_FILE, CERT_HOST, CERT_PASS, CERT_PEM_FILE, KEY_PEM_FILE
    from emensageriapro.certificado import CERT
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
    dados = {}
    name = get_transmissor_name(transmissor_id)
    transmissor_dados = {}
    tra = executar_sql("""
        SELECT te.empregador_tpinsc, te.empregador_nrinsc,
                   t.tipo_inscricao, t.cpf_cnpj, 
                   t.esocial_lote_min, t.esocial_lote_max, 
                   t.esocial_timeout, t.esocial_certificado, t.esocial_senha
              FROM public.transmissor_lote_esocial te
              JOIN public.transmissores t ON t.id = te.transmissor_id
             WHERE te.id=%s;
    """ % transmissor_id, True)
    transmissor_dados['empregador_tpinsc'] = tra[0][0]
    transmissor_dados['empregador_nrinsc'] = tra[0][1]
    transmissor_dados['transmissor_tpinsc'] = tra[0][2]
    transmissor_dados['transmissor_nrinsc'] = tra[0][3]
    transmissor_dados['esocial_lote_min'] = tra[0][4]
    transmissor_dados['esocial_lote_max'] = tra[0][5]
    transmissor_dados['esocial_timeout'] = tra[0][6]
    transmissor_dados['esocial_certificado'] = BASE_DIR + 'uploads/'+tra[0][7]
    transmissor_dados['esocial_senha'] = tra[0][8]
    CERT_PEM_FILE = BASE_DIR + '/' + CERT_PEM_FILE
    KEY_PEM_FILE = BASE_DIR + '/' + KEY_PEM_FILE
    if not os.path.isfile(CERT_PEM_FILE):
        create_pem_files(CERT_HOST,
                         CERT_PASS,
                         CERT_PEM_FILE,
                         KEY_PEM_FILE)
    dados['transmissor_id'] = transmissor_id
    dados['header'] = 'arquivos/Comunicacao/%s/header/%s_%s.xml' % (service, name, data_atual)
    dados['request'] = 'arquivos/Comunicacao/%s/request/%s_%s.xml' % (service, name, data_atual)
    dados['response'] = 'arquivos/Comunicacao/%s/response/%s_%s.xml' % (service, name, data_atual)
    dados['header_completo'] = '%s/arquivos/Comunicacao/%s/header/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['request_completo'] = '%s/arquivos/Comunicacao/%s/request/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['response_completo'] = '%s/arquivos/Comunicacao/%s/response/%s_%s.xml' % (BASE_DIR, service, name, data_atual)
    dados['service'] = service
    dados['url'] = URL_WS
    dados['cert'] = CERT_PEM_FILE
    dados['cacert'] = '%s/certificados/webservicesproducaorestritaesocialgovbr.crt' % BASE_DIR
    dados['key'] = KEY_PEM_FILE
    dados['action'] = ACTION
    dados['timeout'] = transmissor_dados['esocial_timeout']
    qt_ev_validados = executar_sql("""
    SELECT count(*) FROM transmissor_eventos_esocial
     WHERE transmissor_lote_esocial_id=%s AND status=4""" % transmissor_id, True)
    quant_eventos_validados = qt_ev_validados[0][0]
    if quant_eventos_validados or service == 'WsConsultarLoteEventos':

        quant_eventos = create_request(dados, transmissor_dados)
        qt_ev = executar_sql("""
        SELECT count(*) FROM transmissor_eventos_esocial
         WHERE transmissor_lote_esocial_id=%s""" % transmissor_id, True)
        quant_eventos = qt_ev[0][0]
        if (quant_eventos >= transmissor_dados['esocial_lote_min'] and \
                quant_eventos <= transmissor_dados['esocial_lote_max'] and \
                service == 'WsEnviarLoteEventos') or service == 'WsConsultarLoteEventos':
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
            #print command
            command = command.replace('\n', '')
            for n in range(10):
                command = command.replace('  ', ' ')
            #print command
            os.system(command)
            if not os.path.isfile(BASE_DIR + '/' + dados['response']):
                messages.error(request, 'O servidor demorou mais que o esperado para efetuar a conexão! Caso necessário solicite ao administrador do sistema para que aumente o tempo do Timeout')
                return None
            if service == 'WsEnviarLoteEventos':
                from emensageriapro.funcoes_esocial_comunicacao import read_envioLoteEventos
                read_envioLoteEventos(dados['response'], transmissor_id)
                messages.success(request, 'Lote enviado com sucesso!')
            elif service == 'WsConsultarLoteEventos':
                from emensageriapro.funcoes_esocial_comunicacao import read_consultaLoteEventos
                messages.success(request, 'Lote consultado com sucesso!')
                read_consultaLoteEventos(dados['response'], transmissor_id)
            gravar_nome_arquivo(dados['header'], 0)
            gravar_nome_arquivo(dados['request'], 0)
            gravar_nome_arquivo(dados['response'], 0)
            if 'HTTP/1.1 200 OK' not in ler_arquivo(dados['header']):
                messages.warning(request, 'Retorno do servidor: ' + ler_arquivo(dados['header']) )
            if service == 'WsEnviarLoteEventos':
                alterar_status_transmissor(transmissor_id, 7)
            elif service == 'WsConsultarLoteEventos':
                alterar_status_transmissor(transmissor_id, 9)
        elif (quant_eventos < transmissor_dados['esocial_lote_min'] and \
                    service == 'WsEnviarLoteEventos'):
            messages.error(request, 'Lote com quantidade inferior a mínima permitida!')
            alterar_status_transmissor(transmissor_id, 0)
        elif (quant_eventos > transmissor_dados['esocial_lote_max'] and \
                  service == 'WsEnviarLoteEventos'):
            messages.error(request, 'Lote com quantidade de eventos superior a máxima permitida!')
            alterar_status_transmissor(transmissor_id, 0)
        else:
            messages.error(request, 'Erro ao enviar o lote!')
            if service == 'WsEnviarLoteEventos':
                alterar_status_transmissor(transmissor_id, 5)
            elif service == 'WsConsultarLoteEventos':
                alterar_status_transmissor(transmissor_id, 8)
    else:
        messages.error(request, 'Não possuem eventos validados para envio neste lote!')

    atualizar_status_esocial()




