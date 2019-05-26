#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2070.models import *



def read_r2070_evtpgtosdivs_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2070_evtpgtosdivs_obj(doc, status, validar)
    return dados



def read_r2070_evtpgtosdivs(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2070_evtpgtosdivs_obj(doc, status, validar)
    return dados



def read_r2070_evtpgtosdivs_obj(doc, status, validar=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2070_evtpgtosdivs_dados = {}
    r2070_evtpgtosdivs_dados['status'] = status
    r2070_evtpgtosdivs_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2070_evtpgtosdivs_dados['identidade'] = doc.Reinf.evtPgtosDivs['id']
    evtPgtosDivs = doc.Reinf.evtPgtosDivs
    
    try:
        r2070_evtpgtosdivs_dados['indretif'] = evtPgtosDivs.ideEvento.indRetif.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['nrrecibo'] = evtPgtosDivs.ideEvento.nrRecibo.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['perapur'] = evtPgtosDivs.ideEvento.perApur.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['tpamb'] = evtPgtosDivs.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['procemi'] = evtPgtosDivs.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['verproc'] = evtPgtosDivs.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['tpinsc'] = evtPgtosDivs.ideContri.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['nrinsc'] = evtPgtosDivs.ideContri.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['codpgto'] = evtPgtosDivs.ideBenef.codPgto.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['tpinscbenef'] = evtPgtosDivs.ideBenef.tpInscBenef.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['nrinscbenef'] = evtPgtosDivs.ideBenef.nrInscBenef.cdata
    except AttributeError: 
        pass
    
    try:
        r2070_evtpgtosdivs_dados['nmrazaobenef'] = evtPgtosDivs.ideBenef.nmRazaoBenef.cdata
    except AttributeError: 
        pass
        
    r2070_evtpgtosdivs = r2070evtPgtosDivs.objects.create(**r2070_evtpgtosdivs_dados)
    
    if 'infoResidExt' in dir(evtPgtosDivs.ideBenef):
    
        for infoResidExt in evtPgtosDivs.ideBenef.infoResidExt:
    
            r2070_inforesidext_dados = {}
            r2070_inforesidext_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs.id
            
            try:
                r2070_inforesidext_dados['paisresid'] = infoResidExt.infoEnder.paisResid.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['dsclograd'] = infoResidExt.infoEnder.dscLograd.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['nrlograd'] = infoResidExt.infoEnder.nrLograd.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['complem'] = infoResidExt.infoEnder.complem.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['bairro'] = infoResidExt.infoEnder.bairro.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['cidade'] = infoResidExt.infoEnder.cidade.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['codpostal'] = infoResidExt.infoEnder.codPostal.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['indnif'] = infoResidExt.infoFiscal.indNIF.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['nifbenef'] = infoResidExt.infoFiscal.nifBenef.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_inforesidext_dados['relfontepagad'] = infoResidExt.infoFiscal.relFontePagad.cdata
            except AttributeError: 
                pass
    
            r2070_inforesidext = r2070infoResidExt.objects.create(**r2070_inforesidext_dados)
    
    if 'infoMolestia' in dir(evtPgtosDivs.ideBenef):
    
        for infoMolestia in evtPgtosDivs.ideBenef.infoMolestia:
    
            r2070_infomolestia_dados = {}
            r2070_infomolestia_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs.id
            
            try:
                r2070_infomolestia_dados['dtlaudo'] = infoMolestia.dtLaudo.cdata
            except AttributeError: 
                pass
    
            r2070_infomolestia = r2070infoMolestia.objects.create(**r2070_infomolestia_dados)
    
    if 'ideEstab' in dir(evtPgtosDivs.ideBenef.infoPgto):
    
        for ideEstab in evtPgtosDivs.ideBenef.infoPgto.ideEstab:
    
            r2070_ideestab_dados = {}
            r2070_ideestab_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs.id
            
            try:
                r2070_ideestab_dados['tpinsc'] = ideEstab.tpInsc.cdata
            except AttributeError: 
                pass
            
            try:
                r2070_ideestab_dados['nrinsc'] = ideEstab.nrInsc.cdata
            except AttributeError: 
                pass
    
            r2070_ideestab = r2070ideEstab.objects.create(**r2070_ideestab_dados)
            
            if 'pgtoResidBR' in dir(ideEstab):
            
                for pgtoResidBR in ideEstab.pgtoResidBR:
            
                    r2070_pgtoresidbr_dados = {}
                    r2070_pgtoresidbr_dados['r2070_ideestab_id'] = r2070_ideestab.id
            
                    r2070_pgtoresidbr = r2070pgtoResidBR.objects.create(**r2070_pgtoresidbr_dados)
                    
                    if 'pgtoPF' in dir(pgtoResidBR):
                    
                        for pgtoPF in pgtoResidBR.pgtoPF:
                    
                            r2070_pgtopf_dados = {}
                            r2070_pgtopf_dados['r2070_pgtoresidbr_id'] = r2070_pgtoresidbr.id
                            
                            try:
                                r2070_pgtopf_dados['dtpgto'] = pgtoPF.dtPgto.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r2070_pgtopf_dados['indsuspexig'] = pgtoPF.indSuspExig.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r2070_pgtopf_dados['inddecterceiro'] = pgtoPF.indDecTerceiro.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r2070_pgtopf_dados['vlrrendtributavel'] = pgtoPF.vlrRendTributavel.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r2070_pgtopf_dados['vlrirrf'] = pgtoPF.vlrIRRF.cdata
                            except AttributeError: 
                                pass
                    
                            r2070_pgtopf = r2070pgtoPF.objects.create(**r2070_pgtopf_dados)
                            
                            if 'detDeducao' in dir(pgtoPF):
                            
                                for detDeducao in pgtoPF.detDeducao:
                            
                                    r2070_detdeducao_dados = {}
                                    r2070_detdeducao_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_detdeducao_dados['indtpdeducao'] = detDeducao.indTpDeducao.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_detdeducao_dados['vlrdeducao'] = detDeducao.vlrDeducao.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_detdeducao = r2070detDeducao.objects.create(**r2070_detdeducao_dados)
                            
                            if 'rendIsento' in dir(pgtoPF):
                            
                                for rendIsento in pgtoPF.rendIsento:
                            
                                    r2070_rendisento_dados = {}
                                    r2070_rendisento_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_rendisento_dados['tpisencao'] = rendIsento.tpIsencao.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_rendisento_dados['vlrisento'] = rendIsento.vlrIsento.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_rendisento_dados['descrendimento'] = rendIsento.descRendimento.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_rendisento = r2070rendIsento.objects.create(**r2070_rendisento_dados)
                            
                            if 'detCompet' in dir(pgtoPF):
                            
                                for detCompet in pgtoPF.detCompet:
                            
                                    r2070_detcompet_dados = {}
                                    r2070_detcompet_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_detcompet_dados['indperreferencia'] = detCompet.indPerReferencia.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_detcompet_dados['perrefpagto'] = detCompet.perRefPagto.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_detcompet_dados['vlrrendtributavel'] = detCompet.vlrRendTributavel.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_detcompet = r2070detCompet.objects.create(**r2070_detcompet_dados)
                            
                            if 'compJud' in dir(pgtoPF):
                            
                                for compJud in pgtoPF.compJud:
                            
                                    r2070_compjud_dados = {}
                                    r2070_compjud_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_compjud_dados['vlrcompanocalend'] = compJud.vlrCompAnoCalend.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_compjud_dados['vlrcompanoant'] = compJud.vlrCompAnoAnt.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_compjud = r2070compJud.objects.create(**r2070_compjud_dados)
                            
                            if 'infoRRA' in dir(pgtoPF):
                            
                                for infoRRA in pgtoPF.infoRRA:
                            
                                    r2070_inforra_dados = {}
                                    r2070_inforra_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_inforra_dados['tpprocrra'] = infoRRA.tpProcRRA.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_inforra_dados['nrprocrra'] = infoRRA.nrProcRRA.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_inforra_dados['codsusp'] = infoRRA.codSusp.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_inforra_dados['natrra'] = infoRRA.natRRA.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_inforra_dados['qtdmesesrra'] = infoRRA.qtdMesesRRA.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_inforra = r2070infoRRA.objects.create(**r2070_inforra_dados)
                                    
                                    if 'despProcJud' in dir(infoRRA):
                                    
                                        for despProcJud in infoRRA.despProcJud:
                                    
                                            r2070_inforra_despprocjud_dados = {}
                                            r2070_inforra_despprocjud_dados['r2070_inforra_id'] = r2070_inforra.id
                                            
                                            try:
                                                r2070_inforra_despprocjud_dados['vlrdespcustas'] = despProcJud.vlrDespCustas.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r2070_inforra_despprocjud_dados['vlrdespadvogados'] = despProcJud.vlrDespAdvogados.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r2070_inforra_despprocjud = r2070infoRRAdespProcJud.objects.create(**r2070_inforra_despprocjud_dados)
                                            
                                            if 'ideAdvogado' in dir(despProcJud):
                                            
                                                for ideAdvogado in despProcJud.ideAdvogado:
                                            
                                                    r2070_inforra_ideadvogado_dados = {}
                                                    r2070_inforra_ideadvogado_dados['r2070_inforra_despprocjud_id'] = r2070_inforra_despprocjud.id
                                                    
                                                    try:
                                                        r2070_inforra_ideadvogado_dados['tpinscadvogado'] = ideAdvogado.tpInscAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        r2070_inforra_ideadvogado_dados['nrinscadvogado'] = ideAdvogado.nrInscAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        r2070_inforra_ideadvogado_dados['vlradvogado'] = ideAdvogado.vlrAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    r2070_inforra_ideadvogado = r2070infoRRAideAdvogado.objects.create(**r2070_inforra_ideadvogado_dados)
                            
                            if 'infoProcJud' in dir(pgtoPF):
                            
                                for infoProcJud in pgtoPF.infoProcJud:
                            
                                    r2070_infoprocjud_dados = {}
                                    r2070_infoprocjud_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_infoprocjud_dados['nrprocjud'] = infoProcJud.nrProcJud.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_infoprocjud_dados['codsusp'] = infoProcJud.codSusp.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_infoprocjud_dados['indorigemrecursos'] = infoProcJud.indOrigemRecursos.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_infoprocjud = r2070infoProcJud.objects.create(**r2070_infoprocjud_dados)
                                    
                                    if 'despProcJud' in dir(infoProcJud):
                                    
                                        for despProcJud in infoProcJud.despProcJud:
                                    
                                            r2070_infoprocjud_despprocjud_dados = {}
                                            r2070_infoprocjud_despprocjud_dados['r2070_infoprocjud_id'] = r2070_infoprocjud.id
                                            
                                            try:
                                                r2070_infoprocjud_despprocjud_dados['vlrdespcustas'] = despProcJud.vlrDespCustas.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r2070_infoprocjud_despprocjud_dados['vlrdespadvogados'] = despProcJud.vlrDespAdvogados.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r2070_infoprocjud_despprocjud = r2070infoProcJuddespProcJud.objects.create(**r2070_infoprocjud_despprocjud_dados)
                                            
                                            if 'ideAdvogado' in dir(despProcJud):
                                            
                                                for ideAdvogado in despProcJud.ideAdvogado:
                                            
                                                    r2070_infoprocjud_ideadvogado_dados = {}
                                                    r2070_infoprocjud_ideadvogado_dados['r2070_infoprocjud_despprocjud_id'] = r2070_infoprocjud_despprocjud.id
                                                    
                                                    try:
                                                        r2070_infoprocjud_ideadvogado_dados['tpinscadvogado'] = ideAdvogado.tpInscAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        r2070_infoprocjud_ideadvogado_dados['nrinscadvogado'] = ideAdvogado.nrInscAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        r2070_infoprocjud_ideadvogado_dados['vlradvogado'] = ideAdvogado.vlrAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    r2070_infoprocjud_ideadvogado = r2070infoProcJudideAdvogado.objects.create(**r2070_infoprocjud_ideadvogado_dados)
                                    
                                    if 'origemRecursos' in dir(infoProcJud):
                                    
                                        for origemRecursos in infoProcJud.origemRecursos:
                                    
                                            r2070_infoprocjud_origemrecursos_dados = {}
                                            r2070_infoprocjud_origemrecursos_dados['r2070_infoprocjud_id'] = r2070_infoprocjud.id
                                            
                                            try:
                                                r2070_infoprocjud_origemrecursos_dados['cnpjorigemrecursos'] = origemRecursos.cnpjOrigemRecursos.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r2070_infoprocjud_origemrecursos = r2070infoProcJudorigemRecursos.objects.create(**r2070_infoprocjud_origemrecursos_dados)
                            
                            if 'depJudicial' in dir(pgtoPF):
                            
                                for depJudicial in pgtoPF.depJudicial:
                            
                                    r2070_depjudicial_dados = {}
                                    r2070_depjudicial_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                                    
                                    try:
                                        r2070_depjudicial_dados['vlrdepjudicial'] = depJudicial.vlrDepJudicial.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_depjudicial = r2070depJudicial.objects.create(**r2070_depjudicial_dados)
                    
                    if 'pgtoPJ' in dir(pgtoResidBR):
                    
                        for pgtoPJ in pgtoResidBR.pgtoPJ:
                    
                            r2070_pgtopj_dados = {}
                            r2070_pgtopj_dados['r2070_pgtoresidbr_id'] = r2070_pgtoresidbr.id
                            
                            try:
                                r2070_pgtopj_dados['dtpagto'] = pgtoPJ.dtPagto.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r2070_pgtopj_dados['vlrrendtributavel'] = pgtoPJ.vlrRendTributavel.cdata
                            except AttributeError: 
                                pass
                            
                            try:
                                r2070_pgtopj_dados['vlrret'] = pgtoPJ.vlrRet.cdata
                            except AttributeError: 
                                pass
                    
                            r2070_pgtopj = r2070pgtoPJ.objects.create(**r2070_pgtopj_dados)
                            
                            if 'infoProcJud' in dir(pgtoPJ):
                            
                                for infoProcJud in pgtoPJ.infoProcJud:
                            
                                    r2070_pgtopj_infoprocjud_dados = {}
                                    r2070_pgtopj_infoprocjud_dados['r2070_pgtopj_id'] = r2070_pgtopj.id
                                    
                                    try:
                                        r2070_pgtopj_infoprocjud_dados['nrprocjud'] = infoProcJud.nrProcJud.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_pgtopj_infoprocjud_dados['codsusp'] = infoProcJud.codSusp.cdata
                                    except AttributeError: 
                                        pass
                                    
                                    try:
                                        r2070_pgtopj_infoprocjud_dados['indorigemrecursos'] = infoProcJud.indOrigemRecursos.cdata
                                    except AttributeError: 
                                        pass
                            
                                    r2070_pgtopj_infoprocjud = r2070pgtoPJinfoProcJud.objects.create(**r2070_pgtopj_infoprocjud_dados)
                                    
                                    if 'despProcJud' in dir(infoProcJud):
                                    
                                        for despProcJud in infoProcJud.despProcJud:
                                    
                                            r2070_pgtopj_despprocjud_dados = {}
                                            r2070_pgtopj_despprocjud_dados['r2070_pgtopj_infoprocjud_id'] = r2070_pgtopj_infoprocjud.id
                                            
                                            try:
                                                r2070_pgtopj_despprocjud_dados['vlrdespcustas'] = despProcJud.vlrDespCustas.cdata
                                            except AttributeError: 
                                                pass
                                            
                                            try:
                                                r2070_pgtopj_despprocjud_dados['vlrdespadvogados'] = despProcJud.vlrDespAdvogados.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r2070_pgtopj_despprocjud = r2070pgtoPJdespProcJud.objects.create(**r2070_pgtopj_despprocjud_dados)
                                            
                                            if 'ideAdvogado' in dir(despProcJud):
                                            
                                                for ideAdvogado in despProcJud.ideAdvogado:
                                            
                                                    r2070_pgtopj_ideadvogado_dados = {}
                                                    r2070_pgtopj_ideadvogado_dados['r2070_pgtopj_despprocjud_id'] = r2070_pgtopj_despprocjud.id
                                                    
                                                    try:
                                                        r2070_pgtopj_ideadvogado_dados['tpinscadvogado'] = ideAdvogado.tpInscAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        r2070_pgtopj_ideadvogado_dados['nrinscadvogado'] = ideAdvogado.nrInscAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                                    
                                                    try:
                                                        r2070_pgtopj_ideadvogado_dados['vlradvogado'] = ideAdvogado.vlrAdvogado.cdata
                                                    except AttributeError: 
                                                        pass
                                            
                                                    r2070_pgtopj_ideadvogado = r2070pgtoPJideAdvogado.objects.create(**r2070_pgtopj_ideadvogado_dados)
                                    
                                    if 'origemRecursos' in dir(infoProcJud):
                                    
                                        for origemRecursos in infoProcJud.origemRecursos:
                                    
                                            r2070_pgtopj_origemrecursos_dados = {}
                                            r2070_pgtopj_origemrecursos_dados['r2070_pgtopj_infoprocjud_id'] = r2070_pgtopj_infoprocjud.id
                                            
                                            try:
                                                r2070_pgtopj_origemrecursos_dados['cnpjorigemrecursos'] = origemRecursos.cnpjOrigemRecursos.cdata
                                            except AttributeError: 
                                                pass
                                    
                                            r2070_pgtopj_origemrecursos = r2070pgtoPJorigemRecursos.objects.create(**r2070_pgtopj_origemrecursos_dados)
            
            if 'pgtoResidExt' in dir(ideEstab):
            
                for pgtoResidExt in ideEstab.pgtoResidExt:
            
                    r2070_pgtoresidext_dados = {}
                    r2070_pgtoresidext_dados['r2070_ideestab_id'] = r2070_ideestab.id
                    
                    try:
                        r2070_pgtoresidext_dados['dtpagto'] = pgtoResidExt.dtPagto.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2070_pgtoresidext_dados['tprendimento'] = pgtoResidExt.tpRendimento.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2070_pgtoresidext_dados['formatributacao'] = pgtoResidExt.formaTributacao.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2070_pgtoresidext_dados['vlrpgto'] = pgtoResidExt.vlrPgto.cdata
                    except AttributeError: 
                        pass
                    
                    try:
                        r2070_pgtoresidext_dados['vlrret'] = pgtoResidExt.vlrRet.cdata
                    except AttributeError: 
                        pass
            
                    r2070_pgtoresidext = r2070pgtoResidExt.objects.create(**r2070_pgtoresidext_dados)    
    r2070_evtpgtosdivs_dados['evento'] = 'r2070'
    r2070_evtpgtosdivs_dados['id'] = r2070_evtpgtosdivs.id
    r2070_evtpgtosdivs_dados['identidade_evento'] = doc.Reinf.evtPgtosDivs['id']
    r2070_evtpgtosdivs_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(r2070_evtpgtosdivs.id)
    return r2070_evtpgtosdivs_dados