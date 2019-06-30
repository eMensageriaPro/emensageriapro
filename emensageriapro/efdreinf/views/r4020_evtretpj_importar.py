#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r4020.models import *
from emensageriapro.functions import read_from_xml



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
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r4020_evtretpj_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r4020evtRetPJ.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r4020_evtretpj_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r4020_evtretpj_dados = {}
    r4020_evtretpj_dados['status'] = status
    r4020_evtretpj_dados['arquivo_original'] = 1
    if arquivo:
        r4020_evtretpj_dados['arquivo'] = arquivo.arquivo
    r4020_evtretpj_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r4020_evtretpj_dados['identidade'] = doc.Reinf.evtRetPJ['id']
    evtRetPJ = doc.Reinf.evtRetPJ

    try:
        r4020_evtretpj_dados['indretif'] = read_from_xml(evtRetPJ.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['nrrecibo'] = read_from_xml(evtRetPJ.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['perapur'] = read_from_xml(evtRetPJ.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['tpamb'] = read_from_xml(evtRetPJ.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['procemi'] = read_from_xml(evtRetPJ.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['verproc'] = read_from_xml(evtRetPJ.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['tpinsc'] = read_from_xml(evtRetPJ.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['nrinsc'] = read_from_xml(evtRetPJ.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['tpinscestab'] = read_from_xml(evtRetPJ.ideEstab.tpInscEstab.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['nrinscestab'] = read_from_xml(evtRetPJ.ideEstab.nrInscEstab.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['cnpjbenef'] = read_from_xml(evtRetPJ.ideEstab.ideBenef.cnpjBenef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['nmbenef'] = read_from_xml(evtRetPJ.ideEstab.ideBenef.nmBenef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r4020_evtretpj_dados['isenimun'] = read_from_xml(evtRetPJ.ideEstab.ideBenef.isenImun.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    r4020_evtretpj = r4020evtRetPJ.objects.create(**r4020_evtretpj_dados)

    if 'ideEstab' in dir(evtRetPJ) and 'ideBenef' in dir(evtRetPJ.ideEstab) and 'idePgto' in dir(evtRetPJ.ideEstab.ideBenef):

        for idePgto in evtRetPJ.ideEstab.ideBenef.idePgto:

            r4020_idepgto_dados = {}
            r4020_idepgto_dados['r4020_evtretpj_id'] = r4020_evtretpj.id

            try:
                r4020_idepgto_dados['natrend'] = read_from_xml(idePgto.natRend.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4020_idepgto_dados['paisresid'] = read_from_xml(idePgto.paisResid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r4020_idepgto_dados['observ'] = read_from_xml(idePgto.observ.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r4020_idepgto = r4020idePgto.objects.create(**r4020_idepgto_dados)

            if 'infoPgto' in dir(idePgto):

                for infoPgto in idePgto.infoPgto:

                    r4020_infopgto_dados = {}
                    r4020_infopgto_dados['r4020_idepgto_id'] = r4020_idepgto.id

                    try:
                        r4020_infopgto_dados['dtfg'] = read_from_xml(infoPgto.dtFG.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgto_dados['vlrtotalpag'] = read_from_xml(infoPgto.vlrTotalPag.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgto_dados['vlrtotalcred'] = read_from_xml(infoPgto.vlrTotalCred.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r4020_infopgto = r4020infoPgto.objects.create(**r4020_infopgto_dados)

                    if 'IR' in dir(infoPgto):

                        for IR in infoPgto.IR:

                            r4020_ir_dados = {}
                            r4020_ir_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_ir_dados['vlrbaseir'] = read_from_xml(IR.vlrBaseIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_ir_dados['vlrir'] = read_from_xml(IR.vlrIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_ir_dados['vlrbasenir'] = read_from_xml(IR.vlrBaseNIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_ir_dados['vlrnir'] = read_from_xml(IR.vlrNIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_ir_dados['vlrdepir'] = read_from_xml(IR.vlrDepIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4020_ir = r4020IR.objects.create(**r4020_ir_dados)

                    if 'CSLL' in dir(infoPgto):

                        for CSLL in infoPgto.CSLL:

                            r4020_csll_dados = {}
                            r4020_csll_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_csll_dados['vlrbasecsll'] = read_from_xml(CSLL.vlrBaseCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_csll_dados['vlrcsll'] = read_from_xml(CSLL.vlrCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_csll_dados['vlrbasencsll'] = read_from_xml(CSLL.vlrBaseNCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_csll_dados['vlrncsll'] = read_from_xml(CSLL.vlrNCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_csll_dados['vlrdepcsll'] = read_from_xml(CSLL.vlrDepCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4020_csll = r4020CSLL.objects.create(**r4020_csll_dados)

                    if 'Cofins' in dir(infoPgto):

                        for Cofins in infoPgto.Cofins:

                            r4020_cofins_dados = {}
                            r4020_cofins_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_cofins_dados['vlrbasecofins'] = read_from_xml(Cofins.vlrBaseCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_cofins_dados['vlrcofins'] = read_from_xml(Cofins.vlrCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_cofins_dados['vlrbasencofins'] = read_from_xml(Cofins.vlrBaseNCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_cofins_dados['vlrncofins'] = read_from_xml(Cofins.vlrNCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_cofins_dados['vlrdepcofins'] = read_from_xml(Cofins.vlrDepCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4020_cofins = r4020Cofins.objects.create(**r4020_cofins_dados)

                    if 'PP' in dir(infoPgto):

                        for PP in infoPgto.PP:

                            r4020_pp_dados = {}
                            r4020_pp_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_pp_dados['vlrbasepp'] = read_from_xml(PP.vlrBasePP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_pp_dados['vlrpp'] = read_from_xml(PP.vlrPP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_pp_dados['vlrbasenpp'] = read_from_xml(PP.vlrBaseNPP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_pp_dados['vlrnpp'] = read_from_xml(PP.vlrNPP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_pp_dados['vlrdeppp'] = read_from_xml(PP.vlrDepPP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4020_pp = r4020PP.objects.create(**r4020_pp_dados)

                    if 'FCI' in dir(infoPgto):

                        for FCI in infoPgto.FCI:

                            r4020_fci_dados = {}
                            r4020_fci_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_fci_dados['nrinscfci'] = read_from_xml(FCI.nrInscFCI.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass

                            r4020_fci = r4020FCI.objects.create(**r4020_fci_dados)

                    if 'SCP' in dir(infoPgto):

                        for SCP in infoPgto.SCP:

                            r4020_scp_dados = {}
                            r4020_scp_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_scp_dados['nrinscscp'] = read_from_xml(SCP.nrInscSCP.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_scp_dados['percscp'] = read_from_xml(SCP.percSCP.cdata, 'efdreinf', 'N', 4)
                            except AttributeError:
                                pass

                            r4020_scp = r4020SCP.objects.create(**r4020_scp_dados)

                    if 'infoProcRet' in dir(infoPgto):

                        for infoProcRet in infoPgto.infoProcRet:

                            r4020_infoprocret_dados = {}
                            r4020_infoprocret_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_infoprocret_dados['tpprocret'] = read_from_xml(infoProcRet.tpProcRet.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['nrprocret'] = read_from_xml(infoProcRet.nrProcRet.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['codsusp'] = read_from_xml(infoProcRet.codSusp.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['nir'] = read_from_xml(infoProcRet.nIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['depir'] = read_from_xml(infoProcRet.depIR.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['ncsll'] = read_from_xml(infoProcRet.nCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['depcsll'] = read_from_xml(infoProcRet.depCSLL.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['ncofins'] = read_from_xml(infoProcRet.nCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['depcofins'] = read_from_xml(infoProcRet.depCofins.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['npp'] = read_from_xml(infoProcRet.nPP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocret_dados['deppp'] = read_from_xml(infoProcRet.depPP.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r4020_infoprocret = r4020infoProcRet.objects.create(**r4020_infoprocret_dados)

                    if 'infoProcJud' in dir(infoPgto):

                        for infoProcJud in infoPgto.infoProcJud:

                            r4020_infoprocjud_dados = {}
                            r4020_infoprocjud_dados['r4020_infopgto_id'] = r4020_infopgto.id
        
                            try:
                                r4020_infoprocjud_dados['nrproc'] = read_from_xml(infoProcJud.nrProc.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocjud_dados['indorigemrecursos'] = read_from_xml(infoProcJud.indOrigemRecursos.cdata, 'efdreinf', 'N', None)
                            except AttributeError:
                                pass
        
                            try:
                                r4020_infoprocjud_dados['desc'] = read_from_xml(infoProcJud.desc.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass

                            r4020_infoprocjud = r4020infoProcJud.objects.create(**r4020_infoprocjud_dados)
        
                            if 'despProcJud' in dir(infoProcJud):
        
                                for despProcJud in infoProcJud.despProcJud:
        
                                    r4020_despprocjud_dados = {}
                                    r4020_despprocjud_dados['r4020_infoprocjud_id'] = r4020_infoprocjud.id
                
                                    try:
                                        r4020_despprocjud_dados['vlrdespcustas'] = read_from_xml(despProcJud.vlrDespCustas.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r4020_despprocjud_dados['vlrdespadvogados'] = read_from_xml(despProcJud.vlrDespAdvogados.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r4020_despprocjud = r4020despProcJud.objects.create(**r4020_despprocjud_dados)
                
                                    if 'ideAdv' in dir(despProcJud):
                
                                        for ideAdv in despProcJud.ideAdv:
                
                                            r4020_ideadv_dados = {}
                                            r4020_ideadv_dados['r4020_despprocjud_id'] = r4020_despprocjud.id
                        
                                            try:
                                                r4020_ideadv_dados['tpinscadv'] = read_from_xml(ideAdv.tpInscAdv.cdata, 'efdreinf', 'N', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r4020_ideadv_dados['nrinscadv'] = read_from_xml(ideAdv.nrInscAdv.cdata, 'efdreinf', 'C', None)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r4020_ideadv_dados['vlradv'] = read_from_xml(ideAdv.vlrAdv.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            r4020_ideadv = r4020ideAdv.objects.create(**r4020_ideadv_dados)
        
                            if 'origemRec' in dir(infoProcJud):
        
                                for origemRec in infoProcJud.origemRec:
        
                                    r4020_origemrec_dados = {}
                                    r4020_origemrec_dados['r4020_infoprocjud_id'] = r4020_infoprocjud.id
                
                                    try:
                                        r4020_origemrec_dados['cnpjorigrecurso'] = read_from_xml(origemRec.cnpjOrigRecurso.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    r4020_origemrec = r4020origemRec.objects.create(**r4020_origemrec_dados)

            if 'infoPgtoExt' in dir(idePgto):

                for infoPgtoExt in idePgto.infoPgtoExt:

                    r4020_infopgtoext_dados = {}
                    r4020_infopgtoext_dados['r4020_idepgto_id'] = r4020_idepgto.id

                    try:
                        r4020_infopgtoext_dados['dsclograd'] = read_from_xml(infoPgtoExt.endExt.dscLograd.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['nrlograd'] = read_from_xml(infoPgtoExt.endExt.nrLograd.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['complem'] = read_from_xml(infoPgtoExt.endExt.complem.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['bairro'] = read_from_xml(infoPgtoExt.endExt.bairro.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['cidade'] = read_from_xml(infoPgtoExt.endExt.cidade.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['estado'] = read_from_xml(infoPgtoExt.endExt.estado.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['codpostal'] = read_from_xml(infoPgtoExt.endExt.codPostal.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['telef'] = read_from_xml(infoPgtoExt.endExt.telef.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['indnif'] = read_from_xml(infoPgtoExt.infoFiscal.indNIF.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['nifbenef'] = read_from_xml(infoPgtoExt.infoFiscal.nifBenef.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['relfontpg'] = read_from_xml(infoPgtoExt.infoFiscal.relFontPg.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r4020_infopgtoext_dados['frmtribut'] = read_from_xml(infoPgtoExt.infoFiscal.frmTribut.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    r4020_infopgtoext = r4020infoPgtoExt.objects.create(**r4020_infopgtoext_dados)
    r4020_evtretpj_dados['evento'] = 'r4020'
    r4020_evtretpj_dados['id'] = r4020_evtretpj.id
    r4020_evtretpj_dados['identidade_evento'] = doc.Reinf.evtRetPJ['id']

    from emensageriapro.efdreinf.views.r4020_evtretpj_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r4020_evtretpj.id)

    return r4020_evtretpj_dados