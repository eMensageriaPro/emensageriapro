#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4010.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r4010_evtretpf_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r4010evtRetPF.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r4010_evtretpf_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4010_evtretpf_dados = {}
    r4010_evtretpf_dados['status'] = status
    r4010_evtretpf_dados['arquivo_original'] = 1
    if arquivo:
        r4010_evtretpf_dados['arquivo'] = arquivo.arquivo
    r4010_evtretpf_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4010_evtretpf_dados['identidade'] = doc.Reinf.evtRetPF['id']
    evtRetPF = doc.Reinf.evtRetPF

    try:
        r4010_evtretpf_dados['indretif'] = read_from_xml(evtRetPF.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['nrrecibo'] = read_from_xml(evtRetPF.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['perapur'] = read_from_xml(evtRetPF.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['tpamb'] = read_from_xml(evtRetPF.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['procemi'] = read_from_xml(evtRetPF.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['verproc'] = read_from_xml(evtRetPF.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['tpinsc'] = read_from_xml(evtRetPF.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['nrinsc'] = read_from_xml(evtRetPF.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['tpinscestab'] = read_from_xml(evtRetPF.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['nrinscestab'] = read_from_xml(evtRetPF.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['cpfbenef'] = read_from_xml(evtRetPF.ideEstab.ideBenef.cpfBenef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4010_evtretpf_dados['nmbenef'] = read_from_xml(evtRetPF.ideEstab.ideBenef.nmBenef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r4010_evtretpf = r4010evtRetPF.objects.create(**r4010_evtretpf_dados)

    if 'ideEstab' in dir(evtRetPF) and 'ideBenef' in dir(evtRetPF.ideEstab) and 'idePgto' in dir(evtRetPF.ideEstab.ideBenef):

        for idePgto in evtRetPF.ideEstab.ideBenef.idePgto:

            r4010_idepgto_dados = {}
            r4010_idepgto_dados['r4010_evtretpf_id'] = r4010_evtretpf.id

            try:
                r4010_idepgto_dados['natrend'] = read_from_xml(idePgto.natRend.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4010_idepgto_dados['paisresid'] = read_from_xml(idePgto.paisResid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4010_idepgto_dados['observ'] = read_from_xml(idePgto.observ.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r4010_idepgto = r4010idePgto.objects.create(**r4010_idepgto_dados)

            if 'infoPgto' in dir(idePgto):

                for infoPgto in idePgto.infoPgto:

                    r4010_infopgto_dados = {}
                    r4010_infopgto_dados['r4010_idepgto_id'] = r4010_idepgto.id

                    try:
                        r4010_infopgto_dados['dtfg'] = read_from_xml(infoPgto.dtFG.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['inddecterc'] = read_from_xml(infoPgto.indDecTerc.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrrendbruto'] = read_from_xml(infoPgto.vlrRendBruto.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrrendtrib'] = read_from_xml(infoPgto.vlrRendTrib.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrir'] = read_from_xml(infoPgto.vlrIR.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrrendsusp'] = read_from_xml(infoPgto.vlrRendSusp.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrnir'] = read_from_xml(infoPgto.vlrNIR.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrdeposito'] = read_from_xml(infoPgto.vlrDeposito.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrcompanocalend'] = read_from_xml(infoPgto.vlrCompAnoCalend.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgto_dados['vlrcompanoant'] = read_from_xml(infoPgto.vlrCompAnoAnt.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r4010_infopgto = r4010infoPgto.objects.create(**r4010_infopgto_dados)

                    if 'FCI' in dir(infoPgto):

                        for FCI in infoPgto.FCI:

                            r4010_fci_dados = {}
                            r4010_fci_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_fci_dados['nrinscfci'] = read_from_xml(FCI.nrInscFCI.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass

                            r4010_fci = r4010FCI.objects.create(**r4010_fci_dados)

                    if 'SCP' in dir(infoPgto):

                        for SCP in infoPgto.SCP:

                            r4010_scp_dados = {}
                            r4010_scp_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_scp_dados['nrinscscp'] = read_from_xml(SCP.nrInscSCP.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_scp_dados['percscp'] = read_from_xml(SCP.percSCP.cdata, 'efdreinf', 'N', 4)
                            except AttributeError:
                                pass

                            r4010_scp = r4010SCP.objects.create(**r4010_scp_dados)

                    if 'detDed' in dir(infoPgto):

                        for detDed in infoPgto.detDed:

                            r4010_detded_dados = {}
                            r4010_detded_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_detded_dados['indtpdeducao'] = read_from_xml(detDed.indTpDeducao.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_detded_dados['vlrdeducao'] = read_from_xml(detDed.vlrDeducao.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_detded_dados['vlrdedsusp'] = read_from_xml(detDed.vlrDedSusp.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_detded_dados['nrinscprevcomp'] = read_from_xml(detDed.nrInscPrevComp.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass

                            r4010_detded = r4010detDed.objects.create(**r4010_detded_dados)
        
                            if 'benefPen' in dir(detDed):
        
                                for benefPen in detDed.benefPen:
        
                                    r4010_benefpen_dados = {}
                                    r4010_benefpen_dados['r4010_detded_id'] = r4010_detded.id
                
                                    try:
                                        r4010_benefpen_dados['cpf'] = read_from_xml(benefPen.cpf.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4010_benefpen_dados['dtnascto'] = read_from_xml(benefPen.dtNascto.cdata, 'efdreinf', 'D', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4010_benefpen_dados['nome'] = read_from_xml(benefPen.nome.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4010_benefpen_dados['reldep'] = read_from_xml(benefPen.relDep.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4010_benefpen_dados['descrdep'] = read_from_xml(benefPen.descrDep.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    r4010_benefpen = r4010benefPen.objects.create(**r4010_benefpen_dados)

                    if 'rendIsento' in dir(infoPgto):

                        for rendIsento in infoPgto.rendIsento:

                            r4010_rendisento_dados = {}
                            r4010_rendisento_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_rendisento_dados['tpisencao'] = read_from_xml(rendIsento.tpIsencao.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_rendisento_dados['vlrisento'] = read_from_xml(rendIsento.vlrIsento.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_rendisento_dados['descrendimento'] = read_from_xml(rendIsento.descRendimento.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_rendisento_dados['dtlaudo'] = read_from_xml(rendIsento.dtLaudo.cdata, 'efdreinf', 'D', None)
                            except AttributeError:
                                pass

                            r4010_rendisento = r4010rendIsento.objects.create(**r4010_rendisento_dados)

                    if 'infoProcRet' in dir(infoPgto):

                        for infoProcRet in infoPgto.infoProcRet:

                            r4010_infoprocret_dados = {}
                            r4010_infoprocret_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_infoprocret_dados['tpprocret'] = read_from_xml(infoProcRet.tpProcRet.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_infoprocret_dados['nrprocret'] = read_from_xml(infoProcRet.nrProcRet.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_infoprocret_dados['codsusp'] = read_from_xml(infoProcRet.codSusp.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_infoprocret_dados['vlrnretido'] = read_from_xml(infoProcRet.vlrNRetido.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_infoprocret_dados['vlrdep'] = read_from_xml(infoProcRet.vlrDep.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4010_infoprocret = r4010infoProcRet.objects.create(**r4010_infoprocret_dados)

                    if 'infoRRA' in dir(infoPgto):

                        for infoRRA in infoPgto.infoRRA:

                            r4010_inforra_dados = {}
                            r4010_inforra_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_inforra_dados['tpprocrra'] = read_from_xml(infoRRA.tpProcRRA.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforra_dados['nrprocrra'] = read_from_xml(infoRRA.nrProcRRA.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforra_dados['indorigrec'] = read_from_xml(infoRRA.indOrigRec.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforra_dados['descrra'] = read_from_xml(infoRRA.descRRA.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforra_dados['qtdmesesrra'] = read_from_xml(infoRRA.qtdMesesRRA.cdata, 'efdreinf', 'N', 1)
                            except AttributeError:
                                pass

                            r4010_inforra = r4010infoRRA.objects.create(**r4010_inforra_dados)
        
                            if 'despProcJud' in dir(infoRRA):
        
                                for despProcJud in infoRRA.despProcJud:
        
                                    r4010_inforra_despprocjud_dados = {}
                                    r4010_inforra_despprocjud_dados['r4010_inforra_id'] = r4010_inforra.id
                
                                    try:
                                        r4010_inforra_despprocjud_dados['vlrdespcustas'] = read_from_xml(despProcJud.vlrDespCustas.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4010_inforra_despprocjud_dados['vlrdespadvogados'] = read_from_xml(despProcJud.vlrDespAdvogados.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r4010_inforra_despprocjud = r4010infoRRAdespProcJud.objects.create(**r4010_inforra_despprocjud_dados)
                
                                    if 'ideAdv' in dir(despProcJud):
                
                                        for ideAdv in despProcJud.ideAdv:
                
                                            r4010_inforra_ideadv_dados = {}
                                            r4010_inforra_ideadv_dados['r4010_inforra_despprocjud_id'] = r4010_inforra_despprocjud.id
                        
                                            try:
                                                r4010_inforra_ideadv_dados['tpinscadv'] = read_from_xml(ideAdv.tpInscAdv.cdata, 'efdreinf', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r4010_inforra_ideadv_dados['nrinscadv'] = read_from_xml(ideAdv.nrInscAdv.cdata, 'efdreinf', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r4010_inforra_ideadv_dados['vlradv'] = read_from_xml(ideAdv.vlrAdv.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            r4010_inforra_ideadv = r4010infoRRAideAdv.objects.create(**r4010_inforra_ideadv_dados)
        
                            if 'origemRec' in dir(infoRRA):
        
                                for origemRec in infoRRA.origemRec:
        
                                    r4010_inforra_origemrec_dados = {}
                                    r4010_inforra_origemrec_dados['r4010_inforra_id'] = r4010_inforra.id
                
                                    try:
                                        r4010_inforra_origemrec_dados['cnpjorigrecurso'] = read_from_xml(origemRec.cnpjOrigRecurso.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    r4010_inforra_origemrec = r4010infoRRAorigemRec.objects.create(**r4010_inforra_origemrec_dados)

                    if 'infoProcJud' in dir(infoPgto):

                        for infoProcJud in infoPgto.infoProcJud:

                            r4010_infoprocjud_dados = {}
                            r4010_infoprocjud_dados['r4010_infopgto_id'] = r4010_infopgto.id
        
                            try:
                                r4010_infoprocjud_dados['nrproc'] = read_from_xml(infoProcJud.nrProc.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_infoprocjud_dados['indorigrec'] = read_from_xml(infoProcJud.indOrigRec.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_infoprocjud_dados['desc'] = read_from_xml(infoProcJud.desc.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass

                            r4010_infoprocjud = r4010infoProcJud.objects.create(**r4010_infoprocjud_dados)
        
                            if 'despProcJud' in dir(infoProcJud):
        
                                for despProcJud in infoProcJud.despProcJud:
        
                                    r4010_infoprocjud_despprocjud_dados = {}
                                    r4010_infoprocjud_despprocjud_dados['r4010_infoprocjud_id'] = r4010_infoprocjud.id
                
                                    try:
                                        r4010_infoprocjud_despprocjud_dados['vlrdespcustas'] = read_from_xml(despProcJud.vlrDespCustas.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4010_infoprocjud_despprocjud_dados['vlrdespadvogados'] = read_from_xml(despProcJud.vlrDespAdvogados.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r4010_infoprocjud_despprocjud = r4010infoProcJuddespProcJud.objects.create(**r4010_infoprocjud_despprocjud_dados)
                
                                    if 'ideAdv' in dir(despProcJud):
                
                                        for ideAdv in despProcJud.ideAdv:
                
                                            r4010_infoprocjud_ideadv_dados = {}
                                            r4010_infoprocjud_ideadv_dados['r4010_infoprocjud_despprocjud_id'] = r4010_infoprocjud_despprocjud.id
                        
                                            try:
                                                r4010_infoprocjud_ideadv_dados['tpinscadv'] = read_from_xml(ideAdv.tpInscAdv.cdata, 'efdreinf', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r4010_infoprocjud_ideadv_dados['nrinscadv'] = read_from_xml(ideAdv.nrInscAdv.cdata, 'efdreinf', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r4010_infoprocjud_ideadv_dados['vlradv'] = read_from_xml(ideAdv.vlrAdv.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            r4010_infoprocjud_ideadv = r4010infoProcJudideAdv.objects.create(**r4010_infoprocjud_ideadv_dados)
        
                            if 'origemRec' in dir(infoProcJud):
        
                                for origemRec in infoProcJud.origemRec:
        
                                    r4010_infoprocjud_origemrec_dados = {}
                                    r4010_infoprocjud_origemrec_dados['r4010_infoprocjud_id'] = r4010_infoprocjud.id
                
                                    try:
                                        r4010_infoprocjud_origemrec_dados['cnpjorigrecurso'] = read_from_xml(origemRec.cnpjOrigRecurso.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    r4010_infoprocjud_origemrec = r4010infoProcJudorigemRec.objects.create(**r4010_infoprocjud_origemrec_dados)

            if 'infoPgtoExt' in dir(idePgto):

                for infoPgtoExt in idePgto.infoPgtoExt:

                    r4010_infopgtoext_dados = {}
                    r4010_infopgtoext_dados['r4010_idepgto_id'] = r4010_idepgto.id

                    try:
                        r4010_infopgtoext_dados['dsclograd'] = read_from_xml(infoPgtoExt.endExt.dscLograd.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['nrlograd'] = read_from_xml(infoPgtoExt.endExt.nrLograd.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['complem'] = read_from_xml(infoPgtoExt.endExt.complem.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['bairro'] = read_from_xml(infoPgtoExt.endExt.bairro.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['cidade'] = read_from_xml(infoPgtoExt.endExt.cidade.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['estado'] = read_from_xml(infoPgtoExt.endExt.estado.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['codpostal'] = read_from_xml(infoPgtoExt.endExt.codPostal.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['telef'] = read_from_xml(infoPgtoExt.endExt.telef.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['indnif'] = read_from_xml(infoPgtoExt.infoFiscal.indNIF.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['nifbenef'] = read_from_xml(infoPgtoExt.infoFiscal.nifBenef.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infopgtoext_dados['frmtribut'] = read_from_xml(infoPgtoExt.infoFiscal.frmTribut.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r4010_infopgtoext = r4010infoPgtoExt.objects.create(**r4010_infopgtoext_dados)

    if 'ideEstab' in dir(evtRetPF) and 'ideBenef' in dir(evtRetPF.ideEstab) and 'ideOpSaude' in dir(evtRetPF.ideEstab.ideBenef):

        for ideOpSaude in evtRetPF.ideEstab.ideBenef.ideOpSaude:

            r4010_ideopsaude_dados = {}
            r4010_ideopsaude_dados['r4010_evtretpf_id'] = r4010_evtretpf.id

            try:
                r4010_ideopsaude_dados['nrinsc'] = read_from_xml(ideOpSaude.nrInsc.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4010_ideopsaude_dados['regans'] = read_from_xml(ideOpSaude.regANS.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r4010_ideopsaude_dados['vlrsaude'] = read_from_xml(ideOpSaude.vlrSaude.cdata, 'efdreinf', 'N', 2)
            except AttributeError:
                pass

            r4010_ideopsaude = r4010ideOpSaude.objects.create(**r4010_ideopsaude_dados)

            if 'infoReemb' in dir(ideOpSaude):

                for infoReemb in ideOpSaude.infoReemb:

                    r4010_inforeemb_dados = {}
                    r4010_inforeemb_dados['r4010_ideopsaude_id'] = r4010_ideopsaude.id

                    try:
                        r4010_inforeemb_dados['tpinsc'] = read_from_xml(infoReemb.tpInsc.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_inforeemb_dados['nrinsc'] = read_from_xml(infoReemb.nrInsc.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_inforeemb_dados['vlrreemb'] = read_from_xml(infoReemb.vlrReemb.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4010_inforeemb_dados['vlrreembant'] = read_from_xml(infoReemb.vlrReembAnt.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r4010_inforeemb = r4010infoReemb.objects.create(**r4010_inforeemb_dados)

            if 'infoDependPl' in dir(ideOpSaude):

                for infoDependPl in ideOpSaude.infoDependPl:

                    r4010_infodependpl_dados = {}
                    r4010_infodependpl_dados['r4010_ideopsaude_id'] = r4010_ideopsaude.id

                    try:
                        r4010_infodependpl_dados['cpf'] = read_from_xml(infoDependPl.cpf.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infodependpl_dados['dtnascto'] = read_from_xml(infoDependPl.dtNascto.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infodependpl_dados['nome'] = read_from_xml(infoDependPl.nome.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infodependpl_dados['reldep'] = read_from_xml(infoDependPl.relDep.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r4010_infodependpl_dados['vlrsaude'] = read_from_xml(infoDependPl.vlrSaude.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r4010_infodependpl = r4010infoDependPl.objects.create(**r4010_infodependpl_dados)

                    if 'infoReembDep' in dir(infoDependPl):

                        for infoReembDep in infoDependPl.infoReembDep:

                            r4010_inforeembdep_dados = {}
                            r4010_inforeembdep_dados['r4010_infodependpl_id'] = r4010_infodependpl.id
        
                            try:
                                r4010_inforeembdep_dados['tpinsc'] = read_from_xml(infoReembDep.tpInsc.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforeembdep_dados['nrinsc'] = read_from_xml(infoReembDep.nrInsc.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforeembdep_dados['vlrreemb'] = read_from_xml(infoReembDep.vlrReemb.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4010_inforeembdep_dados['vlrreembant'] = read_from_xml(infoReembDep.vlrReembAnt.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4010_inforeembdep = r4010infoReembDep.objects.create(**r4010_inforeembdep_dados)
    r4010_evtretpf_dados['evento'] = 'r4010'
    r4010_evtretpf_dados['id'] = r4010_evtretpf.id
    r4010_evtretpf_dados['identidade_evento'] = doc.Reinf.evtRetPF['id']

    from emensageriapro.efdreinf.views.r4010_evtretpf_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r4010_evtretpf.id)

    return r4010_evtretpf_dados