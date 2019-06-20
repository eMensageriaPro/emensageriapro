#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r3010.models import *



def read_r3010_evtespdesportivo_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r3010_evtespdesportivo_obj(request, doc, status, validar)
    return dados



def read_r3010_evtespdesportivo(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r3010_evtespdesportivo_obj(request, doc, status, validar)

    r3010evtEspDesportivo.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r3010_evtespdesportivo_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r3010_evtespdesportivo_dados = {}
    r3010_evtespdesportivo_dados['status'] = status
    r3010_evtespdesportivo_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r3010_evtespdesportivo_dados['identidade'] = doc.Reinf.evtEspDesportivo['id']
    evtEspDesportivo = doc.Reinf.evtEspDesportivo
    
    try:
        r3010_evtespdesportivo_dados['indretif'] = evtEspDesportivo.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['nrrecibo'] = evtEspDesportivo.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['dtapuracao'] = evtEspDesportivo.ideEvento.dtApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['tpamb'] = evtEspDesportivo.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['procemi'] = evtEspDesportivo.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['verproc'] = evtEspDesportivo.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['tpinsc'] = evtEspDesportivo.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['nrinsc'] = evtEspDesportivo.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['tpinscestab'] = evtEspDesportivo.ideContri.ideEstab.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['nrinscestab'] = evtEspDesportivo.ideContri.ideEstab.nrInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['vlrreceitatotal'] = evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaTotal.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['vlrcp'] = evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCP.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['vlrcpsusptotal'] = evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrCPSuspTotal.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['vlrreceitaclubes'] = evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrReceitaClubes.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
    
    try:
        r3010_evtespdesportivo_dados['vlrretparc'] = evtEspDesportivo.ideContri.ideEstab.receitaTotal.vlrRetParc.cdata.replace('.', '').replace(',', '.')
    except AttributeError: 
        pass
        
    r3010_evtespdesportivo = r3010evtEspDesportivo.objects.create(**r3010_evtespdesportivo_dados)
    
    if 'boletim' in dir(evtEspDesportivo.ideContri.ideEstab):
    
        for boletim in evtEspDesportivo.ideContri.ideEstab.boletim:
    
            r3010_boletim_dados = {}
            r3010_boletim_dados['r3010_evtespdesportivo_id'] = r3010_evtespdesportivo.id
            
            try:
                r3010_boletim_dados['nrboletim'] = boletim.nrBoletim.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['tpcompeticao'] = boletim.tpCompeticao.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['categevento'] = boletim.categEvento.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['moddesportiva'] = boletim.modDesportiva.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['nomecompeticao'] = boletim.nomeCompeticao.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['cnpjmandante'] = boletim.cnpjMandante.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['cnpjvisitante'] = boletim.cnpjVisitante.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['nomevisitante'] = boletim.nomeVisitante.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['pracadesportiva'] = boletim.pracaDesportiva.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['codmunic'] = boletim.codMunic.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['uf'] = boletim.uf.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['qtdepagantes'] = boletim.qtdePagantes.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_boletim_dados['qtdenaopagantes'] = boletim.qtdeNaoPagantes.cdata
            except AttributeError: 
                pass
    
            r3010_boletim = r3010boletim.objects.create(**r3010_boletim_dados)
            
            if 'receitaIngressos' in dir(boletim):
            
                for receitaIngressos in boletim.receitaIngressos:
            
                    r3010_receitaingressos_dados = {}
                    r3010_receitaingressos_dados['r3010_boletim_id'] = r3010_boletim.id
                    
                    try:
                        r3010_receitaingressos_dados['tpingresso'] = receitaIngressos.tpIngresso.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_receitaingressos_dados['descingr'] = receitaIngressos.descIngr.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_receitaingressos_dados['qtdeingrvenda'] = receitaIngressos.qtdeIngrVenda.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_receitaingressos_dados['qtdeingrvendidos'] = receitaIngressos.qtdeIngrVendidos.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_receitaingressos_dados['qtdeingrdev'] = receitaIngressos.qtdeIngrDev.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_receitaingressos_dados['precoindiv'] = receitaIngressos.precoIndiv.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_receitaingressos_dados['vlrtotal'] = receitaIngressos.vlrTotal.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r3010_receitaingressos = r3010receitaIngressos.objects.create(**r3010_receitaingressos_dados)
            
            if 'outrasReceitas' in dir(boletim):
            
                for outrasReceitas in boletim.outrasReceitas:
            
                    r3010_outrasreceitas_dados = {}
                    r3010_outrasreceitas_dados['r3010_boletim_id'] = r3010_boletim.id
                    
                    try:
                        r3010_outrasreceitas_dados['tpreceita'] = outrasReceitas.tpReceita.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_outrasreceitas_dados['vlrreceita'] = outrasReceitas.vlrReceita.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r3010_outrasreceitas_dados['descreceita'] = outrasReceitas.descReceita.cdata
                    except AttributeError: 
                        pass
            
                    r3010_outrasreceitas = r3010outrasReceitas.objects.create(**r3010_outrasreceitas_dados)
    
    if 'infoProc' in dir(evtEspDesportivo.ideContri.ideEstab.receitaTotal):
    
        for infoProc in evtEspDesportivo.ideContri.ideEstab.receitaTotal.infoProc:
    
            r3010_infoproc_dados = {}
            r3010_infoproc_dados['r3010_evtespdesportivo_id'] = r3010_evtespdesportivo.id
            
            try:
                r3010_infoproc_dados['tpproc'] = infoProc.tpProc.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_infoproc_dados['nrproc'] = infoProc.nrProc.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_infoproc_dados['codsusp'] = infoProc.codSusp.cdata
            except AttributeError: 
                pass
            
            try:
                r3010_infoproc_dados['vlrcpsusp'] = infoProc.vlrCPSusp.cdata.replace('.', '').replace(',', '.')
            except AttributeError: 
                pass
    
            r3010_infoproc = r3010infoProc.objects.create(**r3010_infoproc_dados)    
    r3010_evtespdesportivo_dados['evento'] = 'r3010'
    r3010_evtespdesportivo_dados['id'] = r3010_evtespdesportivo.id
    r3010_evtespdesportivo_dados['identidade_evento'] = doc.Reinf.evtEspDesportivo['id']
    r3010_evtespdesportivo_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r3010_evtespdesportivo_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r3010_evtespdesportivo.id)
    
    return r3010_evtespdesportivo_dados