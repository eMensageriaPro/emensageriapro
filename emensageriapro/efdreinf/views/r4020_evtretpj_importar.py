#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4020.models import *



def read_r4020_evtretpj_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4020_evtretpj_obj(request, doc, status, validar)
    return dados



def read_r4020_evtretpj(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r4020_evtretpj_obj(request, doc, status, validar)

    r4020evtRetPJ.objects.filter(id=dados['id']).update(arquivo=arquivo)
    ImportacaoArquivosEventos.objects.filter(arquivo=arquivo).update(versao=dados['versao'])

    return dados



def read_r4020_evtretpj_obj(request, doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4020_evtretpj_dados = {}
    r4020_evtretpj_dados['status'] = status
    r4020_evtretpj_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4020_evtretpj_dados['identidade'] = doc.Reinf.evtRetPJ['id']
    evtRetPJ = doc.Reinf.evtRetPJ
    
    try:
        r4020_evtretpj_dados['indretif'] = evtRetPJ.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['nrrecibo'] = evtRetPJ.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['perapur'] = evtRetPJ.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['tpamb'] = evtRetPJ.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['procemi'] = evtRetPJ.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['verproc'] = evtRetPJ.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['tpinsc'] = evtRetPJ.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['nrinsc'] = evtRetPJ.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['tpinscestab'] = evtRetPJ.ideEstab.tpInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['nrinscestab'] = evtRetPJ.ideEstab.nrInscEstab.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['cnpjbenef'] = evtRetPJ.ideEstab.ideBenef.cnpjBenef.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['nmbenef'] = evtRetPJ.ideEstab.ideBenef.nmBenef.cdata
    except AttributeError: 
        pass
    
    try:
        r4020_evtretpj_dados['isenimun'] = evtRetPJ.ideEstab.ideBenef.isenImun.cdata
    except AttributeError: 
        pass
        
    r4020_evtretpj = r4020evtRetPJ.objects.create(**r4020_evtretpj_dados)
    
    if 'ideEstab' in dir(evtRetPJ) and 'ideBenef' in dir(evtRetPJ.ideEstab) and 'idePgto' in dir(evtRetPJ.ideEstab.ideBenef):
    
        for idePgto in evtRetPJ.ideEstab.ideBenef.idePgto:
    
            r4020_idepgto_dados = {}
            r4020_idepgto_dados['r4020_evtretpj_id'] = r4020_evtretpj.id
            
            try:
                r4020_idepgto_dados['natrend'] = idePgto.natRend.cdata
            except AttributeError: 
                pass
            
            try:
                r4020_idepgto_dados['paisresid'] = idePgto.paisResid.cdata
            except AttributeError: 
                pass
            
            try:
                r4020_idepgto_dados['observ'] = idePgto.observ.cdata
            except AttributeError: 
                pass
    
            r4020_idepgto = r4020idePgto.objects.create(**r4020_idepgto_dados)
            
            if 'infoPgto' in dir(idePgto):
            
                for infoPgto in idePgto.infoPgto:
            
                    r4020_infopgto_dados = {}
                    r4020_infopgto_dados['r4020_idepgto_id'] = r4020_idepgto.id
                    
                    try:
                        r4020_infopgto_dados['dtfg'] = infoPgto.dtFG.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgto_dados['vlrtotalpag'] = infoPgto.vlrTotalPag.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgto_dados['vlrtotalcred'] = infoPgto.vlrTotalCred.cdata.replace('.', '').replace(',', '.')
                    except AttributeError: 
                        pass
            
                    r4020_infopgto = r4020infoPgto.objects.create(**r4020_infopgto_dados)
                    
                    if 'IR' in dir(infoPgto):
                    
                        for IR in infoPgto.IR:
                    
                            r4020_ir_dados = {}
                            r4020_ir_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_ir_dados['vlrbaseir'] = IR.vlrBaseIR.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_ir_dados['vlrir'] = IR.vlrIR.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_ir_dados['vlrbasenir'] = IR.vlrBaseNIR.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_ir_dados['vlrnir'] = IR.vlrNIR.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_ir_dados['vlrdepir'] = IR.vlrDepIR.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                    
                            r4020_ir = r4020IR.objects.create(**r4020_ir_dados)
                    
                    if 'CSLL' in dir(infoPgto):
                    
                        for CSLL in infoPgto.CSLL:
                    
                            r4020_csll_dados = {}
                            r4020_csll_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_csll_dados['vlrbasecsll'] = CSLL.vlrBaseCSLL.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_csll_dados['vlrcsll'] = CSLL.vlrCSLL.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_csll_dados['vlrbasencsll'] = CSLL.vlrBaseNCSLL.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_csll_dados['vlrncsll'] = CSLL.vlrNCSLL.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_csll_dados['vlrdepcsll'] = CSLL.vlrDepCSLL.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                    
                            r4020_csll = r4020CSLL.objects.create(**r4020_csll_dados)
                    
                    if 'Cofins' in dir(infoPgto):
                    
                        for Cofins in infoPgto.Cofins:
                    
                            r4020_cofins_dados = {}
                            r4020_cofins_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_cofins_dados['vlrbasecofins'] = Cofins.vlrBaseCofins.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_cofins_dados['vlrcofins'] = Cofins.vlrCofins.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_cofins_dados['vlrbasencofins'] = Cofins.vlrBaseNCofins.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_cofins_dados['vlrncofins'] = Cofins.vlrNCofins.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_cofins_dados['vlrdepcofins'] = Cofins.vlrDepCofins.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                    
                            r4020_cofins = r4020Cofins.objects.create(**r4020_cofins_dados)
                    
                    if 'PP' in dir(infoPgto):
                    
                        for PP in infoPgto.PP:
                    
                            r4020_pp_dados = {}
                            r4020_pp_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_pp_dados['vlrbasepp'] = PP.vlrBasePP.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_pp_dados['vlrpp'] = PP.vlrPP.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_pp_dados['vlrbasenpp'] = PP.vlrBaseNPP.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_pp_dados['vlrnpp'] = PP.vlrNPP.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_pp_dados['vlrdeppp'] = PP.vlrDepPP.cdata.replace('.', '').replace(',', '.')
                            except AttributeError: 
                                pass
                    
                            r4020_pp = r4020PP.objects.create(**r4020_pp_dados)
                    
                    if 'FCI' in dir(infoPgto):
                    
                        for FCI in infoPgto.FCI:
                    
                            r4020_fci_dados = {}
                            r4020_fci_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_fci_dados['nrinscfci'] = FCI.nrInscFCI.cdata
                            except AttributeError: 
                                pass
                    
                            r4020_fci = r4020FCI.objects.create(**r4020_fci_dados)
                    
                    if 'SCP' in dir(infoPgto):
                    
                        for SCP in infoPgto.SCP:
                    
                            r4020_scp_dados = {}
                            r4020_scp_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_scp_dados['nrinscscp'] = SCP.nrInscSCP.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_scp_dados['percscp'] = SCP.percSCP.cdata
                            except AttributeError: 
                                pass
                    
                            r4020_scp = r4020SCP.objects.create(**r4020_scp_dados)
                    
                    if 'infoProcRet' in dir(infoPgto):
                    
                        for infoProcRet in infoPgto.infoProcRet:
                    
                            r4020_infoprocret_dados = {}
                            r4020_infoprocret_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_infoprocret_dados['tpprocret'] = infoProcRet.tpProcRet.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['nrprocret'] = infoProcRet.nrProcRet.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['codsusp'] = infoProcRet.codSusp.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['nir'] = infoProcRet.nIR.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['depir'] = infoProcRet.depIR.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['ncsll'] = infoProcRet.nCSLL.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['depcsll'] = infoProcRet.depCSLL.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['ncofins'] = infoProcRet.nCofins.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['depcofins'] = infoProcRet.depCofins.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['npp'] = infoProcRet.nPP.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocret_dados['deppp'] = infoProcRet.depPP.cdata
                            except AttributeError: 
                                pass
                    
                            r4020_infoprocret = r4020infoProcRet.objects.create(**r4020_infoprocret_dados)
                    
                    if 'infoProcJud' in dir(infoPgto):
                    
                        for infoProcJud in infoPgto.infoProcJud:
                    
                            r4020_infoprocjud_dados = {}
                            r4020_infoprocjud_dados['r4020_infopgto_id'] = r4020_infopgto.id
                            
                            try:
                                r4020_infoprocjud_dados['nrproc'] = infoProcJud.nrProc.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocjud_dados['indorigemrecursos'] = infoProcJud.indOrigemRecursos.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r4020_infoprocjud_dados['desc'] = infoProcJud.desc.cdata
                            except AttributeError: 
                                pass
                    
                            r4020_infoprocjud = r4020infoProcJud.objects.create(**r4020_infoprocjud_dados)
                            
                            if 'despProcJud' in dir(infoProcJud):
                            
                                for despProcJud in infoProcJud.despProcJud:
                            
                                    r4020_despprocjud_dados = {}
                                    r4020_despprocjud_dados['r4020_infoprocjud_id'] = r4020_infoprocjud.id
                                    
                                    try:
                                        r4020_despprocjud_dados['vlrdespcustas'] = despProcJud.vlrDespCustas.cdata.replace('.', '').replace(',', '.')
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r4020_despprocjud_dados['vlrdespadvogados'] = despProcJud.vlrDespAdvogados.cdata.replace('.', '').replace(',', '.')
                                    except AttributeError: 
                                        pass
                            
                                    r4020_despprocjud = r4020despProcJud.objects.create(**r4020_despprocjud_dados)
                                    
                                    if 'ideAdv' in dir(despProcJud):
                                    
                                        for ideAdv in despProcJud.ideAdv:
                                    
                                            r4020_ideadv_dados = {}
                                            r4020_ideadv_dados['r4020_despprocjud_id'] = r4020_despprocjud.id
                                            
                                            try:
                                                r4020_ideadv_dados['tpinscadv'] = ideAdv.tpInscAdv.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r4020_ideadv_dados['nrinscadv'] = ideAdv.nrInscAdv.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r4020_ideadv_dados['vlradv'] = ideAdv.vlrAdv.cdata.replace('.', '').replace(',', '.')
                                            except AttributeError: 
                                                pass
                                    
                                            r4020_ideadv = r4020ideAdv.objects.create(**r4020_ideadv_dados)
                            
                            if 'origemRec' in dir(infoProcJud):
                            
                                for origemRec in infoProcJud.origemRec:
                            
                                    r4020_origemrec_dados = {}
                                    r4020_origemrec_dados['r4020_infoprocjud_id'] = r4020_infoprocjud.id
                                    
                                    try:
                                        r4020_origemrec_dados['cnpjorigrecurso'] = origemRec.cnpjOrigRecurso.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r4020_origemrec = r4020origemRec.objects.create(**r4020_origemrec_dados)
            
            if 'infoPgtoExt' in dir(idePgto):
            
                for infoPgtoExt in idePgto.infoPgtoExt:
            
                    r4020_infopgtoext_dados = {}
                    r4020_infopgtoext_dados['r4020_idepgto_id'] = r4020_idepgto.id
                    
                    try:
                        r4020_infopgtoext_dados['dsclograd'] = infoPgtoExt.endExt.dscLograd.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['nrlograd'] = infoPgtoExt.endExt.nrLograd.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['complem'] = infoPgtoExt.endExt.complem.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['bairro'] = infoPgtoExt.endExt.bairro.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['cidade'] = infoPgtoExt.endExt.cidade.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['estado'] = infoPgtoExt.endExt.estado.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['codpostal'] = infoPgtoExt.endExt.codPostal.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['telef'] = infoPgtoExt.endExt.telef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['indnif'] = infoPgtoExt.infoFiscal.indNIF.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['nifbenef'] = infoPgtoExt.infoFiscal.nifBenef.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['relfontpg'] = infoPgtoExt.infoFiscal.relFontPg.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r4020_infopgtoext_dados['frmtribut'] = infoPgtoExt.infoFiscal.frmTribut.cdata
                    except AttributeError: 
                        pass
            
                    r4020_infopgtoext = r4020infoPgtoExt.objects.create(**r4020_infopgtoext_dados)    
    r4020_evtretpj_dados['evento'] = 'r4020'
    r4020_evtretpj_dados['id'] = r4020_evtretpj.id
    r4020_evtretpj_dados['identidade_evento'] = doc.Reinf.evtRetPJ['id']
    r4020_evtretpj_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r4020_evtretpj_validar_evento import validar_evento_funcao
    
    if validar:
        validar_evento_funcao(request, r4020_evtretpj.id)
    
    return r4020_evtretpj_dados