# eMensageriaAI #
#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1210.models import *
from emensageriapro.functions import read_from_xml



def read_s1210_evtpgtos_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1210_evtpgtos_obj(request, doc, status, validar)
    return dados



def read_s1210_evtpgtos(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1210_evtpgtos_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1210evtPgtos.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1210_evtpgtos_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1210_evtpgtos_dados = {}
    s1210_evtpgtos_dados['status'] = status
    s1210_evtpgtos_dados['arquivo_original'] = 1
    if arquivo:
        s1210_evtpgtos_dados['arquivo'] = arquivo.arquivo
    s1210_evtpgtos_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1210_evtpgtos_dados['identidade'] = doc.eSocial.evtPgtos['Id']
    evtPgtos = doc.eSocial.evtPgtos

    try:
        s1210_evtpgtos_dados['indretif'] = read_from_xml(evtPgtos.ideEvento.indRetif.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['nrrecibo'] = read_from_xml(evtPgtos.ideEvento.nrRecibo.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['indapuracao'] = read_from_xml(evtPgtos.ideEvento.indApuracao.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['perapur'] = read_from_xml(evtPgtos.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['tpamb'] = read_from_xml(evtPgtos.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['procemi'] = read_from_xml(evtPgtos.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['verproc'] = read_from_xml(evtPgtos.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['tpinsc'] = read_from_xml(evtPgtos.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['nrinsc'] = read_from_xml(evtPgtos.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1210_evtpgtos_dados['cpfbenef'] = read_from_xml(evtPgtos.ideBenef.cpfBenef.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1210_evtpgtos = s1210evtPgtos.objects.create(**s1210_evtpgtos_dados)

    if 'ideBenef' in dir(evtPgtos) and 'deps' in dir(evtPgtos.ideBenef):

        for deps in evtPgtos.ideBenef.deps:

            s1210_deps_dados = {}
            s1210_deps_dados['s1210_evtpgtos_id'] = s1210_evtpgtos.id

            try:
                s1210_deps_dados['vrdeddep'] = read_from_xml(deps.vrDedDep.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s1210_deps = s1210deps.objects.create(**s1210_deps_dados)

    if 'ideBenef' in dir(evtPgtos) and 'infoPgto' in dir(evtPgtos.ideBenef):

        for infoPgto in evtPgtos.ideBenef.infoPgto:

            s1210_infopgto_dados = {}
            s1210_infopgto_dados['s1210_evtpgtos_id'] = s1210_evtpgtos.id

            try:
                s1210_infopgto_dados['dtpgto'] = read_from_xml(infoPgto.dtPgto.cdata, 'esocial', 'D', None)
            except AttributeError:
                pass

            try:
                s1210_infopgto_dados['tppgto'] = read_from_xml(infoPgto.tpPgto.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1210_infopgto_dados['indresbr'] = read_from_xml(infoPgto.indResBr.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1210_infopgto = s1210infoPgto.objects.create(**s1210_infopgto_dados)

            if 'detPgtoFl' in dir(infoPgto):

                for detPgtoFl in infoPgto.detPgtoFl:

                    s1210_detpgtofl_dados = {}
                    s1210_detpgtofl_dados['s1210_infopgto_id'] = s1210_infopgto.id

                    try:
                        s1210_detpgtofl_dados['perref'] = read_from_xml(detPgtoFl.perRef.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofl_dados['idedmdev'] = read_from_xml(detPgtoFl.ideDmDev.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofl_dados['indpgtott'] = read_from_xml(detPgtoFl.indPgtoTt.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofl_dados['vrliq'] = read_from_xml(detPgtoFl.vrLiq.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofl_dados['nrrecarq'] = read_from_xml(detPgtoFl.nrRecArq.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1210_detpgtofl = s1210detPgtoFl.objects.create(**s1210_detpgtofl_dados)

                    if 'retPgtoTot' in dir(detPgtoFl):

                        for retPgtoTot in detPgtoFl.retPgtoTot:

                            s1210_detpgtofl_retpgtotot_dados = {}
                            s1210_detpgtofl_retpgtotot_dados['s1210_detpgtofl_id'] = s1210_detpgtofl.id
        
                            try:
                                s1210_detpgtofl_retpgtotot_dados['codrubr'] = read_from_xml(retPgtoTot.codRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_retpgtotot_dados['idetabrubr'] = read_from_xml(retPgtoTot.ideTabRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_retpgtotot_dados['qtdrubr'] = read_from_xml(retPgtoTot.qtdRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_retpgtotot_dados['fatorrubr'] = read_from_xml(retPgtoTot.fatorRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_retpgtotot_dados['vrunit'] = read_from_xml(retPgtoTot.vrUnit.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_retpgtotot_dados['vrrubr'] = read_from_xml(retPgtoTot.vrRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1210_detpgtofl_retpgtotot = s1210detPgtoFlretPgtoTot.objects.create(**s1210_detpgtofl_retpgtotot_dados)
        
                            if 'penAlim' in dir(retPgtoTot):
        
                                for penAlim in retPgtoTot.penAlim:
        
                                    s1210_detpgtofl_penalim_dados = {}
                                    s1210_detpgtofl_penalim_dados['s1210_detpgtofl_retpgtotot_id'] = s1210_detpgtofl_retpgtotot.id
                
                                    try:
                                        s1210_detpgtofl_penalim_dados['cpfbenef'] = read_from_xml(penAlim.cpfBenef.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1210_detpgtofl_penalim_dados['dtnasctobenef'] = read_from_xml(penAlim.dtNasctoBenef.cdata, 'esocial', 'D', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1210_detpgtofl_penalim_dados['nmbenefic'] = read_from_xml(penAlim.nmBenefic.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1210_detpgtofl_penalim_dados['vlrpensao'] = read_from_xml(penAlim.vlrPensao.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s1210_detpgtofl_penalim = s1210detPgtoFlpenAlim.objects.create(**s1210_detpgtofl_penalim_dados)

                    if 'infoPgtoParc' in dir(detPgtoFl):

                        for infoPgtoParc in detPgtoFl.infoPgtoParc:

                            s1210_detpgtofl_infopgtoparc_dados = {}
                            s1210_detpgtofl_infopgtoparc_dados['s1210_detpgtofl_id'] = s1210_detpgtofl.id
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['matricula'] = read_from_xml(infoPgtoParc.matricula.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['codrubr'] = read_from_xml(infoPgtoParc.codRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['idetabrubr'] = read_from_xml(infoPgtoParc.ideTabRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['qtdrubr'] = read_from_xml(infoPgtoParc.qtdRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['fatorrubr'] = read_from_xml(infoPgtoParc.fatorRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['vrunit'] = read_from_xml(infoPgtoParc.vrUnit.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofl_infopgtoparc_dados['vrrubr'] = read_from_xml(infoPgtoParc.vrRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1210_detpgtofl_infopgtoparc = s1210detPgtoFlinfoPgtoParc.objects.create(**s1210_detpgtofl_infopgtoparc_dados)

            if 'detPgtoBenPr' in dir(infoPgto):

                for detPgtoBenPr in infoPgto.detPgtoBenPr:

                    s1210_detpgtobenpr_dados = {}
                    s1210_detpgtobenpr_dados['s1210_infopgto_id'] = s1210_infopgto.id

                    try:
                        s1210_detpgtobenpr_dados['perref'] = read_from_xml(detPgtoBenPr.perRef.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtobenpr_dados['idedmdev'] = read_from_xml(detPgtoBenPr.ideDmDev.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtobenpr_dados['indpgtott'] = read_from_xml(detPgtoBenPr.indPgtoTt.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtobenpr_dados['vrliq'] = read_from_xml(detPgtoBenPr.vrLiq.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s1210_detpgtobenpr = s1210detPgtoBenPr.objects.create(**s1210_detpgtobenpr_dados)

                    if 'retPgtoTot' in dir(detPgtoBenPr):

                        for retPgtoTot in detPgtoBenPr.retPgtoTot:

                            s1210_detpgtobenpr_retpgtotot_dados = {}
                            s1210_detpgtobenpr_retpgtotot_dados['s1210_detpgtobenpr_id'] = s1210_detpgtobenpr.id
        
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['codrubr'] = read_from_xml(retPgtoTot.codRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['idetabrubr'] = read_from_xml(retPgtoTot.ideTabRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['qtdrubr'] = read_from_xml(retPgtoTot.qtdRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['fatorrubr'] = read_from_xml(retPgtoTot.fatorRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['vrunit'] = read_from_xml(retPgtoTot.vrUnit.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_retpgtotot_dados['vrrubr'] = read_from_xml(retPgtoTot.vrRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1210_detpgtobenpr_retpgtotot = s1210detPgtoBenPrretPgtoTot.objects.create(**s1210_detpgtobenpr_retpgtotot_dados)

                    if 'infoPgtoParc' in dir(detPgtoBenPr):

                        for infoPgtoParc in detPgtoBenPr.infoPgtoParc:

                            s1210_detpgtobenpr_infopgtoparc_dados = {}
                            s1210_detpgtobenpr_infopgtoparc_dados['s1210_detpgtobenpr_id'] = s1210_detpgtobenpr.id
        
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['codrubr'] = read_from_xml(infoPgtoParc.codRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['idetabrubr'] = read_from_xml(infoPgtoParc.ideTabRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['qtdrubr'] = read_from_xml(infoPgtoParc.qtdRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['fatorrubr'] = read_from_xml(infoPgtoParc.fatorRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['vrunit'] = read_from_xml(infoPgtoParc.vrUnit.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtobenpr_infopgtoparc_dados['vrrubr'] = read_from_xml(infoPgtoParc.vrRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1210_detpgtobenpr_infopgtoparc = s1210detPgtoBenPrinfoPgtoParc.objects.create(**s1210_detpgtobenpr_infopgtoparc_dados)

            if 'detPgtoFer' in dir(infoPgto):

                for detPgtoFer in infoPgto.detPgtoFer:

                    s1210_detpgtofer_dados = {}
                    s1210_detpgtofer_dados['s1210_infopgto_id'] = s1210_infopgto.id

                    try:
                        s1210_detpgtofer_dados['codcateg'] = read_from_xml(detPgtoFer.codCateg.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofer_dados['matricula'] = read_from_xml(detPgtoFer.matricula.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofer_dados['dtinigoz'] = read_from_xml(detPgtoFer.dtIniGoz.cdata, 'esocial', 'D', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofer_dados['qtdias'] = read_from_xml(detPgtoFer.qtDias.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_detpgtofer_dados['vrliq'] = read_from_xml(detPgtoFer.vrLiq.cdata, 'esocial', 'N', 2)
                    except AttributeError:
                        pass

                    s1210_detpgtofer = s1210detPgtoFer.objects.create(**s1210_detpgtofer_dados)

                    if 'detRubrFer' in dir(detPgtoFer):

                        for detRubrFer in detPgtoFer.detRubrFer:

                            s1210_detpgtofer_detrubrfer_dados = {}
                            s1210_detpgtofer_detrubrfer_dados['s1210_detpgtofer_id'] = s1210_detpgtofer.id
        
                            try:
                                s1210_detpgtofer_detrubrfer_dados['codrubr'] = read_from_xml(detRubrFer.codRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofer_detrubrfer_dados['idetabrubr'] = read_from_xml(detRubrFer.ideTabRubr.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofer_detrubrfer_dados['qtdrubr'] = read_from_xml(detRubrFer.qtdRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofer_detrubrfer_dados['fatorrubr'] = read_from_xml(detRubrFer.fatorRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofer_detrubrfer_dados['vrunit'] = read_from_xml(detRubrFer.vrUnit.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtofer_detrubrfer_dados['vrrubr'] = read_from_xml(detRubrFer.vrRubr.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1210_detpgtofer_detrubrfer = s1210detPgtoFerdetRubrFer.objects.create(**s1210_detpgtofer_detrubrfer_dados)
        
                            if 'penAlim' in dir(detRubrFer):
        
                                for penAlim in detRubrFer.penAlim:
        
                                    s1210_detpgtofer_penalim_dados = {}
                                    s1210_detpgtofer_penalim_dados['s1210_detpgtofer_detrubrfer_id'] = s1210_detpgtofer_detrubrfer.id
                
                                    try:
                                        s1210_detpgtofer_penalim_dados['cpfbenef'] = read_from_xml(penAlim.cpfBenef.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1210_detpgtofer_penalim_dados['dtnasctobenef'] = read_from_xml(penAlim.dtNasctoBenef.cdata, 'esocial', 'D', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1210_detpgtofer_penalim_dados['nmbenefic'] = read_from_xml(penAlim.nmBenefic.cdata, 'esocial', 'C', None)
                                    except AttributeError:
                                        pass
                
                                    try:
                                        s1210_detpgtofer_penalim_dados['vlrpensao'] = read_from_xml(penAlim.vlrPensao.cdata, 'esocial', 'N', 2)
                                    except AttributeError:
                                        pass
        
                                    s1210_detpgtofer_penalim = s1210detPgtoFerpenAlim.objects.create(**s1210_detpgtofer_penalim_dados)

            if 'detPgtoAnt' in dir(infoPgto):

                for detPgtoAnt in infoPgto.detPgtoAnt:

                    s1210_detpgtoant_dados = {}
                    s1210_detpgtoant_dados['s1210_infopgto_id'] = s1210_infopgto.id

                    try:
                        s1210_detpgtoant_dados['codcateg'] = read_from_xml(detPgtoAnt.codCateg.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    s1210_detpgtoant = s1210detPgtoAnt.objects.create(**s1210_detpgtoant_dados)

                    if 'infoPgtoAnt' in dir(detPgtoAnt):

                        for infoPgtoAnt in detPgtoAnt.infoPgtoAnt:

                            s1210_detpgtoant_infopgtoant_dados = {}
                            s1210_detpgtoant_infopgtoant_dados['s1210_detpgtoant_id'] = s1210_detpgtoant.id
        
                            try:
                                s1210_detpgtoant_infopgtoant_dados['tpbcirrf'] = read_from_xml(infoPgtoAnt.tpBcIRRF.cdata, 'esocial', 'C', None)
                            except AttributeError:
                                pass
        
                            try:
                                s1210_detpgtoant_infopgtoant_dados['vrbcirrf'] = read_from_xml(infoPgtoAnt.vrBcIRRF.cdata, 'esocial', 'N', 2)
                            except AttributeError:
                                pass

                            s1210_detpgtoant_infopgtoant = s1210detPgtoAntinfoPgtoAnt.objects.create(**s1210_detpgtoant_infopgtoant_dados)

            if 'idePgtoExt' in dir(infoPgto):

                for idePgtoExt in infoPgto.idePgtoExt:

                    s1210_idepgtoext_dados = {}
                    s1210_idepgtoext_dados['s1210_infopgto_id'] = s1210_infopgto.id

                    try:
                        s1210_idepgtoext_dados['codpais'] = read_from_xml(idePgtoExt.idePais.codPais.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['indnif'] = read_from_xml(idePgtoExt.idePais.indNIF.cdata, 'esocial', 'N', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['nifbenef'] = read_from_xml(idePgtoExt.idePais.nifBenef.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['dsclograd'] = read_from_xml(idePgtoExt.endExt.dscLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['nrlograd'] = read_from_xml(idePgtoExt.endExt.nrLograd.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['complem'] = read_from_xml(idePgtoExt.endExt.complem.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['bairro'] = read_from_xml(idePgtoExt.endExt.bairro.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['nmcid'] = read_from_xml(idePgtoExt.endExt.nmCid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1210_idepgtoext_dados['codpostal'] = read_from_xml(idePgtoExt.endExt.codPostal.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1210_idepgtoext = s1210idePgtoExt.objects.create(**s1210_idepgtoext_dados)
    s1210_evtpgtos_dados['evento'] = 's1210'
    s1210_evtpgtos_dados['id'] = s1210_evtpgtos.id
    s1210_evtpgtos_dados['identidade_evento'] = doc.eSocial.evtPgtos['Id']

    from emensageriapro.esocial.views.s1210_evtpgtos_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1210_evtpgtos.id)

    return s1210_evtpgtos_dados