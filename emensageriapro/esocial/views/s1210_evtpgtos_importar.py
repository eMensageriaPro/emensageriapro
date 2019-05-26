#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1210.models import *



def read_s1210_evtpgtos_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1210_evtpgtos_obj(doc, status, validar)
    return dados



def read_s1210_evtpgtos(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1210_evtpgtos_obj(doc, status, validar)
    return dados



def read_s1210_evtpgtos_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1210_evtpgtos_dados = {}
    s1210_evtpgtos_dados['status'] = status
    s1210_evtpgtos_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1210_evtpgtos_dados['identidade'] = doc.eSocial.evtPgtos['Id']
    evtPgtos = doc.eSocial.evtPgtos
    
    try:
        s1210_evtpgtos_dados['indretif'] = evtPgtos.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['nrrecibo'] = evtPgtos.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['indapuracao'] = evtPgtos.ideEvento.indApuracao.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['perapur'] = evtPgtos.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['tpamb'] = evtPgtos.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['procemi'] = evtPgtos.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['verproc'] = evtPgtos.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['tpinsc'] = evtPgtos.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['nrinsc'] = evtPgtos.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s1210_evtpgtos_dados['cpfbenef'] = evtPgtos.ideBenef.cpfBenef.cdata
    except AttributeError: 
        pass
        
    s1210_evtpgtos = s1210evtPgtos.objects.create(**s1210_evtpgtos_dados)
    
    if 'deps' in dir(evtPgtos.ideBenef):
    
        for deps in evtPgtos.ideBenef.deps:
    
            s1210_deps_dados = {}
            s1210_deps_dados['s1210_evtpgtos_id'] = s1210_evtpgtos.id
            
            try:
                s1210_deps_dados['vrdeddep'] = deps.vrDedDep.cdata
            except AttributeError: 
                pass
    
            s1210_deps = s1210deps.objects.create(**s1210_deps_dados)
    
    if 'infoPgto' in dir(evtPgtos.ideBenef):
    
        for infoPgto in evtPgtos.ideBenef.infoPgto:
    
            s1210_infopgto_dados = {}
            s1210_infopgto_dados['s1210_evtpgtos_id'] = s1210_evtpgtos.id
            
            try:
                s1210_infopgto_dados['dtpgto'] = infoPgto.dtPgto.cdata
            except AttributeError: 
                pass
            
            try:
                s1210_infopgto_dados['tppgto'] = infoPgto.tpPgto.cdata
            except AttributeError: 
                pass
            
            try:
                s1210_infopgto_dados['indresbr'] = infoPgto.indResBr.cdata
            except AttributeError: 
                pass
    
            s1210_infopgto = s1210infoPgto.objects.create(**s1210_infopgto_dados)
            
            if 'detPgtoFl' in dir(infoPgto):
            
                for detPgtoFl in infoPgto.detPgtoFl:
            
                    s1210_detpgtofl_dados = {}
                    s1210_detpgtofl_dados['s1210_infopgto_id'] = s1210_infopgto.id
                    
                    try:
                        s1210_detpgtofl_dados['perref'] = detPgtoFl.perRef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofl_dados['idedmdev'] = detPgtoFl.ideDmDev.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofl_dados['indpgtott'] = detPgtoFl.indPgtoTt.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofl_dados['vrliq'] = detPgtoFl.vrLiq.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofl_dados['nrrecarq'] = detPgtoFl.nrRecArq.cdata
                    except AttributeError: 
                        pass
            
                    s1210_detpgtofl = s1210detPgtoFl.objects.create(**s1210_detpgtofl_dados)
                    
                    if 'retPgtoTot' in dir(detPgtoFl):
                    
                        for retPgtoTot in detPgtoFl.retPgtoTot:
                    
                            s1210_detpgtofl_retpgtotot_dados = {}
                            s1210_detpgtofl_retpgtotot_dados['s1210_detpgtofl_id'] = s1210_detpgtofl.id
                            
                            try:
                                s1210_detpgtofl_retpgtotot_dados['codrubr'] = retPgtoTot.codRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_retpgtotot_dados['idetabrubr'] = retPgtoTot.ideTabRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_retpgtotot_dados['qtdrubr'] = retPgtoTot.qtdRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_retpgtotot_dados['fatorrubr'] = retPgtoTot.fatorRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_retpgtotot_dados['vrunit'] = retPgtoTot.vrUnit.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_retpgtotot_dados['vrrubr'] = retPgtoTot.vrRubr.cdata
                            except AttributeError: 
                                pass
                    
                            s1210_detpgtofl_retpgtotot = s1210detPgtoFlretPgtoTot.objects.create(**s1210_detpgtofl_retpgtotot_dados)
                            
                            if 'penAlim' in dir(retPgtoTot):
                            
                                for penAlim in retPgtoTot.penAlim:
                            
                                    s1210_detpgtofl_penalim_dados = {}
                                    s1210_detpgtofl_penalim_dados['s1210_detpgtofl_retpgtotot_id'] = s1210_detpgtofl_retpgtotot.id
                                    
                                    try:
                                        s1210_detpgtofl_penalim_dados['cpfbenef'] = penAlim.cpfBenef.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1210_detpgtofl_penalim_dados['dtnasctobenef'] = penAlim.dtNasctoBenef.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1210_detpgtofl_penalim_dados['nmbenefic'] = penAlim.nmBenefic.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1210_detpgtofl_penalim_dados['vlrpensao'] = penAlim.vlrPensao.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s1210_detpgtofl_penalim = s1210detPgtoFlpenAlim.objects.create(**s1210_detpgtofl_penalim_dados)
                    
                    if 'infoPgtoParc' in dir(detPgtoFl):
                    
                        for infoPgtoParc in detPgtoFl.infoPgtoParc:
                    
                            s1210_detpgtofl_infopgtoparc_dados = {}
                            s1210_detpgtofl_infopgtoparc_dados['s1210_detpgtofl_id'] = s1210_detpgtofl.id
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['matricula'] = infoPgtoParc.matricula.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['codrubr'] = infoPgtoParc.codRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['idetabrubr'] = infoPgtoParc.ideTabRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['qtdrubr'] = infoPgtoParc.qtdRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['fatorrubr'] = infoPgtoParc.fatorRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['vrunit'] = infoPgtoParc.vrUnit.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['vrrubr'] = infoPgtoParc.vrRubr.cdata
                            except AttributeError: 
                                pass
                    
                            s1210_detpgtofl_infopgtoparc = s1210detPgtoFlinfoPgtoParc.objects.create(**s1210_detpgtofl_infopgtoparc_dados)
            
            if 'detPgtoBenPr' in dir(infoPgto):
            
                for detPgtoBenPr in infoPgto.detPgtoBenPr:
            
                    s1210_detpgtobenpr_dados = {}
                    s1210_detpgtobenpr_dados['s1210_infopgto_id'] = s1210_infopgto.id
                    
                    try:
                        s1210_detpgtobenpr_dados['perref'] = detPgtoBenPr.perRef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtobenpr_dados['idedmdev'] = detPgtoBenPr.ideDmDev.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtobenpr_dados['indpgtott'] = detPgtoBenPr.indPgtoTt.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtobenpr_dados['vrliq'] = detPgtoBenPr.vrLiq.cdata
                    except AttributeError: 
                        pass
            
                    s1210_detpgtobenpr = s1210detPgtoBenPr.objects.create(**s1210_detpgtobenpr_dados)
                    
                    if 'retPgtoTot' in dir(detPgtoBenPr):
                    
                        for retPgtoTot in detPgtoBenPr.retPgtoTot:
                    
                            s1210_detpgtobenpr_retpgtotot_dados = {}
                            s1210_detpgtobenpr_retpgtotot_dados['s1210_detpgtobenpr_id'] = s1210_detpgtobenpr.id
                            
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['codrubr'] = retPgtoTot.codRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['idetabrubr'] = retPgtoTot.ideTabRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['qtdrubr'] = retPgtoTot.qtdRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['fatorrubr'] = retPgtoTot.fatorRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['vrunit'] = retPgtoTot.vrUnit.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['vrrubr'] = retPgtoTot.vrRubr.cdata
                            except AttributeError: 
                                pass
                    
                            s1210_detpgtobenpr_retpgtotot = s1210detPgtoBenPrretPgtoTot.objects.create(**s1210_detpgtobenpr_retpgtotot_dados)
                    
                    if 'infoPgtoParc' in dir(detPgtoBenPr):
                    
                        for infoPgtoParc in detPgtoBenPr.infoPgtoParc:
                    
                            s1210_detpgtobenpr_infopgtoparc_dados = {}
                            s1210_detpgtobenpr_infopgtoparc_dados['s1210_detpgtobenpr_id'] = s1210_detpgtobenpr.id
                            
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['codrubr'] = infoPgtoParc.codRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['idetabrubr'] = infoPgtoParc.ideTabRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['qtdrubr'] = infoPgtoParc.qtdRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['fatorrubr'] = infoPgtoParc.fatorRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['vrunit'] = infoPgtoParc.vrUnit.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['vrrubr'] = infoPgtoParc.vrRubr.cdata
                            except AttributeError: 
                                pass
                    
                            s1210_detpgtobenpr_infopgtoparc = s1210detPgtoBenPrinfoPgtoParc.objects.create(**s1210_detpgtobenpr_infopgtoparc_dados)
            
            if 'detPgtoFer' in dir(infoPgto):
            
                for detPgtoFer in infoPgto.detPgtoFer:
            
                    s1210_detpgtofer_dados = {}
                    s1210_detpgtofer_dados['s1210_infopgto_id'] = s1210_infopgto.id
                    
                    try:
                        s1210_detpgtofer_dados['codcateg'] = detPgtoFer.codCateg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofer_dados['matricula'] = detPgtoFer.matricula.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofer_dados['dtinigoz'] = detPgtoFer.dtIniGoz.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofer_dados['qtdias'] = detPgtoFer.qtDias.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_detpgtofer_dados['vrliq'] = detPgtoFer.vrLiq.cdata
                    except AttributeError: 
                        pass
            
                    s1210_detpgtofer = s1210detPgtoFer.objects.create(**s1210_detpgtofer_dados)
                    
                    if 'detRubrFer' in dir(detPgtoFer):
                    
                        for detRubrFer in detPgtoFer.detRubrFer:
                    
                            s1210_detpgtofer_detrubrfer_dados = {}
                            s1210_detpgtofer_detrubrfer_dados['s1210_detpgtofer_id'] = s1210_detpgtofer.id
                            
                            try:
                                s1210_detpgtofer_detrubrfer_dados['codrubr'] = detRubrFer.codRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofer_detrubrfer_dados['idetabrubr'] = detRubrFer.ideTabRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofer_detrubrfer_dados['qtdrubr'] = detRubrFer.qtdRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofer_detrubrfer_dados['fatorrubr'] = detRubrFer.fatorRubr.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofer_detrubrfer_dados['vrunit'] = detRubrFer.vrUnit.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtofer_detrubrfer_dados['vrrubr'] = detRubrFer.vrRubr.cdata
                            except AttributeError: 
                                pass
                    
                            s1210_detpgtofer_detrubrfer = s1210detPgtoFerdetRubrFer.objects.create(**s1210_detpgtofer_detrubrfer_dados)
                            
                            if 'penAlim' in dir(detRubrFer):
                            
                                for penAlim in detRubrFer.penAlim:
                            
                                    s1210_detpgtofer_penalim_dados = {}
                                    s1210_detpgtofer_penalim_dados['s1210_detpgtofer_detrubrfer_id'] = s1210_detpgtofer_detrubrfer.id
                                    
                                    try:
                                        s1210_detpgtofer_penalim_dados['cpfbenef'] = penAlim.cpfBenef.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1210_detpgtofer_penalim_dados['dtnasctobenef'] = penAlim.dtNasctoBenef.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1210_detpgtofer_penalim_dados['nmbenefic'] = penAlim.nmBenefic.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        s1210_detpgtofer_penalim_dados['vlrpensao'] = penAlim.vlrPensao.cdata
                                    except AttributeError: 
                                        pass
                            
                                    s1210_detpgtofer_penalim = s1210detPgtoFerpenAlim.objects.create(**s1210_detpgtofer_penalim_dados)
            
            if 'detPgtoAnt' in dir(infoPgto):
            
                for detPgtoAnt in infoPgto.detPgtoAnt:
            
                    s1210_detpgtoant_dados = {}
                    s1210_detpgtoant_dados['s1210_infopgto_id'] = s1210_infopgto.id
                    
                    try:
                        s1210_detpgtoant_dados['codcateg'] = detPgtoAnt.codCateg.cdata
                    except AttributeError: 
                        pass
            
                    s1210_detpgtoant = s1210detPgtoAnt.objects.create(**s1210_detpgtoant_dados)
                    
                    if 'infoPgtoAnt' in dir(detPgtoAnt):
                    
                        for infoPgtoAnt in detPgtoAnt.infoPgtoAnt:
                    
                            s1210_detpgtoant_infopgtoant_dados = {}
                            s1210_detpgtoant_infopgtoant_dados['s1210_detpgtoant_id'] = s1210_detpgtoant.id
                            
                            try:
                                s1210_detpgtoant_infopgtoant_dados['tpbcirrf'] = infoPgtoAnt.tpBcIRRF.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                s1210_detpgtoant_infopgtoant_dados['vrbcirrf'] = infoPgtoAnt.vrBcIRRF.cdata
                            except AttributeError: 
                                pass
                    
                            s1210_detpgtoant_infopgtoant = s1210detPgtoAntinfoPgtoAnt.objects.create(**s1210_detpgtoant_infopgtoant_dados)
            
            if 'idePgtoExt' in dir(infoPgto):
            
                for idePgtoExt in infoPgto.idePgtoExt:
            
                    s1210_idepgtoext_dados = {}
                    s1210_idepgtoext_dados['s1210_infopgto_id'] = s1210_infopgto.id
                    
                    try:
                        s1210_idepgtoext_dados['codpais'] = idePgtoExt.idePais.codPais.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['indnif'] = idePgtoExt.idePais.indNIF.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['nifbenef'] = idePgtoExt.idePais.nifBenef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['dsclograd'] = idePgtoExt.endExt.dscLograd.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['nrlograd'] = idePgtoExt.endExt.nrLograd.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['complem'] = idePgtoExt.endExt.complem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['bairro'] = idePgtoExt.endExt.bairro.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['nmcid'] = idePgtoExt.endExt.nmCid.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        s1210_idepgtoext_dados['codpostal'] = idePgtoExt.endExt.codPostal.cdata
                    except AttributeError: 
                        pass
            
                    s1210_idepgtoext = s1210idePgtoExt.objects.create(**s1210_idepgtoext_dados)    
    s1210_evtpgtos_dados['evento'] = 's1210'
    s1210_evtpgtos_dados['id'] = s1210_evtpgtos.id
    s1210_evtpgtos_dados['identidade_evento'] = doc.eSocial.evtPgtos['Id']
    s1210_evtpgtos_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s1210_evtpgtos_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s1210_evtpgtos.id)
    return s1210_evtpgtos_dados