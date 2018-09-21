#coding:utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

from emensageriapro.padrao import executar_sql


def r1000_enviados():
    db_slug='default'
    from emensageriapro.efdreinf.models import r1000evtInfoContri
    lista = r1000evtInfoContri.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ ]
    for a in lista:
        if a.status == 14:
            codigos_lista.append(a.nrinsc)
    return codigos_lista




def r1070_enviados():
    db_slug='default'
    from emensageriapro.r1070.models import r1070inclusao
    lista = r1070inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.r1070_evttabprocesso.status == 14:
            codigos_lista.append(a.nrproc)
    return codigos_lista



def s1000_enviados():
    db_slug='default'
    from emensageriapro.esocial.models import s1000evtInfoEmpregador
    lista = s1000evtInfoEmpregador.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = []
    for a in lista:
        if a.status == 14:
            codigos_lista.append(a.nrinsc)
    return codigos_lista




def s1005_estabelecimentos_enviados():
    db_slug='default'
    from emensageriapro.s1005.models import s1005inclusao
    lista = s1005inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1005_evttabestab.status == 14:
            codigos_lista.append(a.nrinsc)
    return codigos_lista



def s1010_rubricas_enviados():
    db_slug='default'
    from emensageriapro.s1010.models import s1010inclusao
    lista = s1010inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1010_evttabrubrica.status == 14:
            codigos_lista.append(a.codrubr)
    return codigos_lista




def s1020_lotacoes_enviados():
    db_slug='default'
    from emensageriapro.s1020.models import s1020inclusao
    lista = s1020inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1020_evttablotacao.status == 14:
            codigos_lista.append(a.codlotacao)
    return codigos_lista



def s1030_cargos_enviados():
    db_slug='default'
    from emensageriapro.s1030.models import s1030inclusao
    lista = s1030inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1030_evttabcargo.status == 14:
            codigos_lista.append(a.codcargo)
    return codigos_lista


def s1035_carreiras_enviados():
    db_slug='default'
    from emensageriapro.s1035.models import s1035inclusao
    lista = s1035inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1035_evttabcarreira.status == 14:
            codigos_lista.append(a.codcarreira)
    return codigos_lista




def s1040_funcoes_enviados():
    db_slug='default'
    from emensageriapro.s1040.models import s1040inclusao
    lista = s1040inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1040_evttabfuncao.status == 14:
            codigos_lista.append(a.codfuncao)
    return codigos_lista




def s1050_horarios_enviados():
    db_slug='default'
    from emensageriapro.s1050.models import s1050inclusao
    lista = s1050inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1050_evttabhortur.status == 14:
            codigos_lista.append(a.codhorcontrat)
    return codigos_lista




def s1060_ambientes_enviados():
    db_slug='default'
    from emensageriapro.s1060.models import s1060inclusao
    lista = s1060inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1060_evttabambiente.status == 14:
            codigos_lista.append(a.codamb)
    return codigos_lista




def s1070_processos_enviados():
    db_slug='default'
    from emensageriapro.s1070.models import s1070inclusao
    lista = s1070inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.s1070_evttabprocesso.status == 14:
            codigos_lista.append(a.nrproc)
    return codigos_lista




def s1080_operadores_enviados():
    db_slug='default'
    from emensageriapro.s1080.models import s1080inclusao
    lista = s1080inclusao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.r1000_evtinfocontri.status == 14:
            codigos_lista.append(a.cnpjopportuario)
    return codigos_lista



def s2200_enviados():
    db_slug='default'
    from emensageriapro.esocial.models import s2200evtAdmissao
    lista = s2200evtAdmissao.objects.using(db_slug).filter(excluido=False).all()
    codigos_lista = [ None ]
    for a in lista:
        if a.status == 14:
            codigos_lista.append(a.cpftrab)
    return codigos_lista






