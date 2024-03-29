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

from emensageriapro.esocial.models import STATUS_EVENTO_PROCESSADO

EVENTOS_SEM_PREDECESSAO = [
    'r1000_evtinfocontri',
    's1000_evtinfoempregador',
]


def r1000_enviados():
    from emensageriapro.efdreinf.models import r1000evtInfoContri
    lista = r1000evtInfoContri.objects.all()
    codigos_lista = []
    for a in lista:
        if a.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.nrinsc)
    return codigos_lista


def r1070_enviados():
    from emensageriapro.r1070.models import r1070inclusao
    lista = r1070inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.r1070_evttabprocesso.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.nrproc)
    return codigos_lista


def s1000_enviados():
    from emensageriapro.esocial.models import s1000evtInfoEmpregador
    lista = s1000evtInfoEmpregador.objects.all()
    codigos_lista = []
    for a in lista:
        if a.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.nrinsc)
    return codigos_lista


def s1005_estabelecimentos_enviados():
    from emensageriapro.s1005.models import s1005inclusao
    lista = s1005inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1005_evttabestab.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.nrinsc)
    return codigos_lista


def s1010_rubricas_enviados():
    from emensageriapro.s1010.models import s1010inclusao
    lista = s1010inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1010_evttabrubrica.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codrubr)
    return codigos_lista


def s1020_lotacoes_enviados():
    from emensageriapro.s1020.models import s1020inclusao
    lista = s1020inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1020_evttablotacao.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codlotacao)
    return codigos_lista


def s1030_cargos_enviados():
    from emensageriapro.s1030.models import s1030inclusao
    lista = s1030inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1030_evttabcargo.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codcargo)
    return codigos_lista


def s1035_carreiras_enviados():
    from emensageriapro.s1035.models import s1035inclusao
    lista = s1035inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1035_evttabcarreira.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codcarreira)
    return codigos_lista


def s1040_funcoes_enviados():
    from emensageriapro.s1040.models import s1040inclusao
    lista = s1040inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1040_evttabfuncao.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codfuncao)
    return codigos_lista


def s1050_horarios_enviados():
    from emensageriapro.s1050.models import s1050inclusao
    lista = s1050inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1050_evttabhortur.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codhorcontrat)
    return codigos_lista


def s1060_ambientes_enviados():
    from emensageriapro.s1060.models import s1060inclusao
    lista = s1060inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1060_evttabambiente.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.codamb)
    return codigos_lista


def s1070_processos_enviados():
    from emensageriapro.s1070.models import s1070inclusao
    lista = s1070inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.s1070_evttabprocesso.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.nrproc)
    return codigos_lista


def s1080_operadores_enviados():
    from emensageriapro.s1080.models import s1080inclusao
    lista = s1080inclusao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.r1000_evtinfocontri.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.cnpjopportuario)
    return codigos_lista


def s2200_enviados():
    from emensageriapro.esocial.models import s2200evtAdmissao
    lista = s2200evtAdmissao.objects.all()
    codigos_lista = []
    for a in lista:
        if a.status == STATUS_EVENTO_PROCESSADO:
            codigos_lista.append(a.cpftrab)
    return codigos_lista


