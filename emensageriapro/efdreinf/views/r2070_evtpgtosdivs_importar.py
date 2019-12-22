# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2070.models import *
from emensageriapro.functions import read_from_xml



def read_r2070_evtpgtosdivs_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2070_evtpgtosdivs_obj(request, doc, status, validar)
    return dados



def read_r2070_evtpgtosdivs(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2070_evtpgtosdivs_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2070evtPgtosDivs.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2070_evtpgtosdivs_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2070_evtpgtosdivs_dados = {}
    r2070_evtpgtosdivs_dados['status'] = status
    r2070_evtpgtosdivs_dados['arquivo_original'] = 1
    if arquivo:
        r2070_evtpgtosdivs_dados['arquivo'] = arquivo.arquivo
    r2070_evtpgtosdivs_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2070_evtpgtosdivs_dados['identidade'] = doc.Reinf.evtPgtosDivs['id']
    evtPgtosDivs = doc.Reinf.evtPgtosDivs

    try:
        r2070_evtpgtosdivs_dados['indretif'] = read_from_xml(evtPgtosDivs.ideEvento.indRetif.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['nrrecibo'] = read_from_xml(evtPgtosDivs.ideEvento.nrRecibo.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['perapur'] = read_from_xml(evtPgtosDivs.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['tpamb'] = read_from_xml(evtPgtosDivs.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['procemi'] = read_from_xml(evtPgtosDivs.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['verproc'] = read_from_xml(evtPgtosDivs.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['tpinsc'] = read_from_xml(evtPgtosDivs.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['nrinsc'] = read_from_xml(evtPgtosDivs.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['codpgto'] = read_from_xml(evtPgtosDivs.ideBenef.codPgto.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['tpinscbenef'] = read_from_xml(evtPgtosDivs.ideBenef.tpInscBenef.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['nrinscbenef'] = read_from_xml(evtPgtosDivs.ideBenef.nrInscBenef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2070_evtpgtosdivs_dados['nmrazaobenef'] = read_from_xml(evtPgtosDivs.ideBenef.nmRazaoBenef.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r2070_evtpgtosdivs = r2070evtPgtosDivs.objects.create(**r2070_evtpgtosdivs_dados)

    if 'ideBenef' in dir(evtPgtosDivs) and 'infoResidExt' in dir(evtPgtosDivs.ideBenef):

        for infoResidExt in evtPgtosDivs.ideBenef.infoResidExt:

            r2070_inforesidext_dados = {}
            r2070_inforesidext_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs.id

            try:
                r2070_inforesidext_dados['paisresid'] = read_from_xml(infoResidExt.infoEnder.paisResid.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['dsclograd'] = read_from_xml(infoResidExt.infoEnder.dscLograd.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['nrlograd'] = read_from_xml(infoResidExt.infoEnder.nrLograd.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['complem'] = read_from_xml(infoResidExt.infoEnder.complem.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['bairro'] = read_from_xml(infoResidExt.infoEnder.bairro.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['cidade'] = read_from_xml(infoResidExt.infoEnder.cidade.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['codpostal'] = read_from_xml(infoResidExt.infoEnder.codPostal.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['indnif'] = read_from_xml(infoResidExt.infoFiscal.indNIF.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['nifbenef'] = read_from_xml(infoResidExt.infoFiscal.nifBenef.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2070_inforesidext_dados['relfontepagad'] = read_from_xml(infoResidExt.infoFiscal.relFontePagad.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r2070_inforesidext = r2070infoResidExt.objects.create(**r2070_inforesidext_dados)

    if 'ideBenef' in dir(evtPgtosDivs) and 'infoMolestia' in dir(evtPgtosDivs.ideBenef):

        for infoMolestia in evtPgtosDivs.ideBenef.infoMolestia:

            r2070_infomolestia_dados = {}
            r2070_infomolestia_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs.id

            try:
                r2070_infomolestia_dados['dtlaudo'] = read_from_xml(infoMolestia.dtLaudo.cdata, 'efdreinf', 'D', None)
            except AttributeError:
                pass

            r2070_infomolestia = r2070infoMolestia.objects.create(**r2070_infomolestia_dados)

    if 'ideBenef' in dir(evtPgtosDivs) and 'infoPgto' in dir(evtPgtosDivs.ideBenef) and 'ideEstab' in dir(evtPgtosDivs.ideBenef.infoPgto):

        for ideEstab in evtPgtosDivs.ideBenef.infoPgto.ideEstab:

            r2070_ideestab_dados = {}
            r2070_ideestab_dados['r2070_evtpgtosdivs_id'] = r2070_evtpgtosdivs.id

            try:
                r2070_ideestab_dados['tpinsc'] = read_from_xml(ideEstab.tpInsc.cdata, 'efdreinf', 'N', None)
            except AttributeError:
                pass

            try:
                r2070_ideestab_dados['nrinsc'] = read_from_xml(ideEstab.nrInsc.cdata, 'efdreinf', 'C', None)
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
                                r2070_pgtopf_dados['dtpgto'] = read_from_xml(pgtoPF.dtPgto.cdata, 'efdreinf', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                r2070_pgtopf_dados['indsuspexig'] = read_from_xml(pgtoPF.indSuspExig.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r2070_pgtopf_dados['inddecterceiro'] = read_from_xml(pgtoPF.indDecTerceiro.cdata, 'efdreinf', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                r2070_pgtopf_dados['vlrrendtributavel'] = read_from_xml(pgtoPF.vlrRendTributavel.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r2070_pgtopf_dados['vlrirrf'] = read_from_xml(pgtoPF.vlrIRRF.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r2070_pgtopf = r2070pgtoPF.objects.create(**r2070_pgtopf_dados)
        
                            if 'detDeducao' in dir(pgtoPF):
        
                                for detDeducao in pgtoPF.detDeducao:
        
                                    r2070_detdeducao_dados = {}
                                    r2070_detdeducao_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_detdeducao_dados['indtpdeducao'] = read_from_xml(detDeducao.indTpDeducao.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_detdeducao_dados['vlrdeducao'] = read_from_xml(detDeducao.vlrDeducao.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r2070_detdeducao = r2070detDeducao.objects.create(**r2070_detdeducao_dados)
        
                            if 'rendIsento' in dir(pgtoPF):
        
                                for rendIsento in pgtoPF.rendIsento:
        
                                    r2070_rendisento_dados = {}
                                    r2070_rendisento_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_rendisento_dados['tpisencao'] = read_from_xml(rendIsento.tpIsencao.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_rendisento_dados['vlrisento'] = read_from_xml(rendIsento.vlrIsento.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_rendisento_dados['descrendimento'] = read_from_xml(rendIsento.descRendimento.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
        
                                    r2070_rendisento = r2070rendIsento.objects.create(**r2070_rendisento_dados)
        
                            if 'detCompet' in dir(pgtoPF):
        
                                for detCompet in pgtoPF.detCompet:
        
                                    r2070_detcompet_dados = {}
                                    r2070_detcompet_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_detcompet_dados['indperreferencia'] = read_from_xml(detCompet.indPerReferencia.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_detcompet_dados['perrefpagto'] = read_from_xml(detCompet.perRefPagto.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_detcompet_dados['vlrrendtributavel'] = read_from_xml(detCompet.vlrRendTributavel.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r2070_detcompet = r2070detCompet.objects.create(**r2070_detcompet_dados)
        
                            if 'compJud' in dir(pgtoPF):
        
                                for compJud in pgtoPF.compJud:
        
                                    r2070_compjud_dados = {}
                                    r2070_compjud_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_compjud_dados['vlrcompanocalend'] = read_from_xml(compJud.vlrCompAnoCalend.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_compjud_dados['vlrcompanoant'] = read_from_xml(compJud.vlrCompAnoAnt.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r2070_compjud = r2070compJud.objects.create(**r2070_compjud_dados)
        
                            if 'infoRRA' in dir(pgtoPF):
        
                                for infoRRA in pgtoPF.infoRRA:
        
                                    r2070_inforra_dados = {}
                                    r2070_inforra_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_inforra_dados['tpprocrra'] = read_from_xml(infoRRA.tpProcRRA.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_inforra_dados['nrprocrra'] = read_from_xml(infoRRA.nrProcRRA.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_inforra_dados['codsusp'] = read_from_xml(infoRRA.codSusp.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_inforra_dados['natrra'] = read_from_xml(infoRRA.natRRA.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_inforra_dados['qtdmesesrra'] = read_from_xml(infoRRA.qtdMesesRRA.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    r2070_inforra = r2070infoRRA.objects.create(**r2070_inforra_dados)
                
                                    if 'despProcJud' in dir(infoRRA):
                
                                        for despProcJud in infoRRA.despProcJud:
                
                                            r2070_inforra_despprocjud_dados = {}
                                            r2070_inforra_despprocjud_dados['r2070_inforra_id'] = r2070_inforra.id
                        
                                            try:
                                                r2070_inforra_despprocjud_dados['vlrdespcustas'] = read_from_xml(despProcJud.vlrDespCustas.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r2070_inforra_despprocjud_dados['vlrdespadvogados'] = read_from_xml(despProcJud.vlrDespAdvogados.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            r2070_inforra_despprocjud = r2070infoRRAdespProcJud.objects.create(**r2070_inforra_despprocjud_dados)
                        
                                            if 'ideAdvogado' in dir(despProcJud):
                        
                                                for ideAdvogado in despProcJud.ideAdvogado:
                        
                                                    r2070_inforra_ideadvogado_dados = {}
                                                    r2070_inforra_ideadvogado_dados['r2070_inforra_despprocjud_id'] = r2070_inforra_despprocjud.id
                                
                                                    try:
                                                        r2070_inforra_ideadvogado_dados['tpinscadvogado'] = read_from_xml(ideAdvogado.tpInscAdvogado.cdata, 'efdreinf', 'N', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        r2070_inforra_ideadvogado_dados['nrinscadvogado'] = read_from_xml(ideAdvogado.nrInscAdvogado.cdata, 'efdreinf', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        r2070_inforra_ideadvogado_dados['vlradvogado'] = read_from_xml(ideAdvogado.vlrAdvogado.cdata, 'efdreinf', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    r2070_inforra_ideadvogado = r2070infoRRAideAdvogado.objects.create(**r2070_inforra_ideadvogado_dados)
        
                            if 'infoProcJud' in dir(pgtoPF):
        
                                for infoProcJud in pgtoPF.infoProcJud:
        
                                    r2070_infoprocjud_dados = {}
                                    r2070_infoprocjud_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_infoprocjud_dados['nrprocjud'] = read_from_xml(infoProcJud.nrProcJud.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_infoprocjud_dados['codsusp'] = read_from_xml(infoProcJud.codSusp.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_infoprocjud_dados['indorigemrecursos'] = read_from_xml(infoProcJud.indOrigemRecursos.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    r2070_infoprocjud = r2070infoProcJud.objects.create(**r2070_infoprocjud_dados)
                
                                    if 'despProcJud' in dir(infoProcJud):
                
                                        for despProcJud in infoProcJud.despProcJud:
                
                                            r2070_infoprocjud_despprocjud_dados = {}
                                            r2070_infoprocjud_despprocjud_dados['r2070_infoprocjud_id'] = r2070_infoprocjud.id
                        
                                            try:
                                                r2070_infoprocjud_despprocjud_dados['vlrdespcustas'] = read_from_xml(despProcJud.vlrDespCustas.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r2070_infoprocjud_despprocjud_dados['vlrdespadvogados'] = read_from_xml(despProcJud.vlrDespAdvogados.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            r2070_infoprocjud_despprocjud = r2070infoProcJuddespProcJud.objects.create(**r2070_infoprocjud_despprocjud_dados)
                        
                                            if 'ideAdvogado' in dir(despProcJud):
                        
                                                for ideAdvogado in despProcJud.ideAdvogado:
                        
                                                    r2070_infoprocjud_ideadvogado_dados = {}
                                                    r2070_infoprocjud_ideadvogado_dados['r2070_infoprocjud_despprocjud_id'] = r2070_infoprocjud_despprocjud.id
                                
                                                    try:
                                                        r2070_infoprocjud_ideadvogado_dados['tpinscadvogado'] = read_from_xml(ideAdvogado.tpInscAdvogado.cdata, 'efdreinf', 'N', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        r2070_infoprocjud_ideadvogado_dados['nrinscadvogado'] = read_from_xml(ideAdvogado.nrInscAdvogado.cdata, 'efdreinf', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        r2070_infoprocjud_ideadvogado_dados['vlradvogado'] = read_from_xml(ideAdvogado.vlrAdvogado.cdata, 'efdreinf', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    r2070_infoprocjud_ideadvogado = r2070infoProcJudideAdvogado.objects.create(**r2070_infoprocjud_ideadvogado_dados)
                
                                    if 'origemRecursos' in dir(infoProcJud):
                
                                        for origemRecursos in infoProcJud.origemRecursos:
                
                                            r2070_infoprocjud_origemrecursos_dados = {}
                                            r2070_infoprocjud_origemrecursos_dados['r2070_infoprocjud_id'] = r2070_infoprocjud.id
                        
                                            try:
                                                r2070_infoprocjud_origemrecursos_dados['cnpjorigemrecursos'] = read_from_xml(origemRecursos.cnpjOrigemRecursos.cdata, 'efdreinf', 'C', None)
                                            except AttributeError:
                                                pass
                
                                            r2070_infoprocjud_origemrecursos = r2070infoProcJudorigemRecursos.objects.create(**r2070_infoprocjud_origemrecursos_dados)
        
                            if 'depJudicial' in dir(pgtoPF):
        
                                for depJudicial in pgtoPF.depJudicial:
        
                                    r2070_depjudicial_dados = {}
                                    r2070_depjudicial_dados['r2070_pgtopf_id'] = r2070_pgtopf.id
                
                                    try:
                                        r2070_depjudicial_dados['vlrdepjudicial'] = read_from_xml(depJudicial.vlrDepJudicial.cdata, 'efdreinf', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    r2070_depjudicial = r2070depJudicial.objects.create(**r2070_depjudicial_dados)

                    if 'pgtoPJ' in dir(pgtoResidBR):

                        for pgtoPJ in pgtoResidBR.pgtoPJ:

                            r2070_pgtopj_dados = {}
                            r2070_pgtopj_dados['r2070_pgtoresidbr_id'] = r2070_pgtoresidbr.id
        
                            try:
                                r2070_pgtopj_dados['dtpagto'] = read_from_xml(pgtoPJ.dtPagto.cdata, 'efdreinf', 'D', None)
                            except AttributeError:
                                pass
        
                            try:
                                r2070_pgtopj_dados['vlrrendtributavel'] = read_from_xml(pgtoPJ.vlrRendTributavel.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                r2070_pgtopj_dados['vlrret'] = read_from_xml(pgtoPJ.vlrRet.cdata, 'efdreinf', 'N', 2)
                            except AttributeError:
                                pass

                            r2070_pgtopj = r2070pgtoPJ.objects.create(**r2070_pgtopj_dados)
        
                            if 'infoProcJud' in dir(pgtoPJ):
        
                                for infoProcJud in pgtoPJ.infoProcJud:
        
                                    r2070_pgtopj_infoprocjud_dados = {}
                                    r2070_pgtopj_infoprocjud_dados['r2070_pgtopj_id'] = r2070_pgtopj.id
                
                                    try:
                                        r2070_pgtopj_infoprocjud_dados['nrprocjud'] = read_from_xml(infoProcJud.nrProcJud.cdata, 'efdreinf', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_pgtopj_infoprocjud_dados['codsusp'] = read_from_xml(infoProcJud.codSusp.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        r2070_pgtopj_infoprocjud_dados['indorigemrecursos'] = read_from_xml(infoProcJud.indOrigemRecursos.cdata, 'efdreinf', 'N', None)
                                    except AttributeError:
                                        pass
        
                                    r2070_pgtopj_infoprocjud = r2070pgtoPJinfoProcJud.objects.create(**r2070_pgtopj_infoprocjud_dados)
                
                                    if 'despProcJud' in dir(infoProcJud):
                
                                        for despProcJud in infoProcJud.despProcJud:
                
                                            r2070_pgtopj_despprocjud_dados = {}
                                            r2070_pgtopj_despprocjud_dados['r2070_pgtopj_infoprocjud_id'] = r2070_pgtopj_infoprocjud.id
                        
                                            try:
                                                r2070_pgtopj_despprocjud_dados['vlrdespcustas'] = read_from_xml(despProcJud.vlrDespCustas.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                        
                                            try:
                                                r2070_pgtopj_despprocjud_dados['vlrdespadvogados'] = read_from_xml(despProcJud.vlrDespAdvogados.cdata, 'efdreinf', 'N', 2)
                                            except AttributeError:
                                                pass
                
                                            r2070_pgtopj_despprocjud = r2070pgtoPJdespProcJud.objects.create(**r2070_pgtopj_despprocjud_dados)
                        
                                            if 'ideAdvogado' in dir(despProcJud):
                        
                                                for ideAdvogado in despProcJud.ideAdvogado:
                        
                                                    r2070_pgtopj_ideadvogado_dados = {}
                                                    r2070_pgtopj_ideadvogado_dados['r2070_pgtopj_despprocjud_id'] = r2070_pgtopj_despprocjud.id
                                
                                                    try:
                                                        r2070_pgtopj_ideadvogado_dados['tpinscadvogado'] = read_from_xml(ideAdvogado.tpInscAdvogado.cdata, 'efdreinf', 'N', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        r2070_pgtopj_ideadvogado_dados['nrinscadvogado'] = read_from_xml(ideAdvogado.nrInscAdvogado.cdata, 'efdreinf', 'C', None)
                                                    except AttributeError:
                                                        pass
                                
                                                    try:
                                                        r2070_pgtopj_ideadvogado_dados['vlradvogado'] = read_from_xml(ideAdvogado.vlrAdvogado.cdata, 'efdreinf', 'N', 2)
                                                    except AttributeError:
                                                        pass
                        
                                                    r2070_pgtopj_ideadvogado = r2070pgtoPJideAdvogado.objects.create(**r2070_pgtopj_ideadvogado_dados)
                
                                    if 'origemRecursos' in dir(infoProcJud):
                
                                        for origemRecursos in infoProcJud.origemRecursos:
                
                                            r2070_pgtopj_origemrecursos_dados = {}
                                            r2070_pgtopj_origemrecursos_dados['r2070_pgtopj_infoprocjud_id'] = r2070_pgtopj_infoprocjud.id
                        
                                            try:
                                                r2070_pgtopj_origemrecursos_dados['cnpjorigemrecursos'] = read_from_xml(origemRecursos.cnpjOrigemRecursos.cdata, 'efdreinf', 'C', None)
                                            except AttributeError:
                                                pass
                
                                            r2070_pgtopj_origemrecursos = r2070pgtoPJorigemRecursos.objects.create(**r2070_pgtopj_origemrecursos_dados)

            if 'pgtoResidExt' in dir(ideEstab):

                for pgtoResidExt in ideEstab.pgtoResidExt:

                    r2070_pgtoresidext_dados = {}
                    r2070_pgtoresidext_dados['r2070_ideestab_id'] = r2070_ideestab.id

                    try:
                        r2070_pgtoresidext_dados['dtpagto'] = read_from_xml(pgtoResidExt.dtPagto.cdata, 'efdreinf', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        r2070_pgtoresidext_dados['tprendimento'] = read_from_xml(pgtoResidExt.tpRendimento.cdata, 'efdreinf', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        r2070_pgtoresidext_dados['formatributacao'] = read_from_xml(pgtoResidExt.formaTributacao.cdata, 'efdreinf', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        r2070_pgtoresidext_dados['vlrpgto'] = read_from_xml(pgtoResidExt.vlrPgto.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        r2070_pgtoresidext_dados['vlrret'] = read_from_xml(pgtoResidExt.vlrRet.cdata, 'efdreinf', 'N', 2)
                    except AttributeError:
                        pass

                    r2070_pgtoresidext = r2070pgtoResidExt.objects.create(**r2070_pgtoresidext_dados)
    r2070_evtpgtosdivs_dados['evento'] = 'r2070'
    r2070_evtpgtosdivs_dados['id'] = r2070_evtpgtosdivs.id
    r2070_evtpgtosdivs_dados['identidade_evento'] = doc.Reinf.evtPgtosDivs['id']

    from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2070_evtpgtosdivs.id)

    return r2070_evtpgtosdivs_dados