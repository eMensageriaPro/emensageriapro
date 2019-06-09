#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4010.models import *



def read_r4010_evtretpf_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4010_evtretpf_obj(request, doc, status, validar)
    return dados



def read_r4010_evtretpf(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4010_evtretpf_obj(request, doc, status, validar)

    r4010evtRetPF.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r4010_evtretpf_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4010_evtretpf_dados = {}
    r4010_evtretpf_dados['status'] = status
    r4010_evtretpf_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4010_evtretpf_dados['identidade'] = doc.Reinf.evtRetPF['id']
    evtRetPF = doc.Reinf.evtRetPF
    
    try:
        r4010_evtretpf_dados['indretif'] = evtRetPF.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['nrrecibo'] = evtRetPF.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['perapur'] = evtRetPF.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['tpamb'] = evtRetPF.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['procemi'] = evtRetPF.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['verproc'] = evtRetPF.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['tpinsc'] = evtRetPF.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['nrinsc'] = evtRetPF.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['tpinscestab'] = evtRetPF.ideEstab.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['nrinscestab'] = evtRetPF.ideEstab.nrInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['cpfbenef'] = evtRetPF.ideEstab.ideBenef.cpfBenef.cdata
    except AttributeError: 
        pass
    
    try:
        r4010_evtretpf_dados['nmbenef'] = evtRetPF.ideEstab.ideBenef.nmBenef.cdata
    except AttributeError: 
        pass
        
    r4010_evtretpf = r4010evtRetPF.objects.create(**r4010_evtretpf_dados)
    
    if 'idePgto' in dir(evtRetPF.ideEstab.ideBenef):
    
        for idePgto in evtRetPF.ideEstab.ideBenef.idePgto:
    
            r4010_idepgto_dados = {}
            r4010_idepgto_dados['r4010_evtretpf_id'] = r4010_evtretpf.id
            
            try:
                r4010_idepgto_dados['natrend'] = idePgto.natRend.cdata
            except AttributeError: 
                pass
            
            try:
                r4010_idepgto_dados['paisresid'] = idePgto.paisResid.cdata
            except AttributeError: 
                pass
            
            try:
                r4010_idepgto_dados['observ'] = idePgto.observ.cdata
            except AttributeError: 
                pass
    
            r4010_idepgto = r4010idePgto.objects.create(**r4010_idepgto_dados)
            
            if 'infoPgto' in dir(idePgto):
            
                for infoPgto in idePgto.infoPgto:
            
                    r4010_infopgto_dados = {}
                    r4010_infopgto_dados['r4010_idepgto_id'] = r4010_idepgto.id
                    
                    try:
                        r4010_infopgto_dados['dtfg'] = infoPgto.dtFG.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['inddecterc'] = infoPgto.indDecTerc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrrendbruto'] = infoPgto.vlrRendBruto.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrrendtrib'] = infoPgto.vlrRendTrib.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrir'] = infoPgto.vlrIR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrrendsusp'] = infoPgto.vlrRendSusp.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrnir'] = infoPgto.vlrNIR.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrdeposito'] = infoPgto.vlrDeposito.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrcompanocalend'] = infoPgto.vlrCompAnoCalend.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgto_dados['vlrcompanoant'] = infoPgto.vlrCompAnoAnt.cdata
                    except AttributeError: 
                        pass
            
                    r4010_infopgto = r4010infoPgto.objects.create(**r4010_infopgto_dados)
                    
                    if 'FCI' in dir(infoPgto):
                    
                        for FCI in infoPgto.FCI:
                    
                            r4010_fci_dados = {}
                            r4010_fci_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_fci_dados['nrinscfci'] = FCI.nrInscFCI.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_fci = r4010FCI.objects.create(**r4010_fci_dados)
                    
                    if 'SCP' in dir(infoPgto):
                    
                        for SCP in infoPgto.SCP:
                    
                            r4010_scp_dados = {}
                            r4010_scp_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_scp_dados['nrinscscp'] = SCP.nrInscSCP.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_scp_dados['percscp'] = SCP.percSCP.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_scp = r4010SCP.objects.create(**r4010_scp_dados)
                    
                    if 'detDed' in dir(infoPgto):
                    
                        for detDed in infoPgto.detDed:
                    
                            r4010_detded_dados = {}
                            r4010_detded_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_detded_dados['indtpdeducao'] = detDed.indTpDeducao.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_detded_dados['vlrdeducao'] = detDed.vlrDeducao.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_detded_dados['vlrdedsusp'] = detDed.vlrDedSusp.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_detded_dados['nrinscprevcomp'] = detDed.nrInscPrevComp.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_detded = r4010detDed.objects.create(**r4010_detded_dados)
                            
                            if 'benefPen' in dir(detDed):
                            
                                for benefPen in detDed.benefPen:
                            
                                    r4010_benefpen_dados = {}
                                    r4010_benefpen_dados['r4010_detded_id'] = r4010_detded.id
                                    
                                    try:
                                        r4010_benefpen_dados['cpf'] = benefPen.cpf.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4010_benefpen_dados['dtnascto'] = benefPen.dtNascto.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4010_benefpen_dados['nome'] = benefPen.nome.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4010_benefpen_dados['reldep'] = benefPen.relDep.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4010_benefpen_dados['descrdep'] = benefPen.descrDep.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r4010_benefpen = r4010benefPen.objects.create(**r4010_benefpen_dados)
                    
                    if 'rendIsento' in dir(infoPgto):
                    
                        for rendIsento in infoPgto.rendIsento:
                    
                            r4010_rendisento_dados = {}
                            r4010_rendisento_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_rendisento_dados['tpisencao'] = rendIsento.tpIsencao.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_rendisento_dados['vlrisento'] = rendIsento.vlrIsento.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_rendisento_dados['descrendimento'] = rendIsento.descRendimento.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_rendisento_dados['dtlaudo'] = rendIsento.dtLaudo.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_rendisento = r4010rendIsento.objects.create(**r4010_rendisento_dados)
                    
                    if 'infoProcRet' in dir(infoPgto):
                    
                        for infoProcRet in infoPgto.infoProcRet:
                    
                            r4010_infoprocret_dados = {}
                            r4010_infoprocret_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_infoprocret_dados['tpprocret'] = infoProcRet.tpProcRet.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_infoprocret_dados['nrprocret'] = infoProcRet.nrProcRet.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_infoprocret_dados['codsusp'] = infoProcRet.codSusp.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_infoprocret_dados['vlrnretido'] = infoProcRet.vlrNRetido.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_infoprocret_dados['vlrdep'] = infoProcRet.vlrDep.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_infoprocret = r4010infoProcRet.objects.create(**r4010_infoprocret_dados)
                    
                    if 'infoRRA' in dir(infoPgto):
                    
                        for infoRRA in infoPgto.infoRRA:
                    
                            r4010_inforra_dados = {}
                            r4010_inforra_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_inforra_dados['tpprocrra'] = infoRRA.tpProcRRA.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforra_dados['nrprocrra'] = infoRRA.nrProcRRA.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforra_dados['indorigrec'] = infoRRA.indOrigRec.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforra_dados['descrra'] = infoRRA.descRRA.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforra_dados['qtdmesesrra'] = infoRRA.qtdMesesRRA.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_inforra = r4010infoRRA.objects.create(**r4010_inforra_dados)
                            
                            if 'despProcJud' in dir(infoRRA):
                            
                                for despProcJud in infoRRA.despProcJud:
                            
                                    r4010_inforra_despprocjud_dados = {}
                                    r4010_inforra_despprocjud_dados['r4010_inforra_id'] = r4010_inforra.id
                                    
                                    try:
                                        r4010_inforra_despprocjud_dados['vlrdespcustas'] = despProcJud.vlrDespCustas.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4010_inforra_despprocjud_dados['vlrdespadvogados'] = despProcJud.vlrDespAdvogados.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r4010_inforra_despprocjud = r4010infoRRAdespProcJud.objects.create(**r4010_inforra_despprocjud_dados)
                                    
                                    if 'ideAdv' in dir(despProcJud):
                                    
                                        for ideAdv in despProcJud.ideAdv:
                                    
                                            r4010_inforra_ideadv_dados = {}
                                            r4010_inforra_ideadv_dados['r4010_inforra_despprocjud_id'] = r4010_inforra_despprocjud.id
                                            
                                            try:
                                                r4010_inforra_ideadv_dados['tpinscadv'] = ideAdv.tpInscAdv.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r4010_inforra_ideadv_dados['nrinscadv'] = ideAdv.nrInscAdv.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r4010_inforra_ideadv_dados['vlradv'] = ideAdv.vlrAdv.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r4010_inforra_ideadv = r4010infoRRAideAdv.objects.create(**r4010_inforra_ideadv_dados)
                            
                            if 'origemRec' in dir(infoRRA):
                            
                                for origemRec in infoRRA.origemRec:
                            
                                    r4010_inforra_origemrec_dados = {}
                                    r4010_inforra_origemrec_dados['r4010_inforra_id'] = r4010_inforra.id
                                    
                                    try:
                                        r4010_inforra_origemrec_dados['cnpjorigrecurso'] = origemRec.cnpjOrigRecurso.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r4010_inforra_origemrec = r4010infoRRAorigemRec.objects.create(**r4010_inforra_origemrec_dados)
                    
                    if 'infoProcJud' in dir(infoPgto):
                    
                        for infoProcJud in infoPgto.infoProcJud:
                    
                            r4010_infoprocjud_dados = {}
                            r4010_infoprocjud_dados['r4010_infopgto_id'] = r4010_infopgto.id
                            
                            try:
                                r4010_infoprocjud_dados['nrproc'] = infoProcJud.nrProc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_infoprocjud_dados['indorigrec'] = infoProcJud.indOrigRec.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_infoprocjud_dados['desc'] = infoProcJud.desc.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_infoprocjud = r4010infoProcJud.objects.create(**r4010_infoprocjud_dados)
                            
                            if 'despProcJud' in dir(infoProcJud):
                            
                                for despProcJud in infoProcJud.despProcJud:
                            
                                    r4010_infoprocjud_despprocjud_dados = {}
                                    r4010_infoprocjud_despprocjud_dados['r4010_infoprocjud_id'] = r4010_infoprocjud.id
                                    
                                    try:
                                        r4010_infoprocjud_despprocjud_dados['vlrdespcustas'] = despProcJud.vlrDespCustas.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4010_infoprocjud_despprocjud_dados['vlrdespadvogados'] = despProcJud.vlrDespAdvogados.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r4010_infoprocjud_despprocjud = r4010infoProcJuddespProcJud.objects.create(**r4010_infoprocjud_despprocjud_dados)
                                    
                                    if 'ideAdv' in dir(despProcJud):
                                    
                                        for ideAdv in despProcJud.ideAdv:
                                    
                                            r4010_infoprocjud_ideadv_dados = {}
                                            r4010_infoprocjud_ideadv_dados['r4010_infoprocjud_despprocjud_id'] = r4010_infoprocjud_despprocjud.id
                                            
                                            try:
                                                r4010_infoprocjud_ideadv_dados['tpinscadv'] = ideAdv.tpInscAdv.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r4010_infoprocjud_ideadv_dados['nrinscadv'] = ideAdv.nrInscAdv.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r4010_infoprocjud_ideadv_dados['vlradv'] = ideAdv.vlrAdv.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r4010_infoprocjud_ideadv = r4010infoProcJudideAdv.objects.create(**r4010_infoprocjud_ideadv_dados)
                            
                            if 'origemRec' in dir(infoProcJud):
                            
                                for origemRec in infoProcJud.origemRec:
                            
                                    r4010_infoprocjud_origemrec_dados = {}
                                    r4010_infoprocjud_origemrec_dados['r4010_infoprocjud_id'] = r4010_infoprocjud.id
                                    
                                    try:
                                        r4010_infoprocjud_origemrec_dados['cnpjorigrecurso'] = origemRec.cnpjOrigRecurso.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r4010_infoprocjud_origemrec = r4010infoProcJudorigemRec.objects.create(**r4010_infoprocjud_origemrec_dados)
            
            if 'infoPgtoExt' in dir(idePgto):
            
                for infoPgtoExt in idePgto.infoPgtoExt:
            
                    r4010_infopgtoext_dados = {}
                    r4010_infopgtoext_dados['r4010_idepgto_id'] = r4010_idepgto.id
                    
                    try:
                        r4010_infopgtoext_dados['dsclograd'] = infoPgtoExt.endExt.dscLograd.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['nrlograd'] = infoPgtoExt.endExt.nrLograd.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['complem'] = infoPgtoExt.endExt.complem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['bairro'] = infoPgtoExt.endExt.bairro.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['cidade'] = infoPgtoExt.endExt.cidade.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['estado'] = infoPgtoExt.endExt.estado.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['codpostal'] = infoPgtoExt.endExt.codPostal.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['telef'] = infoPgtoExt.endExt.telef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['indnif'] = infoPgtoExt.infoFiscal.indNIF.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['nifbenef'] = infoPgtoExt.infoFiscal.nifBenef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infopgtoext_dados['frmtribut'] = infoPgtoExt.infoFiscal.frmTribut.cdata
                    except AttributeError: 
                        pass
            
                    r4010_infopgtoext = r4010infoPgtoExt.objects.create(**r4010_infopgtoext_dados)
    
    if 'ideOpSaude' in dir(evtRetPF.ideEstab.ideBenef):
    
        for ideOpSaude in evtRetPF.ideEstab.ideBenef.ideOpSaude:
    
            r4010_ideopsaude_dados = {}
            r4010_ideopsaude_dados['r4010_evtretpf_id'] = r4010_evtretpf.id
            
            try:
                r4010_ideopsaude_dados['nrinsc'] = ideOpSaude.nrInsc.cdata
            except AttributeError: 
                pass
            
            try:
                r4010_ideopsaude_dados['regans'] = ideOpSaude.regANS.cdata
            except AttributeError: 
                pass
            
            try:
                r4010_ideopsaude_dados['vlrsaude'] = ideOpSaude.vlrSaude.cdata
            except AttributeError: 
                pass
    
            r4010_ideopsaude = r4010ideOpSaude.objects.create(**r4010_ideopsaude_dados)
            
            if 'infoReemb' in dir(ideOpSaude):
            
                for infoReemb in ideOpSaude.infoReemb:
            
                    r4010_inforeemb_dados = {}
                    r4010_inforeemb_dados['r4010_ideopsaude_id'] = r4010_ideopsaude.id
                    
                    try:
                        r4010_inforeemb_dados['tpinsc'] = infoReemb.tpInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_inforeemb_dados['nrinsc'] = infoReemb.nrInsc.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_inforeemb_dados['vlrreemb'] = infoReemb.vlrReemb.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_inforeemb_dados['vlrreembant'] = infoReemb.vlrReembAnt.cdata
                    except AttributeError: 
                        pass
            
                    r4010_inforeemb = r4010infoReemb.objects.create(**r4010_inforeemb_dados)
            
            if 'infoDependPl' in dir(ideOpSaude):
            
                for infoDependPl in ideOpSaude.infoDependPl:
            
                    r4010_infodependpl_dados = {}
                    r4010_infodependpl_dados['r4010_ideopsaude_id'] = r4010_ideopsaude.id
                    
                    try:
                        r4010_infodependpl_dados['cpf'] = infoDependPl.cpf.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infodependpl_dados['dtnascto'] = infoDependPl.dtNascto.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infodependpl_dados['nome'] = infoDependPl.nome.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infodependpl_dados['reldep'] = infoDependPl.relDep.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4010_infodependpl_dados['vlrsaude'] = infoDependPl.vlrSaude.cdata
                    except AttributeError: 
                        pass
            
                    r4010_infodependpl = r4010infoDependPl.objects.create(**r4010_infodependpl_dados)
                    
                    if 'infoReembDep' in dir(infoDependPl):
                    
                        for infoReembDep in infoDependPl.infoReembDep:
                    
                            r4010_inforeembdep_dados = {}
                            r4010_inforeembdep_dados['r4010_infodependpl_id'] = r4010_infodependpl.id
                            
                            try:
                                r4010_inforeembdep_dados['tpinsc'] = infoReembDep.tpInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforeembdep_dados['nrinsc'] = infoReembDep.nrInsc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforeembdep_dados['vlrreemb'] = infoReembDep.vlrReemb.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4010_inforeembdep_dados['vlrreembant'] = infoReembDep.vlrReembAnt.cdata
                            except AttributeError: 
                                pass
                    
                            r4010_inforeembdep = r4010infoReembDep.objects.create(**r4010_inforeembdep_dados)    
    r4010_evtretpf_dados['evento'] = 'r4010'
    r4010_evtretpf_dados['id'] = r4010_evtretpf.id
    r4010_evtretpf_dados['identidade_evento'] = doc.Reinf.evtRetPF['id']
    r4010_evtretpf_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r4010_evtretpf_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r4010_evtretpf.id)
    
    return r4010_evtretpf_dados