def validar_precedencia(tabela, tabela_id):

    from emensageriapro.esocial.models import s1005evtTabEstab, \
        s1010evtTabRubrica, s1020evtTabLotacao, s1030evtTabCargo, s1035evtTabCarreira, \
        s1040evtTabFuncao, s1050evtTabHorTur, s1060evtTabAmbiente, s1070evtTabProcesso, \
        s1080evtTabOperPort, s2200evtAdmissao, s2205evtAltCadastral, \
        s2206evtAltContratual, s2210evtCAT, s2220evtMonit, s2230evtAfastTemp, s2240evtExpRisco, \
        s2241evtInsApo, s2250evtAvPrevio, s2298evtReintegr, s2299evtDeslig, \
        s2300evtTSVInicio, s2306evtTSVAltContr, s2399evtTSVTermino, s2400evtCdBenefIn

    from emensageriapro.efdreinf.models import r1070evtTabProcesso, r2010evtServTom, \
        r2020evtServPrest, r2030evtAssocDespRec, r2040evtAssocDespRep, r2050evtComProd, \
        r2060evtCPRB, r2070evtPgtosDivs, r2098evtReabreEvPer, r2099evtFechaEvPer, \
        r3010evtEspDesportivo, r9000evtExclusao

    quant = 1
    
    if tabela == 'r1070_evttabprocesso':
        a = r1070evtTabProcesso.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2010_evtservtom':
        a = r2010evtServTom.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2020_evtservprest':
        a = r2020evtServPrest.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2030_evtassocdesprec':
        a = r2030evtAssocDespRec.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2040_evtassocdesprep':
        a = r2040evtAssocDespRep.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2050_evtcomprod':
        a = r2050evtComProd.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2060_evtcprb':
        a = r2060evtCPRB.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2070_evtpgtosdivs':
        a = r2070evtPgtosDivs.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r2098_evtreabreevper':
        a = r2098evtReabreEvPer.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant
        a = r2098evtReabreEvPer.objects.filter(id=tabela_id).all()
        b = r2099evtFechaEvPer.objects.filter(perapur=a.perapur, status__in=[14])
        c = len(b)
        if not c:
            quant = 0 * quant

    elif tabela == 'r3010_evtespdesportivo':
        a = r3010evtEspDesportivo.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 'r9000_evtexclusao':
        a = r9000evtExclusao.objects.filter(id=tabela_id, nrinsc__in=r1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1005_evttabestab':
        a = s1005evtTabEstab.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1010_evttabrubrica':
        a = s1010evtTabRubrica.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1020_evttablotacao':
        a = s1020evtTabLotacao.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1030_evttabcargo':
        a = s1030evtTabCargo.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1035_evttabcarreira':
        a = s1035evtTabCarreira.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1040_evttabfuncao':
        a = s1040evtTabFuncao.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1050_evttabhortur':
        a = s1050evtTabHorTur.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1060_evttabambiente':
        a = s1060evtTabAmbiente.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1070_evttabprocesso':
        a = s1070evtTabProcesso.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's1080_evttaboperport':
        a = s1080evtTabOperPort.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2200_evtadmissao':
        a = s2200evtAdmissao.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
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

    elif tabela == 's2205_evtaltcadastral':
        a = s2205evtAltCadastral.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2206_evtaltcontratual':
        a = s2206evtAltContratual.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2210_evtcat':
        a = s2210evtCAT.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2220_evtmonit':
        a = s2220evtMonit.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2230_evtafasttemp':
        a = s2230evtAfastTemp.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2240_evtexprisco':
        a = s2240evtExpRisco.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2241_evtinsapo':
        a = s2241evtInsApo.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2250_evtavprevio':
        a = s2250evtAvPrevio.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2298_evtreintegr':
        a = s2298evtReintegr.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2299_evtdeslig':
        a = s2299evtDeslig.objects.filter(id=tabela_id, cpftrab__in=s2200_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2300_evttsvinicio':
        a = s2300evtTSVInicio.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    elif tabela == 's2306_evttsvaltcontr':
        a = s2306evtTSVAltContr.objects.get(id=tabela_id)
        b = s2300evtTSVInicio.objects.filter(cpftrab=a.cpftrab, status=STATUS_EVENTO_PROCESSADO)
        c = len(b)
        if not c:
            quant = 0 * quant

    elif tabela == 's2399_evttsvtermino':
        a = s2399evtTSVTermino.objects.get(id=tabela_id)
        b = s2300evtTSVInicio.objects.filter(cpftrab=a.cpftrab, status=STATUS_EVENTO_PROCESSADO)
        c = len(b)
        if not c:
            quant = 0 * quant

    elif tabela == 's2400_evtcdbenefin':
        a = s2400evtCdBenefIn.objects.filter(id=tabela_id, nrinsc__in=s1000_enviados()).all()
        c = len(a)
        if not c:
            quant = 0 * quant

    return quant

