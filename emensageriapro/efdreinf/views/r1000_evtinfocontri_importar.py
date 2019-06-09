#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r1000.models import *



def read_r1000_evtinfocontri_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r1000_evtinfocontri_obj(request, doc, status, validar)
    return dados



def read_r1000_evtinfocontri(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r1000_evtinfocontri_obj(request, doc, status, validar)

    r1000evtInfoContri.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r1000_evtinfocontri_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r1000_evtinfocontri_dados = {}
    r1000_evtinfocontri_dados['status'] = status
    r1000_evtinfocontri_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r1000_evtinfocontri_dados['identidade'] = doc.Reinf.evtInfoContri['id']
    evtInfoContri = doc.Reinf.evtInfoContri

    if 'inclusao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 1
    elif 'alteracao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 2
    elif 'exclusao' in dir(evtInfoContri.infoContri): r1000_evtinfocontri_dados['operacao'] = 3
    
    try:
        r1000_evtinfocontri_dados['tpamb'] = evtInfoContri.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r1000_evtinfocontri_dados['procemi'] = evtInfoContri.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r1000_evtinfocontri_dados['verproc'] = evtInfoContri.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r1000_evtinfocontri_dados['tpinsc'] = evtInfoContri.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r1000_evtinfocontri_dados['nrinsc'] = evtInfoContri.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
        
    r1000_evtinfocontri = r1000evtInfoContri.objects.create(**r1000_evtinfocontri_dados)
    
    if 'inclusao' in dir(evtInfoContri.infoContri):
    
        for inclusao in evtInfoContri.infoContri.inclusao:
    
            r1000_inclusao_dados = {}
            r1000_inclusao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri.id
            
            try:
                r1000_inclusao_dados['inivalid'] = inclusao.idePeriodo.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['fimvalid'] = inclusao.idePeriodo.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['classtrib'] = inclusao.infoCadastro.classTrib.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['indescrituracao'] = inclusao.infoCadastro.indEscrituracao.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['inddesoneracao'] = inclusao.infoCadastro.indDesoneracao.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['indacordoisenmulta'] = inclusao.infoCadastro.indAcordoIsenMulta.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['indsitpj'] = inclusao.infoCadastro.indSitPJ.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['nmctt'] = inclusao.infoCadastro.contato.nmCtt.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['cpfctt'] = inclusao.infoCadastro.contato.cpfCtt.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['fonefixo'] = inclusao.infoCadastro.contato.foneFixo.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['fonecel'] = inclusao.infoCadastro.contato.foneCel.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_inclusao_dados['email'] = inclusao.infoCadastro.contato.email.cdata
            except AttributeError: 
                pass
    
            r1000_inclusao = r1000inclusao.objects.create(**r1000_inclusao_dados)
            
            if 'softHouse' in dir(inclusao.infoCadastro):
            
                for softHouse in inclusao.infoCadastro.softHouse:
            
                    r1000_inclusao_softhouse_dados = {}
                    r1000_inclusao_softhouse_dados['r1000_inclusao_id'] = r1000_inclusao.id
                    
                    try:
                        r1000_inclusao_softhouse_dados['cnpjsofthouse'] = softHouse.cnpjSoftHouse.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_inclusao_softhouse_dados['nmrazao'] = softHouse.nmRazao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_inclusao_softhouse_dados['nmcont'] = softHouse.nmCont.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_inclusao_softhouse_dados['telefone'] = softHouse.telefone.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_inclusao_softhouse_dados['email'] = softHouse.email.cdata
                    except AttributeError: 
                        pass
            
                    r1000_inclusao_softhouse = r1000inclusaosoftHouse.objects.create(**r1000_inclusao_softhouse_dados)
            
            if 'infoEFR' in dir(inclusao.infoCadastro):
            
                for infoEFR in inclusao.infoCadastro.infoEFR:
            
                    r1000_inclusao_infoefr_dados = {}
                    r1000_inclusao_infoefr_dados['r1000_inclusao_id'] = r1000_inclusao.id
                    
                    try:
                        r1000_inclusao_infoefr_dados['ideefr'] = infoEFR.ideEFR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_inclusao_infoefr_dados['cnpjefr'] = infoEFR.cnpjEFR.cdata
                    except AttributeError: 
                        pass
            
                    r1000_inclusao_infoefr = r1000inclusaoinfoEFR.objects.create(**r1000_inclusao_infoefr_dados)
    
    if 'alteracao' in dir(evtInfoContri.infoContri):
    
        for alteracao in evtInfoContri.infoContri.alteracao:
    
            r1000_alteracao_dados = {}
            r1000_alteracao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri.id
            
            try:
                r1000_alteracao_dados['inivalid'] = alteracao.idePeriodo.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['fimvalid'] = alteracao.idePeriodo.fimValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['classtrib'] = alteracao.infoCadastro.classTrib.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['indescrituracao'] = alteracao.infoCadastro.indEscrituracao.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['inddesoneracao'] = alteracao.infoCadastro.indDesoneracao.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['indacordoisenmulta'] = alteracao.infoCadastro.indAcordoIsenMulta.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['indsitpj'] = alteracao.infoCadastro.indSitPJ.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['nmctt'] = alteracao.infoCadastro.contato.nmCtt.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['cpfctt'] = alteracao.infoCadastro.contato.cpfCtt.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['fonefixo'] = alteracao.infoCadastro.contato.foneFixo.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['fonecel'] = alteracao.infoCadastro.contato.foneCel.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_alteracao_dados['email'] = alteracao.infoCadastro.contato.email.cdata
            except AttributeError: 
                pass
    
            r1000_alteracao = r1000alteracao.objects.create(**r1000_alteracao_dados)
            
            if 'softHouse' in dir(alteracao.infoCadastro):
            
                for softHouse in alteracao.infoCadastro.softHouse:
            
                    r1000_alteracao_softhouse_dados = {}
                    r1000_alteracao_softhouse_dados['r1000_alteracao_id'] = r1000_alteracao.id
                    
                    try:
                        r1000_alteracao_softhouse_dados['cnpjsofthouse'] = softHouse.cnpjSoftHouse.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_alteracao_softhouse_dados['nmrazao'] = softHouse.nmRazao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_alteracao_softhouse_dados['nmcont'] = softHouse.nmCont.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_alteracao_softhouse_dados['telefone'] = softHouse.telefone.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_alteracao_softhouse_dados['email'] = softHouse.email.cdata
                    except AttributeError: 
                        pass
            
                    r1000_alteracao_softhouse = r1000alteracaosoftHouse.objects.create(**r1000_alteracao_softhouse_dados)
            
            if 'infoEFR' in dir(alteracao.infoCadastro):
            
                for infoEFR in alteracao.infoCadastro.infoEFR:
            
                    r1000_alteracao_infoefr_dados = {}
                    r1000_alteracao_infoefr_dados['r1000_alteracao_id'] = r1000_alteracao.id
                    
                    try:
                        r1000_alteracao_infoefr_dados['ideefr'] = infoEFR.ideEFR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_alteracao_infoefr_dados['cnpjefr'] = infoEFR.cnpjEFR.cdata
                    except AttributeError: 
                        pass
            
                    r1000_alteracao_infoefr = r1000alteracaoinfoEFR.objects.create(**r1000_alteracao_infoefr_dados)
            
            if 'novaValidade' in dir(alteracao):
            
                for novaValidade in alteracao.novaValidade:
            
                    r1000_alteracao_novavalidade_dados = {}
                    r1000_alteracao_novavalidade_dados['r1000_alteracao_id'] = r1000_alteracao.id
                    
                    try:
                        r1000_alteracao_novavalidade_dados['inivalid'] = novaValidade.iniValid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r1000_alteracao_novavalidade_dados['fimvalid'] = novaValidade.fimValid.cdata
                    except AttributeError: 
                        pass
            
                    r1000_alteracao_novavalidade = r1000alteracaonovaValidade.objects.create(**r1000_alteracao_novavalidade_dados)
    
    if 'exclusao' in dir(evtInfoContri.infoContri):
    
        for exclusao in evtInfoContri.infoContri.exclusao:
    
            r1000_exclusao_dados = {}
            r1000_exclusao_dados['r1000_evtinfocontri_id'] = r1000_evtinfocontri.id
            
            try:
                r1000_exclusao_dados['inivalid'] = exclusao.idePeriodo.iniValid.cdata
            except AttributeError: 
                pass
            
            try:
                r1000_exclusao_dados['fimvalid'] = exclusao.idePeriodo.fimValid.cdata
            except AttributeError: 
                pass
    
            r1000_exclusao = r1000exclusao.objects.create(**r1000_exclusao_dados)    
    r1000_evtinfocontri_dados['evento'] = 'r1000'
    r1000_evtinfocontri_dados['id'] = r1000_evtinfocontri.id
    r1000_evtinfocontri_dados['identidade_evento'] = doc.Reinf.evtInfoContri['id']
    r1000_evtinfocontri_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r1000_evtinfocontri_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r1000_evtinfocontri.id)
    
    return r1000_evtinfocontri_dados