def validar_precedencia(tipo, tabela, tabela_id):
    from emensageriapro.esocial.models import s1000evtInfoEmpregador, s1005evtTabEstab, \
        s1010evtTabRubrica, s1020evtTabLotacao, s1030evtTabCargo, s1035evtTabCarreira, \
        s1040evtTabFuncao, s1050evtTabHorTur, s1060evtTabAmbiente, s1070evtTabProcesso, \
        s1080evtTabOperPort, s1200evtRemun, s1202evtRmnRPPS, s1207evtBenPrRP, \
        s1210evtPgtos, s1250evtAqProd, s1260evtComProd, s1270evtContratAvNP, \
        s1280evtInfoComplPer, s1295evtTotConting, s1298evtReabreEvPer, s1299evtFechaEvPer, \
        s1300evtContrSindPatr, s2190evtAdmPrelim, s2200evtAdmissao, s2205evtAltCadastral, \
        s2206evtAltContratual, s2210evtCAT, s2220evtMonit, s2230evtAfastTemp, s2240evtExpRisco, \
        s2241evtInsApo, s2250evtAvPrevio, s2260evtConvInterm, s2298evtReintegr, s2299evtDeslig, \
        s2300evtTSVInicio, s2306evtTSVAltContr, s2399evtTSVTermino, s2400evtCdBenefIn, s3000evtExclusao, \
        s5001evtBasesTrab, s5002evtIrrfBenef, s5011evtCS, s5012evtIrrf
    from emensageriapro.efdreinf.models import r1000evtInfoContri, r1070evtTabProcesso, r2010evtServTom, \
        r2020evtServPrest, r2030evtAssocDespRec, r2040evtAssocDespRep, r2050evtComProd, \
        r2060evtCPRB, r2070evtPgtosDivs, r2098evtReabreEvPer, r2099evtFechaEvPer, \
        r3010evtEspDesportivo, r5001evtTotal, r5011evtTotalContrib, r9000evtExclusao

    from emensageriapro.s3000.models import s3000ideFolhaPagto, s3000ideTrabalhador


    # tipo = eSocial ou Reinf
    db_slug = 'default'
    quant = 1
    
    if (tabela == 'r1070_evttabprocesso'):

        a = r1070evtTabProcesso.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 'r2010_evtservtom'):

        a = r2010evtServTom.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 'r2020_evtservprest'):

        a = r2020evtServPrest.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 'r2030_evtassocdesprec'):

        a = r2030evtAssocDespRec.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 'r2040_evtassocdesprep'):

        a = r2040evtAssocDespRep.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 'r2050_evtcomprod'):

        a = r2050evtComProd.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 'r2060_evtcprb'):

        a = r2060evtCPRB.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 'r2070_evtpgtosdivs'):

        a = r2070evtPgtosDivs.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 'r2098_evtreabreevper'):

        a = r2098evtReabreEvPer.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant

        a = r2098evtReabreEvPer.objects.using(db_slug).filter(id=tabela_id).all()
        b = r2099evtFechaEvPer.objects.using(db_slug).filter(perapur=a.perapur, status__in=[14])
        c = len(b)
        if not c:
            quant = 0 * quant

    elif (tabela == 'r3010_evtespdesportivo'):

        a = r3010evtEspDesportivo.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 'r9000_evtexclusao'):

        a = r9000evtExclusao.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=r1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1005_evttabestab'):

        a = s1005evtTabEstab.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados() ).all()
        c = len(a)
        if not c:
            quant = 0 * quant



    elif (tabela == 's1010_evttabrubrica'):

        a = s1010evtTabRubrica.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's1020_evttablotacao'):

        a = s1020evtTabLotacao.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1030_evttabcargo'):

        a = s1030evtTabCargo.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1035_evttabcarreira'):

        a = s1035evtTabCarreira.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1040_evttabfuncao'):

        a = s1040evtTabFuncao.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1050_evttabhortur'):

        a = s1050evtTabHorTur.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1060_evttabambiente'):

        a = s1060evtTabAmbiente.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's1070_evttabprocesso'):

        a = s1070evtTabProcesso.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's1080_evttaboperport'):

        a = s1080evtTabOperPort.objects.using(db_slug).filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2200_evtadmissao'):


        a = s2200evtAdmissao.objects.using(db_slug).filter(id=tabela_id,
                                                           nrinsc__in=s1000_enviados() ).all()

        c = len(a)
        if not c:
            quant = 0 * quant
        else:
            if a[0].codcargo:
                if a[0].codcargo not in s1030_cargos_enviados():
                    quant = 0 * quant
            if a[0].codcarreira:
                if a[0].codcarreira not in s1035_carreiras_enviados():
                    quant = 0 * quant
            if a[0].codfuncao:
                if a[0].codfuncao not in s1040_funcoes_enviados():
                    quant = 0 * quant



    elif (tabela == 's2205_evtaltcadastral'):

        a = s2205evtAltCadastral.objects.using(db_slug).filter(id=tabela_id,
                                                               cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2206_evtaltcontratual'):

            
        a = s2206evtAltContratual.objects.using(db_slug).filter(id=tabela_id,
                                                               cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2210_evtcat'):

        a = s2210evtCAT.objects.using(db_slug).filter(id=tabela_id,
                                                               cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2220_evtmonit'):

        a = s2220evtMonit.objects.using(db_slug).filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's2230_evtafasttemp'):

        a = s2230evtAfastTemp.objects.using(db_slug).filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2240_evtexprisco'):


        a = s2240evtExpRisco.objects.using(db_slug).filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif (tabela == 's2241_evtinsapo'):


        a = s2241evtInsApo.objects.using(db_slug).filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2250_evtavprevio'):

        a = s2250evtAvPrevio.objects.using(db_slug).filter(id=tabela_id,
                                                               cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2298_evtreintegr'):

        a = s2298evtReintegr.objects.using(db_slug).filter(id=tabela_id,
                                                               cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2299_evtdeslig'):


        a = s2299evtDeslig.objects.using(db_slug).filter(id=tabela_id,
                                                               cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2300_evttsvinicio'):

        a = s2300evtTSVInicio.objects.using(db_slug).filter(id=tabela_id).all()
        b = s1000evtInfoEmpregador.objects.using(db_slug).filter(nrinsc=a.nrinsc, status__in=[14])
        c = len(b)
        if not c:
            quant = 0 * quant

    elif (tabela == 's2306_evttsvaltcontr'):

        a = s2306evtTSVAltContr.objects.using(db_slug).filter(id=tabela_id).all()
        b = s2300evtTSVInicio.objects.using(db_slug).filter(cpftrab=a.cpftrab, status__in=[14])
        c = len(b)
        if not c:
            quant = 0 * quant



    elif (tabela == 's2399_evttsvtermino'):



        a = s2399evtTSVTermino.objects.using(db_slug).filter(id=tabela_id).all()
        b = s2300evtTSVInicio.objects.using(db_slug).filter(cpftrab=a.cpftrab, status__in=[14])
        c = len(b)
        if not c:
            quant = 0 * quant


    elif (tabela == 's2400_evtcdbenefin'):

        a = s2400evtCdBenefIn.objects.using(db_slug).filter(id=tabela_id).all()
        b = s1000evtInfoEmpregador.objects.using(db_slug).filter(nrinsc=a.nrinsc, status__in=[14])
        c = len(b)
        if not c:
            quant = 0 * quant

    # elif (tabela == 's3000_evtexclusao'):
    #
    #     a = s3000ideTrabalhador.objects.using(db_slug).filter(id=tabela_id).all()
    #     b = s2200evtAdmissao.objects.using(db_slug).filter(cpftrab=a.cpftrab, status__in=[14])
    #     c = len(b)
    #     if not c:
    #         quant = 0 * quant


    #quant += 1

    executar_sql("""
                UPDATE public.%s SET validacao_precedencia = %s WHERE id=%s
            """ % (tabela, quant, tabela_id), False)

    return quant



