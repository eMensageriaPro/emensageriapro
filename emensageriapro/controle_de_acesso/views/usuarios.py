#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

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

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.controle_de_acesso.forms import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.controle_de_acesso.models import *
import base64
from emensageriapro.mensageiro.models import Relatorios
from emensageriapro.mensageiro.models import Relatorios
from emensageriapro.mensageiro.models import TransmissorLote
from emensageriapro.mensageiro.models import TransmissorLote
from emensageriapro.mensageiro.models import RegrasDeValidacao
from emensageriapro.mensageiro.models import RegrasDeValidacao
from emensageriapro.mensageiro.models import Arquivos
from emensageriapro.mensageiro.models import Arquivos
from emensageriapro.tabelas.models import Municipios
from emensageriapro.tabelas.models import Municipios
from emensageriapro.tabelas.models import CBO
from emensageriapro.tabelas.models import CBO
from emensageriapro.tabelas.models import CID
from emensageriapro.tabelas.models import CID
from emensageriapro.tabelas.models import CNAE
from emensageriapro.tabelas.models import CNAE
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias
from emensageriapro.tabelas.models import eSocialFinanciamentosAposentadoriasEspeciais
from emensageriapro.tabelas.models import eSocialFinanciamentosAposentadoriasEspeciais
from emensageriapro.tabelas.models import eSocialNaturezasRubricas
from emensageriapro.tabelas.models import eSocialNaturezasRubricas
from emensageriapro.tabelas.models import eSocialCodigoAliquotasFPASTerceiros
from emensageriapro.tabelas.models import eSocialCodigoAliquotasFPASTerceiros
from emensageriapro.tabelas.models import eSocialInscricoesTipos
from emensageriapro.tabelas.models import eSocialInscricoesTipos
from emensageriapro.tabelas.models import eSocialPaises
from emensageriapro.tabelas.models import eSocialPaises
from emensageriapro.tabelas.models import eSocialDependentesTipos
from emensageriapro.tabelas.models import eSocialDependentesTipos
from emensageriapro.tabelas.models import eSocialClassificacoesTributarias
from emensageriapro.tabelas.models import eSocialClassificacoesTributarias
from emensageriapro.tabelas.models import eSocialArquivosEsocialTipos
from emensageriapro.tabelas.models import eSocialArquivosEsocialTipos
from emensageriapro.tabelas.models import eSocialLotacoesTributariasTipos
from emensageriapro.tabelas.models import eSocialLotacoesTributariasTipos
from emensageriapro.tabelas.models import eSocialCompatibilidadesCategoriasClassificacoesLotacoes
from emensageriapro.tabelas.models import eSocialCompatibilidadesCategoriasClassificacoesLotacoes
from emensageriapro.tabelas.models import eSocialCompatibilidadesLotacoesClassificacoes
from emensageriapro.tabelas.models import eSocialCompatibilidadesLotacoesClassificacoes
from emensageriapro.tabelas.models import eSocialPartesCorpoAtingidas
from emensageriapro.tabelas.models import eSocialPartesCorpoAtingidas
from emensageriapro.tabelas.models import eSocialAgentesCausadoresAcidentesTrabalho
from emensageriapro.tabelas.models import eSocialAgentesCausadoresAcidentesTrabalho
from emensageriapro.tabelas.models import eSocialAgentesCausadoresDoencasProfissionais
from emensageriapro.tabelas.models import eSocialAgentesCausadoresDoencasProfissionais
from emensageriapro.tabelas.models import eSocialAcidentesSituacoesGeradoras
from emensageriapro.tabelas.models import eSocialAcidentesSituacoesGeradoras
from emensageriapro.tabelas.models import eSocialNaturezasLesoes
from emensageriapro.tabelas.models import eSocialNaturezasLesoes
from emensageriapro.tabelas.models import eSocialAfastamentosMotivos
from emensageriapro.tabelas.models import eSocialAfastamentosMotivos
from emensageriapro.tabelas.models import eSocialDesligamentosMotivos
from emensageriapro.tabelas.models import eSocialDesligamentosMotivos
from emensageriapro.tabelas.models import eSocialLogradourosTipos
from emensageriapro.tabelas.models import eSocialLogradourosTipos
from emensageriapro.tabelas.models import eSocialNaturezasJuridicas
from emensageriapro.tabelas.models import eSocialNaturezasJuridicas
from emensageriapro.tabelas.models import eSocialCompatibilidadesFPASClassificacoesTributarias
from emensageriapro.tabelas.models import eSocialCompatibilidadesFPASClassificacoesTributarias
from emensageriapro.tabelas.models import eSocialFatoresRisco
from emensageriapro.tabelas.models import eSocialFatoresRisco
from emensageriapro.tabelas.models import eSocialCodificacoesAcidenteTrabalho
from emensageriapro.tabelas.models import eSocialCodificacoesAcidenteTrabalho
from emensageriapro.tabelas.models import eSocialBeneficiosPrevidenciariosTipos
from emensageriapro.tabelas.models import eSocialBeneficiosPrevidenciariosTipos
from emensageriapro.tabelas.models import eSocialBeneficiosPrevidenciariosCessacaoMotivos
from emensageriapro.tabelas.models import eSocialBeneficiosPrevidenciariosCessacaoMotivos
from emensageriapro.tabelas.models import eSocialProcedimentosDiagnosticos
from emensageriapro.tabelas.models import eSocialProcedimentosDiagnosticos
from emensageriapro.tabelas.models import eSocialAtividadesPericulosasInsalubresEspeciais
from emensageriapro.tabelas.models import eSocialAtividadesPericulosasInsalubresEspeciais
from emensageriapro.tabelas.models import eSocialTreinamentosCapacitacoesExerciciosSimulados
from emensageriapro.tabelas.models import eSocialTreinamentosCapacitacoesExerciciosSimulados
from emensageriapro.tabelas.models import eSocialProgramasPlanosDocumentos
from emensageriapro.tabelas.models import eSocialProgramasPlanosDocumentos
from emensageriapro.tabelas.models import EFDReinfPagamentosCodigos
from emensageriapro.tabelas.models import EFDReinfPagamentosCodigos
from emensageriapro.tabelas.models import EFDReinfRegrasPagamentosCodigos
from emensageriapro.tabelas.models import EFDReinfRegrasPagamentosCodigos
from emensageriapro.tabelas.models import EFDReinfRendimentosBeneficiariosExterior
from emensageriapro.tabelas.models import EFDReinfRendimentosBeneficiariosExterior
from emensageriapro.tabelas.models import EFDReinfRendimentosBeneficiariosExteriorTributacao
from emensageriapro.tabelas.models import EFDReinfRendimentosBeneficiariosExteriorTributacao
from emensageriapro.tabelas.models import EFDReinfInformacoesBeneficiariosExterior
from emensageriapro.tabelas.models import EFDReinfInformacoesBeneficiariosExterior
from emensageriapro.tabelas.models import EFDReinfClassificacaoServicosPrestados
from emensageriapro.tabelas.models import EFDReinfClassificacaoServicosPrestados
from emensageriapro.tabelas.models import EFDReinfPaises
from emensageriapro.tabelas.models import EFDReinfPaises
from emensageriapro.tabelas.models import EFDReinfClassificacaoTributaria
from emensageriapro.tabelas.models import EFDReinfClassificacaoTributaria
from emensageriapro.tabelas.models import EFDReinfCodigosAtividadesProdutosServicosCPRB
from emensageriapro.tabelas.models import EFDReinfCodigosAtividadesProdutosServicosCPRB
from emensageriapro.tabelas.models import EFDReinfEventos
from emensageriapro.tabelas.models import EFDReinfEventos
from emensageriapro.mensageiro.models import ImportacaoArquivos
from emensageriapro.mensageiro.models import ImportacaoArquivos
from emensageriapro.mensageiro.models import ImportacaoArquivos
from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
from emensageriapro.mensageiro.models import TransmissorLoteEsocial
from emensageriapro.mensageiro.models import TransmissorLoteEsocial
from emensageriapro.mensageiro.models import TransmissorLoteEsocialOcorrencias
from emensageriapro.mensageiro.models import TransmissorLoteEsocialOcorrencias
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinfOcorrencias
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinfOcorrencias
from emensageriapro.mensageiro.models import RetornosEventos
from emensageriapro.mensageiro.models import RetornosEventos
from emensageriapro.mensageiro.models import RetornosEventosOcorrencias
from emensageriapro.mensageiro.models import RetornosEventosOcorrencias
from emensageriapro.mensageiro.models import RetornosEventosHorarios
from emensageriapro.mensageiro.models import RetornosEventosHorarios
from emensageriapro.mensageiro.models import RetornosEventosIntervalos
from emensageriapro.mensageiro.models import RetornosEventosIntervalos
from emensageriapro.efdreinf.models import r1000evtInfoContri
from emensageriapro.efdreinf.models import r1000evtInfoContri
from emensageriapro.efdreinf.models import r1070evtTabProcesso
from emensageriapro.efdreinf.models import r1070evtTabProcesso
from emensageriapro.efdreinf.models import r2010evtServTom
from emensageriapro.efdreinf.models import r2010evtServTom
from emensageriapro.efdreinf.models import r2020evtServPrest
from emensageriapro.efdreinf.models import r2020evtServPrest
from emensageriapro.efdreinf.models import r2030evtAssocDespRec
from emensageriapro.efdreinf.models import r2030evtAssocDespRec
from emensageriapro.efdreinf.models import r2040evtAssocDespRep
from emensageriapro.efdreinf.models import r2040evtAssocDespRep
from emensageriapro.efdreinf.models import r2050evtComProd
from emensageriapro.efdreinf.models import r2050evtComProd
from emensageriapro.efdreinf.models import r2060evtCPRB
from emensageriapro.efdreinf.models import r2060evtCPRB
from emensageriapro.efdreinf.models import r2070evtPgtosDivs
from emensageriapro.efdreinf.models import r2070evtPgtosDivs
from emensageriapro.efdreinf.models import r2098evtReabreEvPer
from emensageriapro.efdreinf.models import r2098evtReabreEvPer
from emensageriapro.efdreinf.models import r2099evtFechaEvPer
from emensageriapro.efdreinf.models import r2099evtFechaEvPer
from emensageriapro.efdreinf.models import r3010evtEspDesportivo
from emensageriapro.efdreinf.models import r3010evtEspDesportivo
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.efdreinf.models import r9000evtExclusao
from emensageriapro.efdreinf.models import r9000evtExclusao
from emensageriapro.r1000.models import r1000inclusao
from emensageriapro.r1000.models import r1000inclusao
from emensageriapro.r1000.models import r1000inclusaosoftHouse
from emensageriapro.r1000.models import r1000inclusaosoftHouse
from emensageriapro.r1000.models import r1000inclusaoinfoEFR
from emensageriapro.r1000.models import r1000inclusaoinfoEFR
from emensageriapro.r1000.models import r1000alteracao
from emensageriapro.r1000.models import r1000alteracao
from emensageriapro.r1000.models import r1000alteracaosoftHouse
from emensageriapro.r1000.models import r1000alteracaosoftHouse
from emensageriapro.r1000.models import r1000alteracaoinfoEFR
from emensageriapro.r1000.models import r1000alteracaoinfoEFR
from emensageriapro.r1000.models import r1000alteracaonovaValidade
from emensageriapro.r1000.models import r1000alteracaonovaValidade
from emensageriapro.r1000.models import r1000exclusao
from emensageriapro.r1000.models import r1000exclusao
from emensageriapro.r1070.models import r1070inclusao
from emensageriapro.r1070.models import r1070inclusao
from emensageriapro.r1070.models import r1070inclusaoinfoSusp
from emensageriapro.r1070.models import r1070inclusaoinfoSusp
from emensageriapro.r1070.models import r1070inclusaodadosProcJud
from emensageriapro.r1070.models import r1070inclusaodadosProcJud
from emensageriapro.r1070.models import r1070alteracao
from emensageriapro.r1070.models import r1070alteracao
from emensageriapro.r1070.models import r1070alteracaoinfoSusp
from emensageriapro.r1070.models import r1070alteracaoinfoSusp
from emensageriapro.r1070.models import r1070alteracaodadosProcJud
from emensageriapro.r1070.models import r1070alteracaodadosProcJud
from emensageriapro.r1070.models import r1070alteracaonovaValidade
from emensageriapro.r1070.models import r1070alteracaonovaValidade
from emensageriapro.r1070.models import r1070exclusao
from emensageriapro.r1070.models import r1070exclusao
from emensageriapro.r2010.models import r2010nfs
from emensageriapro.r2010.models import r2010nfs
from emensageriapro.r2010.models import r2010infoTpServ
from emensageriapro.r2010.models import r2010infoTpServ
from emensageriapro.r2010.models import r2010infoProcRetPr
from emensageriapro.r2010.models import r2010infoProcRetPr
from emensageriapro.r2010.models import r2010infoProcRetAd
from emensageriapro.r2010.models import r2010infoProcRetAd
from emensageriapro.r2020.models import r2020nfs
from emensageriapro.r2020.models import r2020nfs
from emensageriapro.r2020.models import r2020infoTpServ
from emensageriapro.r2020.models import r2020infoTpServ
from emensageriapro.r2020.models import r2020infoProcRetPr
from emensageriapro.r2020.models import r2020infoProcRetPr
from emensageriapro.r2020.models import r2020infoProcRetAd
from emensageriapro.r2020.models import r2020infoProcRetAd
from emensageriapro.r2030.models import r2030recursosRec
from emensageriapro.r2030.models import r2030recursosRec
from emensageriapro.r2030.models import r2030infoRecurso
from emensageriapro.r2030.models import r2030infoRecurso
from emensageriapro.r2030.models import r2030infoProc
from emensageriapro.r2030.models import r2030infoProc
from emensageriapro.r2040.models import r2040recursosRep
from emensageriapro.r2040.models import r2040recursosRep
from emensageriapro.r2040.models import r2040infoRecurso
from emensageriapro.r2040.models import r2040infoRecurso
from emensageriapro.r2040.models import r2040infoProc
from emensageriapro.r2040.models import r2040infoProc
from emensageriapro.r2050.models import r2050tipoCom
from emensageriapro.r2050.models import r2050tipoCom
from emensageriapro.r2050.models import r2050infoProc
from emensageriapro.r2050.models import r2050infoProc
from emensageriapro.r2060.models import r2060tipoCod
from emensageriapro.r2060.models import r2060tipoCod
from emensageriapro.r2060.models import r2060tipoAjuste
from emensageriapro.r2060.models import r2060tipoAjuste
from emensageriapro.r2060.models import r2060infoProc
from emensageriapro.r2060.models import r2060infoProc
from emensageriapro.r2070.models import r2070infoResidExt
from emensageriapro.r2070.models import r2070infoResidExt
from emensageriapro.r2070.models import r2070infoMolestia
from emensageriapro.r2070.models import r2070infoMolestia
from emensageriapro.r2070.models import r2070ideEstab
from emensageriapro.r2070.models import r2070ideEstab
from emensageriapro.r2070.models import r2070pgtoResidBR
from emensageriapro.r2070.models import r2070pgtoResidBR
from emensageriapro.r2070.models import r2070pgtoPF
from emensageriapro.r2070.models import r2070pgtoPF
from emensageriapro.r2070.models import r2070detDeducao
from emensageriapro.r2070.models import r2070detDeducao
from emensageriapro.r2070.models import r2070rendIsento
from emensageriapro.r2070.models import r2070rendIsento
from emensageriapro.r2070.models import r2070detCompet
from emensageriapro.r2070.models import r2070detCompet
from emensageriapro.r2070.models import r2070compJud
from emensageriapro.r2070.models import r2070compJud
from emensageriapro.r2070.models import r2070infoRRA
from emensageriapro.r2070.models import r2070infoRRA
from emensageriapro.r2070.models import r2070infoRRAdespProcJud
from emensageriapro.r2070.models import r2070infoRRAdespProcJud
from emensageriapro.r2070.models import r2070infoRRAideAdvogado
from emensageriapro.r2070.models import r2070infoRRAideAdvogado
from emensageriapro.r2070.models import r2070infoProcJud
from emensageriapro.r2070.models import r2070infoProcJud
from emensageriapro.r2070.models import r2070infoProcJuddespProcJud
from emensageriapro.r2070.models import r2070infoProcJuddespProcJud
from emensageriapro.r2070.models import r2070infoProcJudideAdvogado
from emensageriapro.r2070.models import r2070infoProcJudideAdvogado
from emensageriapro.r2070.models import r2070infoProcJudorigemRecursos
from emensageriapro.r2070.models import r2070infoProcJudorigemRecursos
from emensageriapro.r2070.models import r2070depJudicial
from emensageriapro.r2070.models import r2070depJudicial
from emensageriapro.r2070.models import r2070pgtoPJ
from emensageriapro.r2070.models import r2070pgtoPJ
from emensageriapro.r2070.models import r2070pgtoPJinfoProcJud
from emensageriapro.r2070.models import r2070pgtoPJinfoProcJud
from emensageriapro.r2070.models import r2070pgtoPJdespProcJud
from emensageriapro.r2070.models import r2070pgtoPJdespProcJud
from emensageriapro.r2070.models import r2070pgtoPJideAdvogado
from emensageriapro.r2070.models import r2070pgtoPJideAdvogado
from emensageriapro.r2070.models import r2070pgtoPJorigemRecursos
from emensageriapro.r2070.models import r2070pgtoPJorigemRecursos
from emensageriapro.r2070.models import r2070pgtoResidExt
from emensageriapro.r2070.models import r2070pgtoResidExt
from emensageriapro.r2099.models import r2099ideRespInf
from emensageriapro.r2099.models import r2099ideRespInf
from emensageriapro.r3010.models import r3010ideEstab
from emensageriapro.r3010.models import r3010ideEstab
from emensageriapro.r3010.models import r3010boletim
from emensageriapro.r3010.models import r3010boletim
from emensageriapro.r3010.models import r3010receitaIngressos
from emensageriapro.r3010.models import r3010receitaIngressos
from emensageriapro.r3010.models import r3010outrasReceitas
from emensageriapro.r3010.models import r3010outrasReceitas
from emensageriapro.r3010.models import r3010infoProc
from emensageriapro.r3010.models import r3010infoProc
from emensageriapro.r5001.models import r5001regOcorrs
from emensageriapro.r5001.models import r5001regOcorrs
from emensageriapro.r5001.models import r5001infoTotal
from emensageriapro.r5001.models import r5001infoTotal
from emensageriapro.r5001.models import r5001RTom
from emensageriapro.r5001.models import r5001RTom
from emensageriapro.r5001.models import r5001infoCRTom
from emensageriapro.r5001.models import r5001infoCRTom
from emensageriapro.r5001.models import r5001RPrest
from emensageriapro.r5001.models import r5001RPrest
from emensageriapro.r5001.models import r5001RRecRepAD
from emensageriapro.r5001.models import r5001RRecRepAD
from emensageriapro.r5001.models import r5001RComl
from emensageriapro.r5001.models import r5001RComl
from emensageriapro.r5001.models import r5001RCPRB
from emensageriapro.r5001.models import r5001RCPRB
from emensageriapro.r5001.models import r5001RRecEspetDesp
from emensageriapro.r5001.models import r5001RRecEspetDesp
from emensageriapro.r5011.models import r5011regOcorrs
from emensageriapro.r5011.models import r5011regOcorrs
from emensageriapro.r5011.models import r5011infoTotalContrib
from emensageriapro.r5011.models import r5011infoTotalContrib
from emensageriapro.r5011.models import r5011RTom
from emensageriapro.r5011.models import r5011RTom
from emensageriapro.r5011.models import r5011infoCRTom
from emensageriapro.r5011.models import r5011infoCRTom
from emensageriapro.r5011.models import r5011RPrest
from emensageriapro.r5011.models import r5011RPrest
from emensageriapro.r5011.models import r5011RRecRepAD
from emensageriapro.r5011.models import r5011RRecRepAD
from emensageriapro.r5011.models import r5011RComl
from emensageriapro.r5011.models import r5011RComl
from emensageriapro.r5011.models import r5011RCPRB
from emensageriapro.r5011.models import r5011RCPRB
from emensageriapro.esocial.models import s1000evtInfoEmpregador
from emensageriapro.esocial.models import s1000evtInfoEmpregador
from emensageriapro.esocial.models import s1005evtTabEstab
from emensageriapro.esocial.models import s1005evtTabEstab
from emensageriapro.esocial.models import s1010evtTabRubrica
from emensageriapro.esocial.models import s1010evtTabRubrica
from emensageriapro.esocial.models import s1020evtTabLotacao
from emensageriapro.esocial.models import s1020evtTabLotacao
from emensageriapro.esocial.models import s1030evtTabCargo
from emensageriapro.esocial.models import s1030evtTabCargo
from emensageriapro.esocial.models import s1035evtTabCarreira
from emensageriapro.esocial.models import s1035evtTabCarreira
from emensageriapro.esocial.models import s1040evtTabFuncao
from emensageriapro.esocial.models import s1040evtTabFuncao
from emensageriapro.esocial.models import s1050evtTabHorTur
from emensageriapro.esocial.models import s1050evtTabHorTur
from emensageriapro.esocial.models import s1060evtTabAmbiente
from emensageriapro.esocial.models import s1060evtTabAmbiente
from emensageriapro.esocial.models import s1065evtTabEquipamento
from emensageriapro.esocial.models import s1065evtTabEquipamento
from emensageriapro.esocial.models import s1070evtTabProcesso
from emensageriapro.esocial.models import s1070evtTabProcesso
from emensageriapro.esocial.models import s1080evtTabOperPort
from emensageriapro.esocial.models import s1080evtTabOperPort
from emensageriapro.esocial.models import s1200evtRemun
from emensageriapro.esocial.models import s1200evtRemun
from emensageriapro.esocial.models import s1202evtRmnRPPS
from emensageriapro.esocial.models import s1202evtRmnRPPS
from emensageriapro.esocial.models import s1207evtBenPrRP
from emensageriapro.esocial.models import s1207evtBenPrRP
from emensageriapro.esocial.models import s1210evtPgtos
from emensageriapro.esocial.models import s1210evtPgtos
from emensageriapro.esocial.models import s1250evtAqProd
from emensageriapro.esocial.models import s1250evtAqProd
from emensageriapro.esocial.models import s1260evtComProd
from emensageriapro.esocial.models import s1260evtComProd
from emensageriapro.esocial.models import s1270evtContratAvNP
from emensageriapro.esocial.models import s1270evtContratAvNP
from emensageriapro.esocial.models import s1280evtInfoComplPer
from emensageriapro.esocial.models import s1280evtInfoComplPer
from emensageriapro.esocial.models import s1295evtTotConting
from emensageriapro.esocial.models import s1295evtTotConting
from emensageriapro.esocial.models import s1298evtReabreEvPer
from emensageriapro.esocial.models import s1298evtReabreEvPer
from emensageriapro.esocial.models import s1299evtFechaEvPer
from emensageriapro.esocial.models import s1299evtFechaEvPer
from emensageriapro.esocial.models import s1300evtContrSindPatr
from emensageriapro.esocial.models import s1300evtContrSindPatr
from emensageriapro.esocial.models import s2190evtAdmPrelim
from emensageriapro.esocial.models import s2190evtAdmPrelim
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.models import s2231evtCessao
from emensageriapro.esocial.models import s2231evtCessao
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.models import s2241evtInsApo
from emensageriapro.esocial.models import s2241evtInsApo
from emensageriapro.esocial.models import s2245evtTreiCap
from emensageriapro.esocial.models import s2245evtTreiCap
from emensageriapro.esocial.models import s2250evtAvPrevio
from emensageriapro.esocial.models import s2250evtAvPrevio
from emensageriapro.esocial.models import s2260evtConvInterm
from emensageriapro.esocial.models import s2260evtConvInterm
from emensageriapro.esocial.models import s2298evtReintegr
from emensageriapro.esocial.models import s2298evtReintegr
from emensageriapro.esocial.models import s2299evtDeslig
from emensageriapro.esocial.models import s2299evtDeslig
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.models import s2400evtCdBenefIn
from emensageriapro.esocial.models import s2400evtCdBenefIn
from emensageriapro.esocial.models import s2405evtCdBenefAlt
from emensageriapro.esocial.models import s2405evtCdBenefAlt
from emensageriapro.esocial.models import s2410evtCdBenIn
from emensageriapro.esocial.models import s2410evtCdBenIn
from emensageriapro.esocial.models import s2416evtCdBenAlt
from emensageriapro.esocial.models import s2416evtCdBenAlt
from emensageriapro.esocial.models import s2420evtCdBenTerm
from emensageriapro.esocial.models import s2420evtCdBenTerm
from emensageriapro.esocial.models import s3000evtExclusao
from emensageriapro.esocial.models import s3000evtExclusao
from emensageriapro.esocial.models import s5001evtBasesTrab
from emensageriapro.esocial.models import s5001evtBasesTrab
from emensageriapro.esocial.models import s5002evtIrrfBenef
from emensageriapro.esocial.models import s5002evtIrrfBenef
from emensageriapro.esocial.models import s5011evtCS
from emensageriapro.esocial.models import s5011evtCS
from emensageriapro.esocial.models import s5012evtIrrf
from emensageriapro.esocial.models import s5012evtIrrf
from emensageriapro.s1000.models import s1000inclusao
from emensageriapro.s1000.models import s1000inclusao
from emensageriapro.s1000.models import s1000inclusaodadosIsencao
from emensageriapro.s1000.models import s1000inclusaodadosIsencao
from emensageriapro.s1000.models import s1000inclusaoinfoOP
from emensageriapro.s1000.models import s1000inclusaoinfoOP
from emensageriapro.s1000.models import s1000inclusaoinfoEFR
from emensageriapro.s1000.models import s1000inclusaoinfoEFR
from emensageriapro.s1000.models import s1000inclusaoinfoEnte
from emensageriapro.s1000.models import s1000inclusaoinfoEnte
from emensageriapro.s1000.models import s1000inclusaoinfoOrgInternacional
from emensageriapro.s1000.models import s1000inclusaoinfoOrgInternacional
from emensageriapro.s1000.models import s1000inclusaosoftwareHouse
from emensageriapro.s1000.models import s1000inclusaosoftwareHouse
from emensageriapro.s1000.models import s1000inclusaosituacaoPJ
from emensageriapro.s1000.models import s1000inclusaosituacaoPJ
from emensageriapro.s1000.models import s1000inclusaosituacaoPF
from emensageriapro.s1000.models import s1000inclusaosituacaoPF
from emensageriapro.s1000.models import s1000alteracao
from emensageriapro.s1000.models import s1000alteracao
from emensageriapro.s1000.models import s1000alteracaodadosIsencao
from emensageriapro.s1000.models import s1000alteracaodadosIsencao
from emensageriapro.s1000.models import s1000alteracaoinfoOP
from emensageriapro.s1000.models import s1000alteracaoinfoOP
from emensageriapro.s1000.models import s1000alteracaoinfoEFR
from emensageriapro.s1000.models import s1000alteracaoinfoEFR
from emensageriapro.s1000.models import s1000alteracaoinfoEnte
from emensageriapro.s1000.models import s1000alteracaoinfoEnte
from emensageriapro.s1000.models import s1000alteracaoinfoOrgInternacional
from emensageriapro.s1000.models import s1000alteracaoinfoOrgInternacional
from emensageriapro.s1000.models import s1000alteracaosoftwareHouse
from emensageriapro.s1000.models import s1000alteracaosoftwareHouse
from emensageriapro.s1000.models import s1000alteracaosituacaoPJ
from emensageriapro.s1000.models import s1000alteracaosituacaoPJ
from emensageriapro.s1000.models import s1000alteracaosituacaoPF
from emensageriapro.s1000.models import s1000alteracaosituacaoPF
from emensageriapro.s1000.models import s1000alteracaonovaValidade
from emensageriapro.s1000.models import s1000alteracaonovaValidade
from emensageriapro.s1000.models import s1000exclusao
from emensageriapro.s1000.models import s1000exclusao
from emensageriapro.s1005.models import s1005inclusao
from emensageriapro.s1005.models import s1005inclusao
from emensageriapro.s1005.models import s1005inclusaoprocAdmJudRat
from emensageriapro.s1005.models import s1005inclusaoprocAdmJudRat
from emensageriapro.s1005.models import s1005inclusaoprocAdmJudFap
from emensageriapro.s1005.models import s1005inclusaoprocAdmJudFap
from emensageriapro.s1005.models import s1005inclusaoinfoCaepf
from emensageriapro.s1005.models import s1005inclusaoinfoCaepf
from emensageriapro.s1005.models import s1005inclusaoinfoObra
from emensageriapro.s1005.models import s1005inclusaoinfoObra
from emensageriapro.s1005.models import s1005inclusaoinfoEntEduc
from emensageriapro.s1005.models import s1005inclusaoinfoEntEduc
from emensageriapro.s1005.models import s1005inclusaoinfoPCD
from emensageriapro.s1005.models import s1005inclusaoinfoPCD
from emensageriapro.s1005.models import s1005inclusaoinfoSST
from emensageriapro.s1005.models import s1005inclusaoinfoSST
from emensageriapro.s1005.models import s1005alteracao
from emensageriapro.s1005.models import s1005alteracao
from emensageriapro.s1005.models import s1005alteracaoprocAdmJudRat
from emensageriapro.s1005.models import s1005alteracaoprocAdmJudRat
from emensageriapro.s1005.models import s1005alteracaoprocAdmJudFap
from emensageriapro.s1005.models import s1005alteracaoprocAdmJudFap
from emensageriapro.s1005.models import s1005alteracaoinfoCaepf
from emensageriapro.s1005.models import s1005alteracaoinfoCaepf
from emensageriapro.s1005.models import s1005alteracaoinfoObra
from emensageriapro.s1005.models import s1005alteracaoinfoObra
from emensageriapro.s1005.models import s1005alteracaoinfoEntEduc
from emensageriapro.s1005.models import s1005alteracaoinfoEntEduc
from emensageriapro.s1005.models import s1005alteracaoinfoPCD
from emensageriapro.s1005.models import s1005alteracaoinfoPCD
from emensageriapro.s1005.models import s1005alteracaonovaValidade
from emensageriapro.s1005.models import s1005alteracaonovaValidade
from emensageriapro.s1005.models import s1005alteracaoinfoSST
from emensageriapro.s1005.models import s1005alteracaoinfoSST
from emensageriapro.s1005.models import s1005exclusao
from emensageriapro.s1005.models import s1005exclusao
from emensageriapro.s1010.models import s1010inclusao
from emensageriapro.s1010.models import s1010inclusao
from emensageriapro.s1010.models import s1010inclusaoideProcessoCP
from emensageriapro.s1010.models import s1010inclusaoideProcessoCP
from emensageriapro.s1010.models import s1010inclusaoideProcessoIRRF
from emensageriapro.s1010.models import s1010inclusaoideProcessoIRRF
from emensageriapro.s1010.models import s1010inclusaoideProcessoFGTS
from emensageriapro.s1010.models import s1010inclusaoideProcessoFGTS
from emensageriapro.s1010.models import s1010inclusaoideProcessoSIND
from emensageriapro.s1010.models import s1010inclusaoideProcessoSIND
from emensageriapro.s1010.models import s1010inclusaoideProcessoCPRP
from emensageriapro.s1010.models import s1010inclusaoideProcessoCPRP
from emensageriapro.s1010.models import s1010alteracao
from emensageriapro.s1010.models import s1010alteracao
from emensageriapro.s1050.models import s1050exclusao
from emensageriapro.s1050.models import s1050exclusao
from emensageriapro.s1010.models import s1010alteracaoideProcessoCP
from emensageriapro.s1010.models import s1010alteracaoideProcessoCP
from emensageriapro.s1010.models import s1010alteracaoideProcessoIRRF
from emensageriapro.s1010.models import s1010alteracaoideProcessoIRRF
from emensageriapro.s1010.models import s1010alteracaoideProcessoFGTS
from emensageriapro.s1010.models import s1010alteracaoideProcessoFGTS
from emensageriapro.s1010.models import s1010alteracaoideProcessoSIND
from emensageriapro.s1010.models import s1010alteracaoideProcessoSIND
from emensageriapro.s1010.models import s1010alteracaoideProcessoCPRP
from emensageriapro.s1010.models import s1010alteracaoideProcessoCPRP
from emensageriapro.s1010.models import s1010alteracaonovaValidade
from emensageriapro.s1010.models import s1010alteracaonovaValidade
from emensageriapro.s1010.models import s1010exclusao
from emensageriapro.s1010.models import s1010exclusao
from emensageriapro.s1020.models import s1020inclusao
from emensageriapro.s1020.models import s1020inclusao
from emensageriapro.s1020.models import s1020inclusaoinfoProcJudTerceiros
from emensageriapro.s1020.models import s1020inclusaoinfoProcJudTerceiros
from emensageriapro.s1020.models import s1020inclusaoprocJudTerceiro
from emensageriapro.s1020.models import s1020inclusaoprocJudTerceiro
from emensageriapro.s1020.models import s1020inclusaoinfoEmprParcial
from emensageriapro.s1020.models import s1020inclusaoinfoEmprParcial
from emensageriapro.s1020.models import s1020alteracao
from emensageriapro.s1020.models import s1020alteracao
from emensageriapro.s1020.models import s1020alteracaoinfoProcJudTerceiros
from emensageriapro.s1020.models import s1020alteracaoinfoProcJudTerceiros
from emensageriapro.s1020.models import s1020alteracaoprocJudTerceiro
from emensageriapro.s1020.models import s1020alteracaoprocJudTerceiro
from emensageriapro.s1020.models import s1020alteracaoinfoEmprParcial
from emensageriapro.s1020.models import s1020alteracaoinfoEmprParcial
from emensageriapro.s1020.models import s1020alteracaonovaValidade
from emensageriapro.s1020.models import s1020alteracaonovaValidade
from emensageriapro.s1020.models import s1020exclusao
from emensageriapro.s1020.models import s1020exclusao
from emensageriapro.s1030.models import s1030inclusao
from emensageriapro.s1030.models import s1030inclusao
from emensageriapro.s1030.models import s1030inclusaocargoPublico
from emensageriapro.s1030.models import s1030inclusaocargoPublico
from emensageriapro.s1030.models import s1030alteracao
from emensageriapro.s1030.models import s1030alteracao
from emensageriapro.s1030.models import s1030alteracaocargoPublico
from emensageriapro.s1030.models import s1030alteracaocargoPublico
from emensageriapro.s1030.models import s1030alteracaonovaValidade
from emensageriapro.s1030.models import s1030alteracaonovaValidade
from emensageriapro.s1030.models import s1030exclusao
from emensageriapro.s1030.models import s1030exclusao
from emensageriapro.s1035.models import s1035inclusao
from emensageriapro.s1035.models import s1035inclusao
from emensageriapro.s1035.models import s1035alteracao
from emensageriapro.s1035.models import s1035alteracao
from emensageriapro.s1035.models import s1035alteracaonovaValidade
from emensageriapro.s1035.models import s1035alteracaonovaValidade
from emensageriapro.s1035.models import s1035exclusao
from emensageriapro.s1035.models import s1035exclusao
from emensageriapro.s1040.models import s1040inclusao
from emensageriapro.s1040.models import s1040inclusao
from emensageriapro.s1040.models import s1040alteracao
from emensageriapro.s1040.models import s1040alteracao
from emensageriapro.s1040.models import s1040alteracaonovaValidade
from emensageriapro.s1040.models import s1040alteracaonovaValidade
from emensageriapro.s1040.models import s1040exclusao
from emensageriapro.s1040.models import s1040exclusao
from emensageriapro.s1050.models import s1050inclusao
from emensageriapro.s1050.models import s1050inclusao
from emensageriapro.s1050.models import s1050inclusaohorarioIntervalo
from emensageriapro.s1050.models import s1050inclusaohorarioIntervalo
from emensageriapro.s1050.models import s1050alteracao
from emensageriapro.s1050.models import s1050alteracao
from emensageriapro.s1050.models import s1050alteracaohorarioIntervalo
from emensageriapro.s1050.models import s1050alteracaohorarioIntervalo
from emensageriapro.s1050.models import s1050alteracaonovaValidade
from emensageriapro.s1050.models import s1050alteracaonovaValidade
from emensageriapro.s1060.models import s1060inclusao
from emensageriapro.s1060.models import s1060inclusao
from emensageriapro.s1060.models import s1060inclusaofatorRisco
from emensageriapro.s1060.models import s1060inclusaofatorRisco
from emensageriapro.s1060.models import s1060alteracao
from emensageriapro.s1060.models import s1060alteracao
from emensageriapro.s1060.models import s1060alteracaofatorRisco
from emensageriapro.s1060.models import s1060alteracaofatorRisco
from emensageriapro.s1060.models import s1060alteracaonovaValidade
from emensageriapro.s1060.models import s1060alteracaonovaValidade
from emensageriapro.s1060.models import s1060exclusao
from emensageriapro.s1060.models import s1060exclusao
from emensageriapro.s1065.models import s1065inclusao
from emensageriapro.s1065.models import s1065inclusao
from emensageriapro.s1065.models import s1065alteracao
from emensageriapro.s1065.models import s1065alteracao
from emensageriapro.s1065.models import s1065alteracaonovaValidade
from emensageriapro.s1065.models import s1065alteracaonovaValidade
from emensageriapro.s1065.models import s1065exclusao
from emensageriapro.s1065.models import s1065exclusao
from emensageriapro.s1070.models import s1070inclusao
from emensageriapro.s1070.models import s1070inclusao
from emensageriapro.s1070.models import s1070inclusaodadosProcJud
from emensageriapro.s1070.models import s1070inclusaodadosProcJud
from emensageriapro.s1070.models import s1070inclusaoinfoSusp
from emensageriapro.s1070.models import s1070inclusaoinfoSusp
from emensageriapro.s1070.models import s1070alteracao
from emensageriapro.s1070.models import s1070alteracao
from emensageriapro.s1070.models import s1070alteracaodadosProcJud
from emensageriapro.s1070.models import s1070alteracaodadosProcJud
from emensageriapro.s1070.models import s1070alteracaoinfoSusp
from emensageriapro.s1070.models import s1070alteracaoinfoSusp
from emensageriapro.s1070.models import s1070alteracaonovaValidade
from emensageriapro.s1070.models import s1070alteracaonovaValidade
from emensageriapro.s1070.models import s1070exclusao
from emensageriapro.s1070.models import s1070exclusao
from emensageriapro.s1080.models import s1080inclusao
from emensageriapro.s1080.models import s1080inclusao
from emensageriapro.s1080.models import s1080alteracao
from emensageriapro.s1080.models import s1080alteracao
from emensageriapro.s1080.models import s1080alteracaonovaValidade
from emensageriapro.s1080.models import s1080alteracaonovaValidade
from emensageriapro.s1080.models import s1080exclusao
from emensageriapro.s1080.models import s1080exclusao
from emensageriapro.s1200.models import s1200infoMV
from emensageriapro.s1200.models import s1200infoMV
from emensageriapro.s1200.models import s1200remunOutrEmpr
from emensageriapro.s1200.models import s1200remunOutrEmpr
from emensageriapro.s1200.models import s1200infoComplem
from emensageriapro.s1200.models import s1200infoComplem
from emensageriapro.s1200.models import s1200sucessaoVinc
from emensageriapro.s1200.models import s1200sucessaoVinc
from emensageriapro.s1200.models import s1200procJudTrab
from emensageriapro.s1200.models import s1200procJudTrab
from emensageriapro.s1200.models import s1200infoInterm
from emensageriapro.s1200.models import s1200infoInterm
from emensageriapro.s1200.models import s1200dmDev
from emensageriapro.s1200.models import s1200dmDev
from emensageriapro.s1200.models import s1200infoPerApur
from emensageriapro.s1200.models import s1200infoPerApur
from emensageriapro.s1200.models import s1200infoPerApurideEstabLot
from emensageriapro.s1200.models import s1200infoPerApurideEstabLot
from emensageriapro.s1200.models import s1200infoPerApurremunPerApur
from emensageriapro.s1200.models import s1200infoPerApurremunPerApur
from emensageriapro.s1200.models import s1200infoPerApuritensRemun
from emensageriapro.s1200.models import s1200infoPerApuritensRemun
from emensageriapro.s1200.models import s1200infoPerApurinfoSaudeColet
from emensageriapro.s1200.models import s1200infoPerApurinfoSaudeColet
from emensageriapro.s1200.models import s1200infoPerApurdetOper
from emensageriapro.s1200.models import s1200infoPerApurdetOper
from emensageriapro.s1200.models import s1200infoPerApurdetPlano
from emensageriapro.s1200.models import s1200infoPerApurdetPlano
from emensageriapro.s1200.models import s1200infoPerApurinfoAgNocivo
from emensageriapro.s1200.models import s1200infoPerApurinfoAgNocivo
from emensageriapro.s1200.models import s1200infoPerApurinfoTrabInterm
from emensageriapro.s1200.models import s1200infoPerApurinfoTrabInterm
from emensageriapro.s1200.models import s1200infoPerAnt
from emensageriapro.s1200.models import s1200infoPerAnt
from emensageriapro.s1200.models import s1200infoPerAntideADC
from emensageriapro.s1200.models import s1200infoPerAntideADC
from emensageriapro.s1200.models import s1200infoPerAntidePeriodo
from emensageriapro.s1200.models import s1200infoPerAntidePeriodo
from emensageriapro.s1200.models import s1200infoPerAntideEstabLot
from emensageriapro.s1200.models import s1200infoPerAntideEstabLot
from emensageriapro.s1200.models import s1200infoPerAntremunPerAnt
from emensageriapro.s1200.models import s1200infoPerAntremunPerAnt
from emensageriapro.s1200.models import s1200infoPerAntitensRemun
from emensageriapro.s1200.models import s1200infoPerAntitensRemun
from emensageriapro.s1200.models import s1200infoPerAntinfoAgNocivo
from emensageriapro.s1200.models import s1200infoPerAntinfoAgNocivo
from emensageriapro.s1200.models import s1200infoPerAntinfoTrabInterm
from emensageriapro.s1200.models import s1200infoPerAntinfoTrabInterm
from emensageriapro.s1202.models import s1202infoPerAntremunPerAnt
from emensageriapro.s1202.models import s1202infoPerAntremunPerAnt
from emensageriapro.s1200.models import s1200infoPerAntinfoComplCont
from emensageriapro.s1200.models import s1200infoPerAntinfoComplCont
from emensageriapro.s1202.models import s1202procJudTrab
from emensageriapro.s1202.models import s1202procJudTrab
from emensageriapro.s1202.models import s1202dmDev
from emensageriapro.s1202.models import s1202dmDev
from emensageriapro.s1202.models import s1202infoPerApur
from emensageriapro.s1202.models import s1202infoPerApur
from emensageriapro.s1202.models import s1202infoPerApurideEstab
from emensageriapro.s1202.models import s1202infoPerApurideEstab
from emensageriapro.s1202.models import s1202infoPerApurremunPerApur
from emensageriapro.s1202.models import s1202infoPerApurremunPerApur
from emensageriapro.s1202.models import s1202infoPerApuritensRemun
from emensageriapro.s1202.models import s1202infoPerApuritensRemun
from emensageriapro.s1202.models import s1202infoPerApurinfoSaudeColet
from emensageriapro.s1202.models import s1202infoPerApurinfoSaudeColet
from emensageriapro.s1202.models import s1202infoPerApurdetOper
from emensageriapro.s1202.models import s1202infoPerApurdetOper
from emensageriapro.s1202.models import s1202infoPerApurdetPlano
from emensageriapro.s1202.models import s1202infoPerApurdetPlano
from emensageriapro.s1202.models import s1202infoPerAnt
from emensageriapro.s1202.models import s1202infoPerAnt
from emensageriapro.s1202.models import s1202infoPerAntideADC
from emensageriapro.s1202.models import s1202infoPerAntideADC
from emensageriapro.s1202.models import s1202infoPerAntidePeriodo
from emensageriapro.s1202.models import s1202infoPerAntidePeriodo
from emensageriapro.s1202.models import s1202infoPerAntideEstab
from emensageriapro.s1202.models import s1202infoPerAntideEstab
from emensageriapro.s1202.models import s1202infoPerAntitensRemun
from emensageriapro.s1202.models import s1202infoPerAntitensRemun
from emensageriapro.s1207.models import s1207procJudTrab
from emensageriapro.s1207.models import s1207procJudTrab
from emensageriapro.s1207.models import s1207dmDev
from emensageriapro.s1207.models import s1207dmDev
from emensageriapro.s1207.models import s1207itens
from emensageriapro.s1207.models import s1207itens
from emensageriapro.s1207.models import s1207infoPerApur
from emensageriapro.s1207.models import s1207infoPerApur
from emensageriapro.s1207.models import s1207infoPerApurideEstab
from emensageriapro.s1207.models import s1207infoPerApurideEstab
from emensageriapro.s1207.models import s1207infoPerApurremunPerApur
from emensageriapro.s1207.models import s1207infoPerApurremunPerApur
from emensageriapro.s1207.models import s1207infoPerApuritensRemun
from emensageriapro.s1207.models import s1207infoPerApuritensRemun
from emensageriapro.s1207.models import s1207infoPerAnt
from emensageriapro.s1207.models import s1207infoPerAnt
from emensageriapro.s1207.models import s1207infoPerAntideADC
from emensageriapro.s1207.models import s1207infoPerAntideADC
from emensageriapro.s1207.models import s1207infoPerAntidePeriodo
from emensageriapro.s1207.models import s1207infoPerAntidePeriodo
from emensageriapro.s1207.models import s1207infoPerAntideEstab
from emensageriapro.s1207.models import s1207infoPerAntideEstab
from emensageriapro.s1207.models import s1207infoPerAntremunPerAnt
from emensageriapro.s1207.models import s1207infoPerAntremunPerAnt
from emensageriapro.s1207.models import s1207infoPerAntitensRemun
from emensageriapro.s1207.models import s1207infoPerAntitensRemun
from emensageriapro.s1210.models import s1210deps
from emensageriapro.s1210.models import s1210deps
from emensageriapro.s1210.models import s1210infoPgto
from emensageriapro.s1210.models import s1210infoPgto
from emensageriapro.s1210.models import s1210detPgtoFl
from emensageriapro.s1210.models import s1210detPgtoFl
from emensageriapro.s1210.models import s1210detPgtoFlretPgtoTot
from emensageriapro.s1210.models import s1210detPgtoFlretPgtoTot
from emensageriapro.s1210.models import s1210detPgtoFlpenAlim
from emensageriapro.s1210.models import s1210detPgtoFlpenAlim
from emensageriapro.s1210.models import s1210detPgtoFlinfoPgtoParc
from emensageriapro.s1210.models import s1210detPgtoFlinfoPgtoParc
from emensageriapro.s1210.models import s1210detPgtoBenPr
from emensageriapro.s1210.models import s1210detPgtoBenPr
from emensageriapro.s1210.models import s1210detPgtoBenPrretPgtoTot
from emensageriapro.s1210.models import s1210detPgtoBenPrretPgtoTot
from emensageriapro.s1210.models import s1210detPgtoBenPrinfoPgtoParc
from emensageriapro.s1210.models import s1210detPgtoBenPrinfoPgtoParc
from emensageriapro.s1210.models import s1210detPgtoFer
from emensageriapro.s1210.models import s1210detPgtoFer
from emensageriapro.s1210.models import s1210detPgtoFerdetRubrFer
from emensageriapro.s1210.models import s1210detPgtoFerdetRubrFer
from emensageriapro.s1210.models import s1210detPgtoFerpenAlim
from emensageriapro.s1210.models import s1210detPgtoFerpenAlim
from emensageriapro.s1210.models import s1210detPgtoAnt
from emensageriapro.s1210.models import s1210detPgtoAnt
from emensageriapro.s1210.models import s1210detPgtoAntinfoPgtoAnt
from emensageriapro.s1210.models import s1210detPgtoAntinfoPgtoAnt
from emensageriapro.s1210.models import s1210idePgtoExt
from emensageriapro.s1210.models import s1210idePgtoExt
from emensageriapro.s1250.models import s1250tpAquis
from emensageriapro.s1250.models import s1250tpAquis
from emensageriapro.s1250.models import s1250ideProdutor
from emensageriapro.s1250.models import s1250ideProdutor
from emensageriapro.s1250.models import s1250nfs
from emensageriapro.s1250.models import s1250nfs
from emensageriapro.s1250.models import s1250infoProcJud
from emensageriapro.s1250.models import s1250infoProcJud
from emensageriapro.s1260.models import s1260tpComerc
from emensageriapro.s1260.models import s1260tpComerc
from emensageriapro.s1260.models import s1260ideAdquir
from emensageriapro.s1260.models import s1260ideAdquir
from emensageriapro.s1260.models import s1260nfs
from emensageriapro.s1260.models import s1260nfs
from emensageriapro.s2200.models import s2200infoCeletista
from emensageriapro.s2200.models import s2200infoCeletista
from emensageriapro.s1260.models import s1260infoProcJud
from emensageriapro.s1260.models import s1260infoProcJud
from emensageriapro.s1270.models import s1270remunAvNP
from emensageriapro.s1270.models import s1270remunAvNP
from emensageriapro.s1280.models import s1280infoSubstPatr
from emensageriapro.s1280.models import s1280infoSubstPatr
from emensageriapro.s1280.models import s1280infoSubstPatrOpPort
from emensageriapro.s1280.models import s1280infoSubstPatrOpPort
from emensageriapro.s1280.models import s1280infoAtivConcom
from emensageriapro.s1280.models import s1280infoAtivConcom
from emensageriapro.s1295.models import s1295ideRespInf
from emensageriapro.s1295.models import s1295ideRespInf
from emensageriapro.s1299.models import s1299ideRespInf
from emensageriapro.s1299.models import s1299ideRespInf
from emensageriapro.s1300.models import s1300contribSind
from emensageriapro.s1300.models import s1300contribSind
from emensageriapro.s2200.models import s2200documentos
from emensageriapro.s2200.models import s2200documentos
from emensageriapro.s2200.models import s2200CTPS
from emensageriapro.s2200.models import s2200CTPS
from emensageriapro.s2200.models import s2200RIC
from emensageriapro.s2200.models import s2200RIC
from emensageriapro.s2200.models import s2200RG
from emensageriapro.s2200.models import s2200RG
from emensageriapro.s2200.models import s2200RNE
from emensageriapro.s2200.models import s2200RNE
from emensageriapro.s2200.models import s2200OC
from emensageriapro.s2200.models import s2200OC
from emensageriapro.s2200.models import s2200CNH
from emensageriapro.s2200.models import s2200CNH
from emensageriapro.s2200.models import s2200brasil
from emensageriapro.s2200.models import s2200brasil
from emensageriapro.s2200.models import s2200exterior
from emensageriapro.s2200.models import s2200exterior
from emensageriapro.s2200.models import s2200trabEstrangeiro
from emensageriapro.s2200.models import s2200trabEstrangeiro
from emensageriapro.s2200.models import s2200infoDeficiencia
from emensageriapro.s2200.models import s2200infoDeficiencia
from emensageriapro.s2200.models import s2200dependente
from emensageriapro.s2200.models import s2200dependente
from emensageriapro.s2200.models import s2200aposentadoria
from emensageriapro.s2200.models import s2200aposentadoria
from emensageriapro.s2200.models import s2200contato
from emensageriapro.s2200.models import s2200contato
from emensageriapro.s2200.models import s2200trabTemporario
from emensageriapro.s2200.models import s2200trabTemporario
from emensageriapro.s2200.models import s2200ideEstabVinc
from emensageriapro.s2200.models import s2200ideEstabVinc
from emensageriapro.s2200.models import s2200ideTrabSubstituido
from emensageriapro.s2200.models import s2200ideTrabSubstituido
from emensageriapro.s2200.models import s2200aprend
from emensageriapro.s2200.models import s2200aprend
from emensageriapro.s2200.models import s2200infoEstatutario
from emensageriapro.s2200.models import s2200infoEstatutario
from emensageriapro.s2200.models import s2200infoDecJud
from emensageriapro.s2200.models import s2200infoDecJud
from emensageriapro.s2200.models import s2200localTrabGeral
from emensageriapro.s2200.models import s2200localTrabGeral
from emensageriapro.s2200.models import s2200localTrabDom
from emensageriapro.s2200.models import s2200localTrabDom
from emensageriapro.s2200.models import s2200horContratual
from emensageriapro.s2200.models import s2200horContratual
from emensageriapro.s2200.models import s2200horario
from emensageriapro.s2200.models import s2200horario
from emensageriapro.s2200.models import s2200filiacaoSindical
from emensageriapro.s2200.models import s2200filiacaoSindical
from emensageriapro.s2200.models import s2200alvaraJudicial
from emensageriapro.s2200.models import s2200alvaraJudicial
from emensageriapro.s2200.models import s2200observacoes
from emensageriapro.s2200.models import s2200observacoes
from emensageriapro.s2200.models import s2200sucessaoVinc
from emensageriapro.s2200.models import s2200sucessaoVinc
from emensageriapro.s2200.models import s2200transfDom
from emensageriapro.s2200.models import s2200transfDom
from emensageriapro.s2200.models import s2200afastamento
from emensageriapro.s2200.models import s2200afastamento
from emensageriapro.s2200.models import s2200desligamento
from emensageriapro.s2200.models import s2200desligamento
from emensageriapro.s2200.models import s2200cessao
from emensageriapro.s2200.models import s2200cessao
from emensageriapro.s2205.models import s2205documentos
from emensageriapro.s2205.models import s2205documentos
from emensageriapro.s2205.models import s2205CTPS
from emensageriapro.s2205.models import s2205CTPS
from emensageriapro.s2205.models import s2205RIC
from emensageriapro.s2205.models import s2205RIC
from emensageriapro.s2205.models import s2205RG
from emensageriapro.s2205.models import s2205RG
from emensageriapro.s2205.models import s2205RNE
from emensageriapro.s2205.models import s2205RNE
from emensageriapro.s2205.models import s2205OC
from emensageriapro.s2205.models import s2205OC
from emensageriapro.s2205.models import s2205CNH
from emensageriapro.s2205.models import s2205CNH
from emensageriapro.s2205.models import s2205brasil
from emensageriapro.s2205.models import s2205brasil
from emensageriapro.s2205.models import s2205exterior
from emensageriapro.s2205.models import s2205exterior
from emensageriapro.s2205.models import s2205trabEstrangeiro
from emensageriapro.s2205.models import s2205trabEstrangeiro
from emensageriapro.s2205.models import s2205infoDeficiencia
from emensageriapro.s2205.models import s2205infoDeficiencia
from emensageriapro.s2205.models import s2205dependente
from emensageriapro.s2205.models import s2205dependente
from emensageriapro.s2205.models import s2205aposentadoria
from emensageriapro.s2205.models import s2205aposentadoria
from emensageriapro.s2205.models import s2205contato
from emensageriapro.s2205.models import s2205contato
from emensageriapro.s2206.models import s2206infoCeletista
from emensageriapro.s2206.models import s2206infoCeletista
from emensageriapro.s2206.models import s2206trabTemp
from emensageriapro.s2206.models import s2206trabTemp
from emensageriapro.s2206.models import s2206aprend
from emensageriapro.s2206.models import s2206aprend
from emensageriapro.s2206.models import s2206infoEstatutario
from emensageriapro.s2206.models import s2206infoEstatutario
from emensageriapro.s2206.models import s2206localTrabGeral
from emensageriapro.s2206.models import s2206localTrabGeral
from emensageriapro.s2206.models import s2206localTrabDom
from emensageriapro.s2206.models import s2206localTrabDom
from emensageriapro.s2206.models import s2206horContratual
from emensageriapro.s2206.models import s2206horContratual
from emensageriapro.s2206.models import s2206horario
from emensageriapro.s2206.models import s2206horario
from emensageriapro.s2206.models import s2206filiacaoSindical
from emensageriapro.s2206.models import s2206filiacaoSindical
from emensageriapro.s2240.models import s2240iniExpRiscoepc
from emensageriapro.s2240.models import s2240iniExpRiscoepc
from emensageriapro.s2206.models import s2206alvaraJudicial
from emensageriapro.s2206.models import s2206alvaraJudicial
from emensageriapro.s2206.models import s2206observacoes
from emensageriapro.s2206.models import s2206observacoes
from emensageriapro.s2206.models import s2206servPubl
from emensageriapro.s2206.models import s2206servPubl
from emensageriapro.s2210.models import s2210ideLocalAcid
from emensageriapro.s2210.models import s2210ideLocalAcid
from emensageriapro.s2210.models import s2210parteAtingida
from emensageriapro.s2210.models import s2210parteAtingida
from emensageriapro.s2210.models import s2210agenteCausador
from emensageriapro.s2210.models import s2210agenteCausador
from emensageriapro.s2210.models import s2210atestado
from emensageriapro.s2210.models import s2210atestado
from emensageriapro.s2210.models import s2210catOrigem
from emensageriapro.s2210.models import s2210catOrigem
from emensageriapro.s2220.models import s2220exMedOcup
from emensageriapro.s2220.models import s2220exMedOcup
from emensageriapro.s2220.models import s2220exame
from emensageriapro.s2220.models import s2220exame
from emensageriapro.s2220.models import s2220toxicologico
from emensageriapro.s2220.models import s2220toxicologico
from emensageriapro.s2230.models import s2230iniAfastamento
from emensageriapro.s2230.models import s2230iniAfastamento
from emensageriapro.s2230.models import s2230infoAtestado
from emensageriapro.s2230.models import s2230infoAtestado
from emensageriapro.s2230.models import s2230emitente
from emensageriapro.s2230.models import s2230emitente
from emensageriapro.s2230.models import s2230infoCessao
from emensageriapro.s2230.models import s2230infoCessao
from emensageriapro.s2230.models import s2230infoMandSind
from emensageriapro.s2230.models import s2230infoMandSind
from emensageriapro.s2230.models import s2230infoRetif
from emensageriapro.s2230.models import s2230infoRetif
from emensageriapro.s2230.models import s2230fimAfastamento
from emensageriapro.s2230.models import s2230fimAfastamento
from emensageriapro.s2231.models import s2231iniCessao
from emensageriapro.s2231.models import s2231iniCessao
from emensageriapro.s2231.models import s2231fimCessao
from emensageriapro.s2231.models import s2231fimCessao
from emensageriapro.s2240.models import s2240iniExpRisco
from emensageriapro.s2240.models import s2240iniExpRisco
from emensageriapro.s2240.models import s2240iniExpRiscoinfoAmb
from emensageriapro.s2240.models import s2240iniExpRiscoinfoAmb
from emensageriapro.s2240.models import s2240iniExpRiscoativPericInsal
from emensageriapro.s2240.models import s2240iniExpRiscoativPericInsal
from emensageriapro.s2240.models import s2240iniExpRiscofatRisco
from emensageriapro.s2240.models import s2240iniExpRiscofatRisco
from emensageriapro.s2240.models import s2240iniExpRiscoepi
from emensageriapro.s2240.models import s2240iniExpRiscoepi
from emensageriapro.s2240.models import s2240iniExpRiscorespReg
from emensageriapro.s2240.models import s2240iniExpRiscorespReg
from emensageriapro.s2240.models import s2240iniExpRiscoobs
from emensageriapro.s2240.models import s2240iniExpRiscoobs
from emensageriapro.s2240.models import s2240altExpRisco
from emensageriapro.s2240.models import s2240altExpRisco
from emensageriapro.s2240.models import s2240altExpRiscoinfoAmb
from emensageriapro.s2240.models import s2240altExpRiscoinfoAmb
from emensageriapro.s2240.models import s2240altExpRiscofatRisco
from emensageriapro.s2240.models import s2240altExpRiscofatRisco
from emensageriapro.s2240.models import s2240altExpRiscoepc
from emensageriapro.s2240.models import s2240altExpRiscoepc
from emensageriapro.s2240.models import s2240altExpRiscoepi
from emensageriapro.s2240.models import s2240altExpRiscoepi
from emensageriapro.s2240.models import s2240fimExpRisco
from emensageriapro.s2240.models import s2240fimExpRisco
from emensageriapro.s2240.models import s2240fimExpRiscoinfoAmb
from emensageriapro.s2240.models import s2240fimExpRiscoinfoAmb
from emensageriapro.s2240.models import s2240fimExpRiscorespReg
from emensageriapro.s2240.models import s2240fimExpRiscorespReg
from emensageriapro.s2241.models import s2241insalPeric
from emensageriapro.s2241.models import s2241insalPeric
from emensageriapro.s2241.models import s2241iniInsalPeric
from emensageriapro.s2241.models import s2241iniInsalPeric
from emensageriapro.s2241.models import s2241iniInsalPericinfoAmb
from emensageriapro.s2241.models import s2241iniInsalPericinfoAmb
from emensageriapro.s2241.models import s2241iniInsalPericfatRisco
from emensageriapro.s2241.models import s2241iniInsalPericfatRisco
from emensageriapro.s2241.models import s2241altInsalPeric
from emensageriapro.s2241.models import s2241altInsalPeric
from emensageriapro.s2241.models import s2241altInsalPericinfoamb
from emensageriapro.s2241.models import s2241altInsalPericinfoamb
from emensageriapro.s2241.models import s2241altInsalPericfatRisco
from emensageriapro.s2241.models import s2241altInsalPericfatRisco
from emensageriapro.s2241.models import s2241fimInsalPeric
from emensageriapro.s2241.models import s2241fimInsalPeric
from emensageriapro.s2241.models import s2241fimInsalPericinfoAmb
from emensageriapro.s2241.models import s2241fimInsalPericinfoAmb
from emensageriapro.s2241.models import s2241aposentEsp
from emensageriapro.s2241.models import s2241aposentEsp
from emensageriapro.s2241.models import s2241iniAposentEsp
from emensageriapro.s2241.models import s2241iniAposentEsp
from emensageriapro.s2241.models import s2241iniAposentEspinfoAmb
from emensageriapro.s2241.models import s2241iniAposentEspinfoAmb
from emensageriapro.s2241.models import s2241iniAposentEspfatRisco
from emensageriapro.s2241.models import s2241iniAposentEspfatRisco
from emensageriapro.s2241.models import s2241altAposentEsp
from emensageriapro.s2241.models import s2241altAposentEsp
from emensageriapro.s2241.models import s2241altAposentEspinfoamb
from emensageriapro.s2241.models import s2241altAposentEspinfoamb
from emensageriapro.s2241.models import s2241altAposentEspfatRisco
from emensageriapro.s2241.models import s2241altAposentEspfatRisco
from emensageriapro.s2241.models import s2241fimAposentEsp
from emensageriapro.s2241.models import s2241fimAposentEsp
from emensageriapro.s2241.models import s2241fimAposentEspinfoAmb
from emensageriapro.s2241.models import s2241fimAposentEspinfoAmb
from emensageriapro.s2245.models import s2245ideProfResp
from emensageriapro.s2245.models import s2245ideProfResp
from emensageriapro.s2250.models import s2250detAvPrevio
from emensageriapro.s2250.models import s2250detAvPrevio
from emensageriapro.s2250.models import s2250cancAvPrevio
from emensageriapro.s2250.models import s2250cancAvPrevio
from emensageriapro.s2260.models import s2260localTrabInterm
from emensageriapro.s2260.models import s2260localTrabInterm
from emensageriapro.s2299.models import s2299observacoes
from emensageriapro.s2299.models import s2299observacoes
from emensageriapro.s2299.models import s2299sucessaoVinc
from emensageriapro.s2299.models import s2299sucessaoVinc
from emensageriapro.s2299.models import s2299transfTit
from emensageriapro.s2299.models import s2299transfTit
from emensageriapro.s2299.models import s2299verbasResc
from emensageriapro.s2299.models import s2299verbasResc
from emensageriapro.s2299.models import s2299dmDev
from emensageriapro.s2299.models import s2299dmDev
from emensageriapro.s2299.models import s2299infoPerApur
from emensageriapro.s2299.models import s2299infoPerApur
from emensageriapro.s2299.models import s2299infoPerApurideEstabLot
from emensageriapro.s2299.models import s2299infoPerApurideEstabLot
from emensageriapro.s2299.models import s2299infoPerApurdetVerbas
from emensageriapro.s2299.models import s2299infoPerApurdetVerbas
from emensageriapro.s2299.models import s2299infoPerApurinfoSaudeColet
from emensageriapro.s2299.models import s2299infoPerApurinfoSaudeColet
from emensageriapro.s2299.models import s2299infoPerApurdetOper
from emensageriapro.s2299.models import s2299infoPerApurdetOper
from emensageriapro.s2299.models import s2299infoPerApurdetPlano
from emensageriapro.s2299.models import s2299infoPerApurdetPlano
from emensageriapro.s2300.models import s2300infoDirigenteSindical
from emensageriapro.s2300.models import s2300infoDirigenteSindical
from emensageriapro.s2299.models import s2299infoPerApurinfoAgNocivo
from emensageriapro.s2299.models import s2299infoPerApurinfoAgNocivo
from emensageriapro.s2299.models import s2299infoPerApurinfoSimples
from emensageriapro.s2299.models import s2299infoPerApurinfoSimples
from emensageriapro.s2299.models import s2299infoPerAnt
from emensageriapro.s2299.models import s2299infoPerAnt
from emensageriapro.s2299.models import s2299infoPerAntideADC
from emensageriapro.s2299.models import s2299infoPerAntideADC
from emensageriapro.s2299.models import s2299infoPerAntidePeriodo
from emensageriapro.s2299.models import s2299infoPerAntidePeriodo
from emensageriapro.s2299.models import s2299infoPerAntideEstabLot
from emensageriapro.s2299.models import s2299infoPerAntideEstabLot
from emensageriapro.s2299.models import s2299infoPerAntdetVerbas
from emensageriapro.s2299.models import s2299infoPerAntdetVerbas
from emensageriapro.s2299.models import s2299infoPerAntinfoAgNocivo
from emensageriapro.s2299.models import s2299infoPerAntinfoAgNocivo
from emensageriapro.s2299.models import s2299infoPerAntinfoSimples
from emensageriapro.s2299.models import s2299infoPerAntinfoSimples
from emensageriapro.s2299.models import s2299infoTrabInterm
from emensageriapro.s2299.models import s2299infoTrabInterm
from emensageriapro.s2299.models import s2299infoTrabIntermprocJudTrab
from emensageriapro.s2299.models import s2299infoTrabIntermprocJudTrab
from emensageriapro.s2299.models import s2299infoTrabInterminfoMV
from emensageriapro.s2299.models import s2299infoTrabInterminfoMV
from emensageriapro.s2299.models import s2299infoTrabIntermremunOutrEmpr
from emensageriapro.s2299.models import s2299infoTrabIntermremunOutrEmpr
from emensageriapro.s2299.models import s2299infoTrabIntermprocCS
from emensageriapro.s2299.models import s2299infoTrabIntermprocCS
from emensageriapro.s2299.models import s2299infoTrabIntermquarentena
from emensageriapro.s2299.models import s2299infoTrabIntermquarentena
from emensageriapro.s2299.models import s2299infoTrabIntermconsigFGTS
from emensageriapro.s2299.models import s2299infoTrabIntermconsigFGTS
from emensageriapro.s2300.models import s2300documentos
from emensageriapro.s2300.models import s2300documentos
from emensageriapro.s2300.models import s2300CTPS
from emensageriapro.s2300.models import s2300CTPS
from emensageriapro.s2300.models import s2300RIC
from emensageriapro.s2300.models import s2300RIC
from emensageriapro.s2300.models import s2300RG
from emensageriapro.s2300.models import s2300RG
from emensageriapro.s2300.models import s2300RNE
from emensageriapro.s2300.models import s2300RNE
from emensageriapro.s2300.models import s2300OC
from emensageriapro.s2300.models import s2300OC
from emensageriapro.s2300.models import s2300CNH
from emensageriapro.s2300.models import s2300CNH
from emensageriapro.s2300.models import s2300brasil
from emensageriapro.s2300.models import s2300brasil
from emensageriapro.s2300.models import s2300exterior
from emensageriapro.s2300.models import s2300exterior
from emensageriapro.s2300.models import s2300trabEstrangeiro
from emensageriapro.s2300.models import s2300trabEstrangeiro
from emensageriapro.s2300.models import s2300infoDeficiencia
from emensageriapro.s2300.models import s2300infoDeficiencia
from emensageriapro.s2300.models import s2300dependente
from emensageriapro.s2300.models import s2300dependente
from emensageriapro.s2300.models import s2300contato
from emensageriapro.s2300.models import s2300contato
from emensageriapro.s2300.models import s2300infoComplementares
from emensageriapro.s2300.models import s2300infoComplementares
from emensageriapro.s2300.models import s2300cargoFuncao
from emensageriapro.s2300.models import s2300cargoFuncao
from emensageriapro.s2300.models import s2300remuneracao
from emensageriapro.s2300.models import s2300remuneracao
from emensageriapro.s2300.models import s2300fgts
from emensageriapro.s2300.models import s2300fgts
from emensageriapro.s2300.models import s2300infoTrabCedido
from emensageriapro.s2300.models import s2300infoTrabCedido
from emensageriapro.s2300.models import s2300infoEstagiario
from emensageriapro.s2300.models import s2300infoEstagiario
from emensageriapro.s2300.models import s2300ageIntegracao
from emensageriapro.s2300.models import s2300ageIntegracao
from emensageriapro.s2300.models import s2300supervisorEstagio
from emensageriapro.s2300.models import s2300supervisorEstagio
from emensageriapro.s2300.models import s2300afastamento
from emensageriapro.s2300.models import s2300afastamento
from emensageriapro.s2300.models import s2300termino
from emensageriapro.s2300.models import s2300termino
from emensageriapro.s2306.models import s2306infoComplementares
from emensageriapro.s2306.models import s2306infoComplementares
from emensageriapro.s2306.models import s2306cargoFuncao
from emensageriapro.s2306.models import s2306cargoFuncao
from emensageriapro.s2306.models import s2306remuneracao
from emensageriapro.s2306.models import s2306remuneracao
from emensageriapro.s2306.models import s2306infoTrabCedido
from emensageriapro.s2306.models import s2306infoTrabCedido
from emensageriapro.s2306.models import s2306infoEstagiario
from emensageriapro.s2306.models import s2306infoEstagiario
from emensageriapro.s2306.models import s2306ageIntegracao
from emensageriapro.s2306.models import s2306ageIntegracao
from emensageriapro.s2306.models import s2306supervisorEstagio
from emensageriapro.s2306.models import s2306supervisorEstagio
from emensageriapro.s2399.models import s2399verbasResc
from emensageriapro.s2399.models import s2399verbasResc
from emensageriapro.s2399.models import s2399dmDev
from emensageriapro.s2399.models import s2399dmDev
from emensageriapro.s2399.models import s2399ideEstabLot
from emensageriapro.s2399.models import s2399ideEstabLot
from emensageriapro.s2399.models import s2399detVerbas
from emensageriapro.s2399.models import s2399detVerbas
from emensageriapro.s2399.models import s2399infoSaudeColet
from emensageriapro.s2399.models import s2399infoSaudeColet
from emensageriapro.s2399.models import s2399detOper
from emensageriapro.s2399.models import s2399detOper
from emensageriapro.s2399.models import s2399detPlano
from emensageriapro.s2399.models import s2399detPlano
from emensageriapro.s2399.models import s2399infoAgNocivo
from emensageriapro.s2399.models import s2399infoAgNocivo
from emensageriapro.s2399.models import s2399infoSimples
from emensageriapro.s2399.models import s2399infoSimples
from emensageriapro.s2399.models import s2399procJudTrab
from emensageriapro.s2399.models import s2399procJudTrab
from emensageriapro.s2399.models import s2399infoMV
from emensageriapro.s2399.models import s2399infoMV
from emensageriapro.s2399.models import s2399remunOutrEmpr
from emensageriapro.s2399.models import s2399remunOutrEmpr
from emensageriapro.s2399.models import s2399quarentena
from emensageriapro.s2399.models import s2399quarentena
from emensageriapro.s2400.models import s2400endereco
from emensageriapro.s2400.models import s2400endereco
from emensageriapro.s2400.models import s2400brasil
from emensageriapro.s2400.models import s2400brasil
from emensageriapro.s2400.models import s2400exterior
from emensageriapro.s2400.models import s2400exterior
from emensageriapro.s2400.models import s2400dependente
from emensageriapro.s2400.models import s2400dependente
from emensageriapro.s2405.models import s2405endereco
from emensageriapro.s2405.models import s2405endereco
from emensageriapro.s2405.models import s2405brasil
from emensageriapro.s2405.models import s2405brasil
from emensageriapro.s2405.models import s2405exterior
from emensageriapro.s2405.models import s2405exterior
from emensageriapro.s2405.models import s2405dependente
from emensageriapro.s2405.models import s2405dependente
from emensageriapro.s2410.models import s2410infoPenMorte
from emensageriapro.s2410.models import s2410infoPenMorte
from emensageriapro.s2410.models import s2410instPenMorte
from emensageriapro.s2410.models import s2410instPenMorte
from emensageriapro.s2410.models import s2410homologTC
from emensageriapro.s2410.models import s2410homologTC
from emensageriapro.s2416.models import s2416infoPenMorte
from emensageriapro.s2416.models import s2416infoPenMorte
from emensageriapro.s2416.models import s2416homologTC
from emensageriapro.s2416.models import s2416homologTC
from emensageriapro.s2416.models import s2416suspensao
from emensageriapro.s2416.models import s2416suspensao
from emensageriapro.s3000.models import s3000ideTrabalhador
from emensageriapro.s3000.models import s3000ideTrabalhador
from emensageriapro.s3000.models import s3000ideFolhaPagto
from emensageriapro.s3000.models import s3000ideFolhaPagto
from emensageriapro.s5001.models import s5001procJudTrab
from emensageriapro.s5001.models import s5001procJudTrab
from emensageriapro.s5001.models import s5001infoCpCalc
from emensageriapro.s5001.models import s5001infoCpCalc
from emensageriapro.s5001.models import s5001infoCp
from emensageriapro.s5001.models import s5001infoCp
from emensageriapro.s5001.models import s5001ideEstabLot
from emensageriapro.s5001.models import s5001ideEstabLot
from emensageriapro.s5001.models import s5001infoCategIncid
from emensageriapro.s5001.models import s5001infoCategIncid
from emensageriapro.s5001.models import s5001infoBaseCS
from emensageriapro.s5001.models import s5001infoBaseCS
from emensageriapro.s5001.models import s5001calcTerc
from emensageriapro.s5001.models import s5001calcTerc
from emensageriapro.s5002.models import s5002infoDep
from emensageriapro.s5002.models import s5002infoDep
from emensageriapro.s5002.models import s5002infoIrrf
from emensageriapro.s5002.models import s5002infoIrrf
from emensageriapro.s5002.models import s5002basesIrrf
from emensageriapro.s5002.models import s5002basesIrrf
from emensageriapro.s5002.models import s5002irrf
from emensageriapro.s5002.models import s5002irrf
from emensageriapro.s5002.models import s5002idePgtoExt
from emensageriapro.s5002.models import s5002idePgtoExt
from emensageriapro.s5011.models import s5011infoCPSeg
from emensageriapro.s5011.models import s5011infoCPSeg
from emensageriapro.s5011.models import s5011infoPJ
from emensageriapro.s5011.models import s5011infoPJ
from emensageriapro.s5011.models import s5011infoAtConc
from emensageriapro.s5011.models import s5011infoAtConc
from emensageriapro.s5011.models import s5011ideEstab
from emensageriapro.s5011.models import s5011ideEstab
from emensageriapro.s5011.models import s5011infoEstab
from emensageriapro.s5011.models import s5011infoEstab
from emensageriapro.s5011.models import s5011infoComplObra
from emensageriapro.s5011.models import s5011infoComplObra
from emensageriapro.s5011.models import s5011ideLotacao
from emensageriapro.s5011.models import s5011ideLotacao
from emensageriapro.s5011.models import s5011infoTercSusp
from emensageriapro.s5011.models import s5011infoTercSusp
from emensageriapro.s5011.models import s5011infoEmprParcial
from emensageriapro.s5011.models import s5011infoEmprParcial
from emensageriapro.s5011.models import s5011dadosOpPort
from emensageriapro.s5011.models import s5011dadosOpPort
from emensageriapro.s5011.models import s5011basesRemun
from emensageriapro.s5011.models import s5011basesRemun
from emensageriapro.s5011.models import s5011basesAvNPort
from emensageriapro.s5011.models import s5011basesAvNPort
from emensageriapro.s5011.models import s5011infoSubstPatrOpPort
from emensageriapro.s5011.models import s5011infoSubstPatrOpPort
from emensageriapro.s5011.models import s5011basesAquis
from emensageriapro.s5011.models import s5011basesAquis
from emensageriapro.s5011.models import s5011basesComerc
from emensageriapro.s5011.models import s5011basesComerc
from emensageriapro.s5011.models import s5011infoCREstab
from emensageriapro.s5011.models import s5011infoCREstab
from emensageriapro.s5011.models import s5011infoCRContrib
from emensageriapro.s5011.models import s5011infoCRContrib
from emensageriapro.s5012.models import s5012infoCRContrib
from emensageriapro.s5012.models import s5012infoCRContrib
from emensageriapro.mensageiro.forms import form_relatorios
from emensageriapro.mensageiro.forms import form_relatorios
from emensageriapro.mensageiro.forms import form_transmissores
from emensageriapro.mensageiro.forms import form_transmissores
from emensageriapro.mensageiro.forms import form_regras_validacao
from emensageriapro.mensageiro.forms import form_regras_validacao
from emensageriapro.mensageiro.forms import form_arquivos
from emensageriapro.mensageiro.forms import form_arquivos
from emensageriapro.tabelas.forms import form_municipios
from emensageriapro.tabelas.forms import form_municipios
from emensageriapro.tabelas.forms import form_cbo
from emensageriapro.tabelas.forms import form_cbo
from emensageriapro.tabelas.forms import form_cid
from emensageriapro.tabelas.forms import form_cid
from emensageriapro.tabelas.forms import form_cnae
from emensageriapro.tabelas.forms import form_cnae
from emensageriapro.tabelas.forms import form_esocial_trabalhadores_categorias
from emensageriapro.tabelas.forms import form_esocial_trabalhadores_categorias
from emensageriapro.tabelas.forms import form_esocial_financiamentos_aposentadorias_especiais
from emensageriapro.tabelas.forms import form_esocial_financiamentos_aposentadorias_especiais
from emensageriapro.tabelas.forms import form_esocial_naturezas_rubricas
from emensageriapro.tabelas.forms import form_esocial_naturezas_rubricas
from emensageriapro.tabelas.forms import form_esocial_codigo_aliquotas_fpas_terceiros
from emensageriapro.tabelas.forms import form_esocial_codigo_aliquotas_fpas_terceiros
from emensageriapro.tabelas.forms import form_esocial_inscricoes_tipos
from emensageriapro.tabelas.forms import form_esocial_inscricoes_tipos
from emensageriapro.tabelas.forms import form_esocial_paises
from emensageriapro.tabelas.forms import form_esocial_paises
from emensageriapro.tabelas.forms import form_esocial_dependentes_tipos
from emensageriapro.tabelas.forms import form_esocial_dependentes_tipos
from emensageriapro.tabelas.forms import form_esocial_classificacoes_tributarias
from emensageriapro.tabelas.forms import form_esocial_classificacoes_tributarias
from emensageriapro.tabelas.forms import form_esocial_arquivos_esocial_tipos
from emensageriapro.tabelas.forms import form_esocial_arquivos_esocial_tipos
from emensageriapro.tabelas.forms import form_esocial_lotacoes_tributarias_tipos
from emensageriapro.tabelas.forms import form_esocial_lotacoes_tributarias_tipos
from emensageriapro.tabelas.forms import form_esocial_compatibilidades_categorias_classificacoes_lotacoes
from emensageriapro.tabelas.forms import form_esocial_compatibilidades_categorias_classificacoes_lotacoes
from emensageriapro.tabelas.forms import form_esocial_compatibilidades_lotacoes_classificacoes
from emensageriapro.tabelas.forms import form_esocial_compatibilidades_lotacoes_classificacoes
from emensageriapro.tabelas.forms import form_esocial_partes_corpo_atingidas
from emensageriapro.tabelas.forms import form_esocial_partes_corpo_atingidas
from emensageriapro.tabelas.forms import form_esocial_agentes_causadores_acidentes_trabalho
from emensageriapro.tabelas.forms import form_esocial_agentes_causadores_acidentes_trabalho
from emensageriapro.tabelas.forms import form_esocial_agentes_causadores_doencas_profissionais
from emensageriapro.tabelas.forms import form_esocial_agentes_causadores_doencas_profissionais
from emensageriapro.tabelas.forms import form_esocial_acidentes_situacoes_geradoras
from emensageriapro.tabelas.forms import form_esocial_acidentes_situacoes_geradoras
from emensageriapro.tabelas.forms import form_esocial_naturezas_lesoes
from emensageriapro.tabelas.forms import form_esocial_naturezas_lesoes
from emensageriapro.tabelas.forms import form_esocial_afastamentos_motivos
from emensageriapro.tabelas.forms import form_esocial_afastamentos_motivos
from emensageriapro.tabelas.forms import form_esocial_desligamentos_motivos
from emensageriapro.tabelas.forms import form_esocial_desligamentos_motivos
from emensageriapro.tabelas.forms import form_esocial_logradouros_tipos
from emensageriapro.tabelas.forms import form_esocial_logradouros_tipos
from emensageriapro.tabelas.forms import form_esocial_naturezas_juridicas
from emensageriapro.tabelas.forms import form_esocial_naturezas_juridicas
from emensageriapro.tabelas.forms import form_esocial_compatibilidades_fpas_classificacoes_tributarias
from emensageriapro.tabelas.forms import form_esocial_compatibilidades_fpas_classificacoes_tributarias
from emensageriapro.tabelas.forms import form_esocial_fatores_risco
from emensageriapro.tabelas.forms import form_esocial_fatores_risco
from emensageriapro.tabelas.forms import form_esocial_codificacoes_acidente_trabalho
from emensageriapro.tabelas.forms import form_esocial_codificacoes_acidente_trabalho
from emensageriapro.tabelas.forms import form_esocial_beneficios_previdenciarios_tipos
from emensageriapro.tabelas.forms import form_esocial_beneficios_previdenciarios_tipos
from emensageriapro.tabelas.forms import form_esocial_beneficios_previdenciarios_cessacao_motivos
from emensageriapro.tabelas.forms import form_esocial_beneficios_previdenciarios_cessacao_motivos
from emensageriapro.tabelas.forms import form_esocial_procedimentos_diagnosticos
from emensageriapro.tabelas.forms import form_esocial_procedimentos_diagnosticos
from emensageriapro.tabelas.forms import form_esocial_atividades_periculosas_insalubres_especiais
from emensageriapro.tabelas.forms import form_esocial_atividades_periculosas_insalubres_especiais
from emensageriapro.tabelas.forms import form_esocial_treinamentos_capacitacoes_exercicios_simulados
from emensageriapro.tabelas.forms import form_esocial_treinamentos_capacitacoes_exercicios_simulados
from emensageriapro.tabelas.forms import form_esocial_programas_planos_documentos
from emensageriapro.tabelas.forms import form_esocial_programas_planos_documentos
from emensageriapro.tabelas.forms import form_efdreinf_pagamentos_codigos
from emensageriapro.tabelas.forms import form_efdreinf_pagamentos_codigos
from emensageriapro.tabelas.forms import form_efdreinf_regras_pagamentos_codigos
from emensageriapro.tabelas.forms import form_efdreinf_regras_pagamentos_codigos
from emensageriapro.tabelas.forms import form_efdreinf_rendimentos_beneficiarios_exterior
from emensageriapro.tabelas.forms import form_efdreinf_rendimentos_beneficiarios_exterior
from emensageriapro.tabelas.forms import form_efdreinf_rendimentos_beneficiarios_exterior_tributacao
from emensageriapro.tabelas.forms import form_efdreinf_rendimentos_beneficiarios_exterior_tributacao
from emensageriapro.tabelas.forms import form_efdreinf_informacoes_beneficiarios_exterior
from emensageriapro.tabelas.forms import form_efdreinf_informacoes_beneficiarios_exterior
from emensageriapro.tabelas.forms import form_efdreinf_classificacao_servicos_prestados
from emensageriapro.tabelas.forms import form_efdreinf_classificacao_servicos_prestados
from emensageriapro.tabelas.forms import form_efdreinf_paises
from emensageriapro.tabelas.forms import form_efdreinf_paises
from emensageriapro.tabelas.forms import form_efdreinf_classificacao_tributaria
from emensageriapro.tabelas.forms import form_efdreinf_classificacao_tributaria
from emensageriapro.tabelas.forms import form_efdreinf_codigos_atividades_produtos_servicos_cprb
from emensageriapro.tabelas.forms import form_efdreinf_codigos_atividades_produtos_servicos_cprb
from emensageriapro.tabelas.forms import form_efdreinf_eventos
from emensageriapro.tabelas.forms import form_efdreinf_eventos
from emensageriapro.mensageiro.forms import form_importacao_arquivos
from emensageriapro.mensageiro.forms import form_importacao_arquivos
from emensageriapro.mensageiro.forms import form_importacao_arquivos
from emensageriapro.mensageiro.forms import form_importacao_arquivos_eventos
from emensageriapro.mensageiro.forms import form_importacao_arquivos_eventos
from emensageriapro.mensageiro.forms import form_transmissor_lote_esocial
from emensageriapro.mensageiro.forms import form_transmissor_lote_esocial
from emensageriapro.mensageiro.forms import form_transmissor_lote_esocial_ocorrencias
from emensageriapro.mensageiro.forms import form_transmissor_lote_esocial_ocorrencias
from emensageriapro.mensageiro.forms import form_transmissor_lote_efdreinf
from emensageriapro.mensageiro.forms import form_transmissor_lote_efdreinf
from emensageriapro.mensageiro.forms import form_transmissor_lote_efdreinf_ocorrencias
from emensageriapro.mensageiro.forms import form_transmissor_lote_efdreinf_ocorrencias
from emensageriapro.mensageiro.forms import form_retornos_eventos
from emensageriapro.mensageiro.forms import form_retornos_eventos
from emensageriapro.mensageiro.forms import form_retornos_eventos_ocorrencias
from emensageriapro.mensageiro.forms import form_retornos_eventos_ocorrencias
from emensageriapro.mensageiro.forms import form_retornos_eventos_horarios
from emensageriapro.mensageiro.forms import form_retornos_eventos_horarios
from emensageriapro.mensageiro.forms import form_retornos_eventos_intervalos
from emensageriapro.mensageiro.forms import form_retornos_eventos_intervalos
from emensageriapro.efdreinf.forms import form_r1000_evtinfocontri
from emensageriapro.efdreinf.forms import form_r1000_evtinfocontri
from emensageriapro.efdreinf.forms import form_r1070_evttabprocesso
from emensageriapro.efdreinf.forms import form_r1070_evttabprocesso
from emensageriapro.efdreinf.forms import form_r2010_evtservtom
from emensageriapro.efdreinf.forms import form_r2010_evtservtom
from emensageriapro.efdreinf.forms import form_r2020_evtservprest
from emensageriapro.efdreinf.forms import form_r2020_evtservprest
from emensageriapro.efdreinf.forms import form_r2030_evtassocdesprec
from emensageriapro.efdreinf.forms import form_r2030_evtassocdesprec
from emensageriapro.efdreinf.forms import form_r2040_evtassocdesprep
from emensageriapro.efdreinf.forms import form_r2040_evtassocdesprep
from emensageriapro.efdreinf.forms import form_r2050_evtcomprod
from emensageriapro.efdreinf.forms import form_r2050_evtcomprod
from emensageriapro.efdreinf.forms import form_r2060_evtcprb
from emensageriapro.efdreinf.forms import form_r2060_evtcprb
from emensageriapro.efdreinf.forms import form_r2070_evtpgtosdivs
from emensageriapro.efdreinf.forms import form_r2070_evtpgtosdivs
from emensageriapro.efdreinf.forms import form_r2098_evtreabreevper
from emensageriapro.efdreinf.forms import form_r2098_evtreabreevper
from emensageriapro.efdreinf.forms import form_r2099_evtfechaevper
from emensageriapro.efdreinf.forms import form_r2099_evtfechaevper
from emensageriapro.efdreinf.forms import form_r3010_evtespdesportivo
from emensageriapro.efdreinf.forms import form_r3010_evtespdesportivo
from emensageriapro.efdreinf.forms import form_r5001_evttotal
from emensageriapro.efdreinf.forms import form_r5001_evttotal
from emensageriapro.efdreinf.forms import form_r5011_evttotalcontrib
from emensageriapro.efdreinf.forms import form_r5011_evttotalcontrib
from emensageriapro.efdreinf.forms import form_r9000_evtexclusao
from emensageriapro.efdreinf.forms import form_r9000_evtexclusao
from emensageriapro.r1000.forms import form_r1000_inclusao
from emensageriapro.r1000.forms import form_r1000_inclusao
from emensageriapro.r1000.forms import form_r1000_inclusao_softhouse
from emensageriapro.r1000.forms import form_r1000_inclusao_softhouse
from emensageriapro.r1000.forms import form_r1000_inclusao_infoefr
from emensageriapro.r1000.forms import form_r1000_inclusao_infoefr
from emensageriapro.r1000.forms import form_r1000_alteracao
from emensageriapro.r1000.forms import form_r1000_alteracao
from emensageriapro.r1000.forms import form_r1000_alteracao_softhouse
from emensageriapro.r1000.forms import form_r1000_alteracao_softhouse
from emensageriapro.r1000.forms import form_r1000_alteracao_infoefr
from emensageriapro.r1000.forms import form_r1000_alteracao_infoefr
from emensageriapro.r1000.forms import form_r1000_alteracao_novavalidade
from emensageriapro.r1000.forms import form_r1000_alteracao_novavalidade
from emensageriapro.r1000.forms import form_r1000_exclusao
from emensageriapro.r1000.forms import form_r1000_exclusao
from emensageriapro.r1070.forms import form_r1070_inclusao
from emensageriapro.r1070.forms import form_r1070_inclusao
from emensageriapro.r1070.forms import form_r1070_inclusao_infosusp
from emensageriapro.r1070.forms import form_r1070_inclusao_infosusp
from emensageriapro.r1070.forms import form_r1070_inclusao_dadosprocjud
from emensageriapro.r1070.forms import form_r1070_inclusao_dadosprocjud
from emensageriapro.r1070.forms import form_r1070_alteracao
from emensageriapro.r1070.forms import form_r1070_alteracao
from emensageriapro.r1070.forms import form_r1070_alteracao_infosusp
from emensageriapro.r1070.forms import form_r1070_alteracao_infosusp
from emensageriapro.r1070.forms import form_r1070_alteracao_dadosprocjud
from emensageriapro.r1070.forms import form_r1070_alteracao_dadosprocjud
from emensageriapro.r1070.forms import form_r1070_alteracao_novavalidade
from emensageriapro.r1070.forms import form_r1070_alteracao_novavalidade
from emensageriapro.r1070.forms import form_r1070_exclusao
from emensageriapro.r1070.forms import form_r1070_exclusao
from emensageriapro.r2010.forms import form_r2010_nfs
from emensageriapro.r2010.forms import form_r2010_nfs
from emensageriapro.r2010.forms import form_r2010_infotpserv
from emensageriapro.r2010.forms import form_r2010_infotpserv
from emensageriapro.r2010.forms import form_r2010_infoprocretpr
from emensageriapro.r2010.forms import form_r2010_infoprocretpr
from emensageriapro.r2010.forms import form_r2010_infoprocretad
from emensageriapro.r2010.forms import form_r2010_infoprocretad
from emensageriapro.r2020.forms import form_r2020_nfs
from emensageriapro.r2020.forms import form_r2020_nfs
from emensageriapro.r2020.forms import form_r2020_infotpserv
from emensageriapro.r2020.forms import form_r2020_infotpserv
from emensageriapro.r2020.forms import form_r2020_infoprocretpr
from emensageriapro.r2020.forms import form_r2020_infoprocretpr
from emensageriapro.r2020.forms import form_r2020_infoprocretad
from emensageriapro.r2020.forms import form_r2020_infoprocretad
from emensageriapro.r2030.forms import form_r2030_recursosrec
from emensageriapro.r2030.forms import form_r2030_recursosrec
from emensageriapro.r2030.forms import form_r2030_inforecurso
from emensageriapro.r2030.forms import form_r2030_inforecurso
from emensageriapro.r2030.forms import form_r2030_infoproc
from emensageriapro.r2030.forms import form_r2030_infoproc
from emensageriapro.r2040.forms import form_r2040_recursosrep
from emensageriapro.r2040.forms import form_r2040_recursosrep
from emensageriapro.r2040.forms import form_r2040_inforecurso
from emensageriapro.r2040.forms import form_r2040_inforecurso
from emensageriapro.r2040.forms import form_r2040_infoproc
from emensageriapro.r2040.forms import form_r2040_infoproc
from emensageriapro.r2050.forms import form_r2050_tipocom
from emensageriapro.r2050.forms import form_r2050_tipocom
from emensageriapro.r2050.forms import form_r2050_infoproc
from emensageriapro.r2050.forms import form_r2050_infoproc
from emensageriapro.r2060.forms import form_r2060_tipocod
from emensageriapro.r2060.forms import form_r2060_tipocod
from emensageriapro.r2060.forms import form_r2060_tipoajuste
from emensageriapro.r2060.forms import form_r2060_tipoajuste
from emensageriapro.r2060.forms import form_r2060_infoproc
from emensageriapro.r2060.forms import form_r2060_infoproc
from emensageriapro.r2070.forms import form_r2070_inforesidext
from emensageriapro.r2070.forms import form_r2070_inforesidext
from emensageriapro.r2070.forms import form_r2070_infomolestia
from emensageriapro.r2070.forms import form_r2070_infomolestia
from emensageriapro.r2070.forms import form_r2070_ideestab
from emensageriapro.r2070.forms import form_r2070_ideestab
from emensageriapro.r2070.forms import form_r2070_pgtoresidbr
from emensageriapro.r2070.forms import form_r2070_pgtoresidbr
from emensageriapro.r2070.forms import form_r2070_pgtopf
from emensageriapro.r2070.forms import form_r2070_pgtopf
from emensageriapro.r2070.forms import form_r2070_detdeducao
from emensageriapro.r2070.forms import form_r2070_detdeducao
from emensageriapro.r2070.forms import form_r2070_rendisento
from emensageriapro.r2070.forms import form_r2070_rendisento
from emensageriapro.r2070.forms import form_r2070_detcompet
from emensageriapro.r2070.forms import form_r2070_detcompet
from emensageriapro.r2070.forms import form_r2070_compjud
from emensageriapro.r2070.forms import form_r2070_compjud
from emensageriapro.r2070.forms import form_r2070_inforra
from emensageriapro.r2070.forms import form_r2070_inforra
from emensageriapro.r2070.forms import form_r2070_inforra_despprocjud
from emensageriapro.r2070.forms import form_r2070_inforra_despprocjud
from emensageriapro.r2070.forms import form_r2070_inforra_ideadvogado
from emensageriapro.r2070.forms import form_r2070_inforra_ideadvogado
from emensageriapro.r2070.forms import form_r2070_infoprocjud
from emensageriapro.r2070.forms import form_r2070_infoprocjud
from emensageriapro.r2070.forms import form_r2070_infoprocjud_despprocjud
from emensageriapro.r2070.forms import form_r2070_infoprocjud_despprocjud
from emensageriapro.r2070.forms import form_r2070_infoprocjud_ideadvogado
from emensageriapro.r2070.forms import form_r2070_infoprocjud_ideadvogado
from emensageriapro.r2070.forms import form_r2070_infoprocjud_origemrecursos
from emensageriapro.r2070.forms import form_r2070_infoprocjud_origemrecursos
from emensageriapro.r2070.forms import form_r2070_depjudicial
from emensageriapro.r2070.forms import form_r2070_depjudicial
from emensageriapro.r2070.forms import form_r2070_pgtopj
from emensageriapro.r2070.forms import form_r2070_pgtopj
from emensageriapro.r2070.forms import form_r2070_pgtopj_infoprocjud
from emensageriapro.r2070.forms import form_r2070_pgtopj_infoprocjud
from emensageriapro.r2070.forms import form_r2070_pgtopj_despprocjud
from emensageriapro.r2070.forms import form_r2070_pgtopj_despprocjud
from emensageriapro.r2070.forms import form_r2070_pgtopj_ideadvogado
from emensageriapro.r2070.forms import form_r2070_pgtopj_ideadvogado
from emensageriapro.r2070.forms import form_r2070_pgtopj_origemrecursos
from emensageriapro.r2070.forms import form_r2070_pgtopj_origemrecursos
from emensageriapro.r2070.forms import form_r2070_pgtoresidext
from emensageriapro.r2070.forms import form_r2070_pgtoresidext
from emensageriapro.r2099.forms import form_r2099_iderespinf
from emensageriapro.r2099.forms import form_r2099_iderespinf
from emensageriapro.r3010.forms import form_r3010_ideestab
from emensageriapro.r3010.forms import form_r3010_ideestab
from emensageriapro.r3010.forms import form_r3010_boletim
from emensageriapro.r3010.forms import form_r3010_boletim
from emensageriapro.r3010.forms import form_r3010_receitaingressos
from emensageriapro.r3010.forms import form_r3010_receitaingressos
from emensageriapro.r3010.forms import form_r3010_outrasreceitas
from emensageriapro.r3010.forms import form_r3010_outrasreceitas
from emensageriapro.r3010.forms import form_r3010_infoproc
from emensageriapro.r3010.forms import form_r3010_infoproc
from emensageriapro.r5001.forms import form_r5001_regocorrs
from emensageriapro.r5001.forms import form_r5001_regocorrs
from emensageriapro.r5001.forms import form_r5001_infototal
from emensageriapro.r5001.forms import form_r5001_infototal
from emensageriapro.r5001.forms import form_r5001_rtom
from emensageriapro.r5001.forms import form_r5001_rtom
from emensageriapro.r5001.forms import form_r5001_infocrtom
from emensageriapro.r5001.forms import form_r5001_infocrtom
from emensageriapro.r5001.forms import form_r5001_rprest
from emensageriapro.r5001.forms import form_r5001_rprest
from emensageriapro.r5001.forms import form_r5001_rrecrepad
from emensageriapro.r5001.forms import form_r5001_rrecrepad
from emensageriapro.r5001.forms import form_r5001_rcoml
from emensageriapro.r5001.forms import form_r5001_rcoml
from emensageriapro.r5001.forms import form_r5001_rcprb
from emensageriapro.r5001.forms import form_r5001_rcprb
from emensageriapro.r5001.forms import form_r5001_rrecespetdesp
from emensageriapro.r5001.forms import form_r5001_rrecespetdesp
from emensageriapro.r5011.forms import form_r5011_regocorrs
from emensageriapro.r5011.forms import form_r5011_regocorrs
from emensageriapro.r5011.forms import form_r5011_infototalcontrib
from emensageriapro.r5011.forms import form_r5011_infototalcontrib
from emensageriapro.r5011.forms import form_r5011_rtom
from emensageriapro.r5011.forms import form_r5011_rtom
from emensageriapro.r5011.forms import form_r5011_infocrtom
from emensageriapro.r5011.forms import form_r5011_infocrtom
from emensageriapro.r5011.forms import form_r5011_rprest
from emensageriapro.r5011.forms import form_r5011_rprest
from emensageriapro.r5011.forms import form_r5011_rrecrepad
from emensageriapro.r5011.forms import form_r5011_rrecrepad
from emensageriapro.r5011.forms import form_r5011_rcoml
from emensageriapro.r5011.forms import form_r5011_rcoml
from emensageriapro.r5011.forms import form_r5011_rcprb
from emensageriapro.r5011.forms import form_r5011_rcprb
from emensageriapro.esocial.forms import form_s1000_evtinfoempregador
from emensageriapro.esocial.forms import form_s1000_evtinfoempregador
from emensageriapro.esocial.forms import form_s1005_evttabestab
from emensageriapro.esocial.forms import form_s1005_evttabestab
from emensageriapro.esocial.forms import form_s1010_evttabrubrica
from emensageriapro.esocial.forms import form_s1010_evttabrubrica
from emensageriapro.esocial.forms import form_s1020_evttablotacao
from emensageriapro.esocial.forms import form_s1020_evttablotacao
from emensageriapro.esocial.forms import form_s1030_evttabcargo
from emensageriapro.esocial.forms import form_s1030_evttabcargo
from emensageriapro.esocial.forms import form_s1035_evttabcarreira
from emensageriapro.esocial.forms import form_s1035_evttabcarreira
from emensageriapro.esocial.forms import form_s1040_evttabfuncao
from emensageriapro.esocial.forms import form_s1040_evttabfuncao
from emensageriapro.esocial.forms import form_s1050_evttabhortur
from emensageriapro.esocial.forms import form_s1050_evttabhortur
from emensageriapro.esocial.forms import form_s1060_evttabambiente
from emensageriapro.esocial.forms import form_s1060_evttabambiente
from emensageriapro.esocial.forms import form_s1065_evttabequipamento
from emensageriapro.esocial.forms import form_s1065_evttabequipamento
from emensageriapro.esocial.forms import form_s1070_evttabprocesso
from emensageriapro.esocial.forms import form_s1070_evttabprocesso
from emensageriapro.esocial.forms import form_s1080_evttaboperport
from emensageriapro.esocial.forms import form_s1080_evttaboperport
from emensageriapro.esocial.forms import form_s1200_evtremun
from emensageriapro.esocial.forms import form_s1200_evtremun
from emensageriapro.esocial.forms import form_s1202_evtrmnrpps
from emensageriapro.esocial.forms import form_s1202_evtrmnrpps
from emensageriapro.esocial.forms import form_s1207_evtbenprrp
from emensageriapro.esocial.forms import form_s1207_evtbenprrp
from emensageriapro.esocial.forms import form_s1210_evtpgtos
from emensageriapro.esocial.forms import form_s1210_evtpgtos
from emensageriapro.esocial.forms import form_s1250_evtaqprod
from emensageriapro.esocial.forms import form_s1250_evtaqprod
from emensageriapro.esocial.forms import form_s1260_evtcomprod
from emensageriapro.esocial.forms import form_s1260_evtcomprod
from emensageriapro.esocial.forms import form_s1270_evtcontratavnp
from emensageriapro.esocial.forms import form_s1270_evtcontratavnp
from emensageriapro.esocial.forms import form_s1280_evtinfocomplper
from emensageriapro.esocial.forms import form_s1280_evtinfocomplper
from emensageriapro.esocial.forms import form_s1295_evttotconting
from emensageriapro.esocial.forms import form_s1295_evttotconting
from emensageriapro.esocial.forms import form_s1298_evtreabreevper
from emensageriapro.esocial.forms import form_s1298_evtreabreevper
from emensageriapro.esocial.forms import form_s1299_evtfechaevper
from emensageriapro.esocial.forms import form_s1299_evtfechaevper
from emensageriapro.esocial.forms import form_s1300_evtcontrsindpatr
from emensageriapro.esocial.forms import form_s1300_evtcontrsindpatr
from emensageriapro.esocial.forms import form_s2190_evtadmprelim
from emensageriapro.esocial.forms import form_s2190_evtadmprelim
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.forms import form_s2231_evtcessao
from emensageriapro.esocial.forms import form_s2231_evtcessao
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.forms import form_s2241_evtinsapo
from emensageriapro.esocial.forms import form_s2241_evtinsapo
from emensageriapro.esocial.forms import form_s2245_evttreicap
from emensageriapro.esocial.forms import form_s2245_evttreicap
from emensageriapro.esocial.forms import form_s2250_evtavprevio
from emensageriapro.esocial.forms import form_s2250_evtavprevio
from emensageriapro.esocial.forms import form_s2260_evtconvinterm
from emensageriapro.esocial.forms import form_s2260_evtconvinterm
from emensageriapro.esocial.forms import form_s2298_evtreintegr
from emensageriapro.esocial.forms import form_s2298_evtreintegr
from emensageriapro.esocial.forms import form_s2299_evtdeslig
from emensageriapro.esocial.forms import form_s2299_evtdeslig
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.esocial.forms import form_s2400_evtcdbenefin
from emensageriapro.esocial.forms import form_s2400_evtcdbenefin
from emensageriapro.esocial.forms import form_s2405_evtcdbenefalt
from emensageriapro.esocial.forms import form_s2405_evtcdbenefalt
from emensageriapro.esocial.forms import form_s2410_evtcdbenin
from emensageriapro.esocial.forms import form_s2410_evtcdbenin
from emensageriapro.esocial.forms import form_s2416_evtcdbenalt
from emensageriapro.esocial.forms import form_s2416_evtcdbenalt
from emensageriapro.esocial.forms import form_s2420_evtcdbenterm
from emensageriapro.esocial.forms import form_s2420_evtcdbenterm
from emensageriapro.esocial.forms import form_s3000_evtexclusao
from emensageriapro.esocial.forms import form_s3000_evtexclusao
from emensageriapro.esocial.forms import form_s5001_evtbasestrab
from emensageriapro.esocial.forms import form_s5001_evtbasestrab
from emensageriapro.esocial.forms import form_s5002_evtirrfbenef
from emensageriapro.esocial.forms import form_s5002_evtirrfbenef
from emensageriapro.esocial.forms import form_s5011_evtcs
from emensageriapro.esocial.forms import form_s5011_evtcs
from emensageriapro.esocial.forms import form_s5012_evtirrf
from emensageriapro.esocial.forms import form_s5012_evtirrf
from emensageriapro.s1000.forms import form_s1000_inclusao
from emensageriapro.s1000.forms import form_s1000_inclusao
from emensageriapro.s1000.forms import form_s1000_inclusao_dadosisencao
from emensageriapro.s1000.forms import form_s1000_inclusao_dadosisencao
from emensageriapro.s1000.forms import form_s1000_inclusao_infoop
from emensageriapro.s1000.forms import form_s1000_inclusao_infoop
from emensageriapro.s1000.forms import form_s1000_inclusao_infoefr
from emensageriapro.s1000.forms import form_s1000_inclusao_infoefr
from emensageriapro.s1000.forms import form_s1000_inclusao_infoente
from emensageriapro.s1000.forms import form_s1000_inclusao_infoente
from emensageriapro.s1000.forms import form_s1000_inclusao_infoorginternacional
from emensageriapro.s1000.forms import form_s1000_inclusao_infoorginternacional
from emensageriapro.s1000.forms import form_s1000_inclusao_softwarehouse
from emensageriapro.s1000.forms import form_s1000_inclusao_softwarehouse
from emensageriapro.s1000.forms import form_s1000_inclusao_situacaopj
from emensageriapro.s1000.forms import form_s1000_inclusao_situacaopj
from emensageriapro.s1000.forms import form_s1000_inclusao_situacaopf
from emensageriapro.s1000.forms import form_s1000_inclusao_situacaopf
from emensageriapro.s1000.forms import form_s1000_alteracao
from emensageriapro.s1000.forms import form_s1000_alteracao
from emensageriapro.s1000.forms import form_s1000_alteracao_dadosisencao
from emensageriapro.s1000.forms import form_s1000_alteracao_dadosisencao
from emensageriapro.s1000.forms import form_s1000_alteracao_infoop
from emensageriapro.s1000.forms import form_s1000_alteracao_infoop
from emensageriapro.s1000.forms import form_s1000_alteracao_infoefr
from emensageriapro.s1000.forms import form_s1000_alteracao_infoefr
from emensageriapro.s1000.forms import form_s1000_alteracao_infoente
from emensageriapro.s1000.forms import form_s1000_alteracao_infoente
from emensageriapro.s1000.forms import form_s1000_alteracao_infoorginternacional
from emensageriapro.s1000.forms import form_s1000_alteracao_infoorginternacional
from emensageriapro.s1000.forms import form_s1000_alteracao_softwarehouse
from emensageriapro.s1000.forms import form_s1000_alteracao_softwarehouse
from emensageriapro.s1000.forms import form_s1000_alteracao_situacaopj
from emensageriapro.s1000.forms import form_s1000_alteracao_situacaopj
from emensageriapro.s1000.forms import form_s1000_alteracao_situacaopf
from emensageriapro.s1000.forms import form_s1000_alteracao_situacaopf
from emensageriapro.s1000.forms import form_s1000_alteracao_novavalidade
from emensageriapro.s1000.forms import form_s1000_alteracao_novavalidade
from emensageriapro.s1000.forms import form_s1000_exclusao
from emensageriapro.s1000.forms import form_s1000_exclusao
from emensageriapro.s1005.forms import form_s1005_inclusao
from emensageriapro.s1005.forms import form_s1005_inclusao
from emensageriapro.s1005.forms import form_s1005_inclusao_procadmjudrat
from emensageriapro.s1005.forms import form_s1005_inclusao_procadmjudrat
from emensageriapro.s1005.forms import form_s1005_inclusao_procadmjudfap
from emensageriapro.s1005.forms import form_s1005_inclusao_procadmjudfap
from emensageriapro.s1005.forms import form_s1005_inclusao_infocaepf
from emensageriapro.s1005.forms import form_s1005_inclusao_infocaepf
from emensageriapro.s1005.forms import form_s1005_inclusao_infoobra
from emensageriapro.s1005.forms import form_s1005_inclusao_infoobra
from emensageriapro.s1005.forms import form_s1005_inclusao_infoenteduc
from emensageriapro.s1005.forms import form_s1005_inclusao_infoenteduc
from emensageriapro.s1005.forms import form_s1005_inclusao_infopcd
from emensageriapro.s1005.forms import form_s1005_inclusao_infopcd
from emensageriapro.s1005.forms import form_s1005_inclusao_infosst
from emensageriapro.s1005.forms import form_s1005_inclusao_infosst
from emensageriapro.s1005.forms import form_s1005_alteracao
from emensageriapro.s1005.forms import form_s1005_alteracao
from emensageriapro.s1005.forms import form_s1005_alteracao_procadmjudrat
from emensageriapro.s1005.forms import form_s1005_alteracao_procadmjudrat
from emensageriapro.s1005.forms import form_s1005_alteracao_procadmjudfap
from emensageriapro.s1005.forms import form_s1005_alteracao_procadmjudfap
from emensageriapro.s1005.forms import form_s1005_alteracao_infocaepf
from emensageriapro.s1005.forms import form_s1005_alteracao_infocaepf
from emensageriapro.s1005.forms import form_s1005_alteracao_infoobra
from emensageriapro.s1005.forms import form_s1005_alteracao_infoobra
from emensageriapro.s1005.forms import form_s1005_alteracao_infoenteduc
from emensageriapro.s1005.forms import form_s1005_alteracao_infoenteduc
from emensageriapro.s1005.forms import form_s1005_alteracao_infopcd
from emensageriapro.s1005.forms import form_s1005_alteracao_infopcd
from emensageriapro.s1005.forms import form_s1005_alteracao_novavalidade
from emensageriapro.s1005.forms import form_s1005_alteracao_novavalidade
from emensageriapro.s1005.forms import form_s1005_alteracao_infosst
from emensageriapro.s1005.forms import form_s1005_alteracao_infosst
from emensageriapro.s1005.forms import form_s1005_exclusao
from emensageriapro.s1005.forms import form_s1005_exclusao
from emensageriapro.s1010.forms import form_s1010_inclusao
from emensageriapro.s1010.forms import form_s1010_inclusao
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessocp
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessocp
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessoirrf
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessoirrf
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessofgts
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessofgts
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessosind
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessosind
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessocprp
from emensageriapro.s1010.forms import form_s1010_inclusao_ideprocessocprp
from emensageriapro.s1010.forms import form_s1010_alteracao
from emensageriapro.s1010.forms import form_s1010_alteracao
from emensageriapro.s1050.forms import form_s1050_exclusao
from emensageriapro.s1050.forms import form_s1050_exclusao
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessocp
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessocp
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessoirrf
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessoirrf
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessofgts
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessofgts
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessosind
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessosind
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessocprp
from emensageriapro.s1010.forms import form_s1010_alteracao_ideprocessocprp
from emensageriapro.s1010.forms import form_s1010_alteracao_novavalidade
from emensageriapro.s1010.forms import form_s1010_alteracao_novavalidade
from emensageriapro.s1010.forms import form_s1010_exclusao
from emensageriapro.s1010.forms import form_s1010_exclusao
from emensageriapro.s1020.forms import form_s1020_inclusao
from emensageriapro.s1020.forms import form_s1020_inclusao
from emensageriapro.s1020.forms import form_s1020_inclusao_infoprocjudterceiros
from emensageriapro.s1020.forms import form_s1020_inclusao_infoprocjudterceiros
from emensageriapro.s1020.forms import form_s1020_inclusao_procjudterceiro
from emensageriapro.s1020.forms import form_s1020_inclusao_procjudterceiro
from emensageriapro.s1020.forms import form_s1020_inclusao_infoemprparcial
from emensageriapro.s1020.forms import form_s1020_inclusao_infoemprparcial
from emensageriapro.s1020.forms import form_s1020_alteracao
from emensageriapro.s1020.forms import form_s1020_alteracao
from emensageriapro.s1020.forms import form_s1020_alteracao_infoprocjudterceiros
from emensageriapro.s1020.forms import form_s1020_alteracao_infoprocjudterceiros
from emensageriapro.s1020.forms import form_s1020_alteracao_procjudterceiro
from emensageriapro.s1020.forms import form_s1020_alteracao_procjudterceiro
from emensageriapro.s1020.forms import form_s1020_alteracao_infoemprparcial
from emensageriapro.s1020.forms import form_s1020_alteracao_infoemprparcial
from emensageriapro.s1020.forms import form_s1020_alteracao_novavalidade
from emensageriapro.s1020.forms import form_s1020_alteracao_novavalidade
from emensageriapro.s1020.forms import form_s1020_exclusao
from emensageriapro.s1020.forms import form_s1020_exclusao
from emensageriapro.s1030.forms import form_s1030_inclusao
from emensageriapro.s1030.forms import form_s1030_inclusao
from emensageriapro.s1030.forms import form_s1030_inclusao_cargopublico
from emensageriapro.s1030.forms import form_s1030_inclusao_cargopublico
from emensageriapro.s1030.forms import form_s1030_alteracao
from emensageriapro.s1030.forms import form_s1030_alteracao
from emensageriapro.s1030.forms import form_s1030_alteracao_cargopublico
from emensageriapro.s1030.forms import form_s1030_alteracao_cargopublico
from emensageriapro.s1030.forms import form_s1030_alteracao_novavalidade
from emensageriapro.s1030.forms import form_s1030_alteracao_novavalidade
from emensageriapro.s1030.forms import form_s1030_exclusao
from emensageriapro.s1030.forms import form_s1030_exclusao
from emensageriapro.s1035.forms import form_s1035_inclusao
from emensageriapro.s1035.forms import form_s1035_inclusao
from emensageriapro.s1035.forms import form_s1035_alteracao
from emensageriapro.s1035.forms import form_s1035_alteracao
from emensageriapro.s1035.forms import form_s1035_alteracao_novavalidade
from emensageriapro.s1035.forms import form_s1035_alteracao_novavalidade
from emensageriapro.s1035.forms import form_s1035_exclusao
from emensageriapro.s1035.forms import form_s1035_exclusao
from emensageriapro.s1040.forms import form_s1040_inclusao
from emensageriapro.s1040.forms import form_s1040_inclusao
from emensageriapro.s1040.forms import form_s1040_alteracao
from emensageriapro.s1040.forms import form_s1040_alteracao
from emensageriapro.s1040.forms import form_s1040_alteracao_novavalidade
from emensageriapro.s1040.forms import form_s1040_alteracao_novavalidade
from emensageriapro.s1040.forms import form_s1040_exclusao
from emensageriapro.s1040.forms import form_s1040_exclusao
from emensageriapro.s1050.forms import form_s1050_inclusao
from emensageriapro.s1050.forms import form_s1050_inclusao
from emensageriapro.s1050.forms import form_s1050_inclusao_horariointervalo
from emensageriapro.s1050.forms import form_s1050_inclusao_horariointervalo
from emensageriapro.s1050.forms import form_s1050_alteracao
from emensageriapro.s1050.forms import form_s1050_alteracao
from emensageriapro.s1050.forms import form_s1050_alteracao_horariointervalo
from emensageriapro.s1050.forms import form_s1050_alteracao_horariointervalo
from emensageriapro.s1050.forms import form_s1050_alteracao_novavalidade
from emensageriapro.s1050.forms import form_s1050_alteracao_novavalidade
from emensageriapro.s1060.forms import form_s1060_inclusao
from emensageriapro.s1060.forms import form_s1060_inclusao
from emensageriapro.s1060.forms import form_s1060_inclusao_fatorrisco
from emensageriapro.s1060.forms import form_s1060_inclusao_fatorrisco
from emensageriapro.s1060.forms import form_s1060_alteracao
from emensageriapro.s1060.forms import form_s1060_alteracao
from emensageriapro.s1060.forms import form_s1060_alteracao_fatorrisco
from emensageriapro.s1060.forms import form_s1060_alteracao_fatorrisco
from emensageriapro.s1060.forms import form_s1060_alteracao_novavalidade
from emensageriapro.s1060.forms import form_s1060_alteracao_novavalidade
from emensageriapro.s1060.forms import form_s1060_exclusao
from emensageriapro.s1060.forms import form_s1060_exclusao
from emensageriapro.s1065.forms import form_s1065_inclusao
from emensageriapro.s1065.forms import form_s1065_inclusao
from emensageriapro.s1065.forms import form_s1065_alteracao
from emensageriapro.s1065.forms import form_s1065_alteracao
from emensageriapro.s1065.forms import form_s1065_alteracao_novavalidade
from emensageriapro.s1065.forms import form_s1065_alteracao_novavalidade
from emensageriapro.s1065.forms import form_s1065_exclusao
from emensageriapro.s1065.forms import form_s1065_exclusao
from emensageriapro.s1070.forms import form_s1070_inclusao
from emensageriapro.s1070.forms import form_s1070_inclusao
from emensageriapro.s1070.forms import form_s1070_inclusao_dadosprocjud
from emensageriapro.s1070.forms import form_s1070_inclusao_dadosprocjud
from emensageriapro.s1070.forms import form_s1070_inclusao_infosusp
from emensageriapro.s1070.forms import form_s1070_inclusao_infosusp
from emensageriapro.s1070.forms import form_s1070_alteracao
from emensageriapro.s1070.forms import form_s1070_alteracao
from emensageriapro.s1070.forms import form_s1070_alteracao_dadosprocjud
from emensageriapro.s1070.forms import form_s1070_alteracao_dadosprocjud
from emensageriapro.s1070.forms import form_s1070_alteracao_infosusp
from emensageriapro.s1070.forms import form_s1070_alteracao_infosusp
from emensageriapro.s1070.forms import form_s1070_alteracao_novavalidade
from emensageriapro.s1070.forms import form_s1070_alteracao_novavalidade
from emensageriapro.s1070.forms import form_s1070_exclusao
from emensageriapro.s1070.forms import form_s1070_exclusao
from emensageriapro.s1080.forms import form_s1080_inclusao
from emensageriapro.s1080.forms import form_s1080_inclusao
from emensageriapro.s1080.forms import form_s1080_alteracao
from emensageriapro.s1080.forms import form_s1080_alteracao
from emensageriapro.s1080.forms import form_s1080_alteracao_novavalidade
from emensageriapro.s1080.forms import form_s1080_alteracao_novavalidade
from emensageriapro.s1080.forms import form_s1080_exclusao
from emensageriapro.s1080.forms import form_s1080_exclusao
from emensageriapro.s1200.forms import form_s1200_infomv
from emensageriapro.s1200.forms import form_s1200_infomv
from emensageriapro.s1200.forms import form_s1200_remunoutrempr
from emensageriapro.s1200.forms import form_s1200_remunoutrempr
from emensageriapro.s1200.forms import form_s1200_infocomplem
from emensageriapro.s1200.forms import form_s1200_infocomplem
from emensageriapro.s1200.forms import form_s1200_sucessaovinc
from emensageriapro.s1200.forms import form_s1200_sucessaovinc
from emensageriapro.s1200.forms import form_s1200_procjudtrab
from emensageriapro.s1200.forms import form_s1200_procjudtrab
from emensageriapro.s1200.forms import form_s1200_infointerm
from emensageriapro.s1200.forms import form_s1200_infointerm
from emensageriapro.s1200.forms import form_s1200_dmdev
from emensageriapro.s1200.forms import form_s1200_dmdev
from emensageriapro.s1200.forms import form_s1200_infoperapur
from emensageriapro.s1200.forms import form_s1200_infoperapur
from emensageriapro.s1200.forms import form_s1200_infoperapur_ideestablot
from emensageriapro.s1200.forms import form_s1200_infoperapur_ideestablot
from emensageriapro.s1200.forms import form_s1200_infoperapur_remunperapur
from emensageriapro.s1200.forms import form_s1200_infoperapur_remunperapur
from emensageriapro.s1200.forms import form_s1200_infoperapur_itensremun
from emensageriapro.s1200.forms import form_s1200_infoperapur_itensremun
from emensageriapro.s1200.forms import form_s1200_infoperapur_infosaudecolet
from emensageriapro.s1200.forms import form_s1200_infoperapur_infosaudecolet
from emensageriapro.s1200.forms import form_s1200_infoperapur_detoper
from emensageriapro.s1200.forms import form_s1200_infoperapur_detoper
from emensageriapro.s1200.forms import form_s1200_infoperapur_detplano
from emensageriapro.s1200.forms import form_s1200_infoperapur_detplano
from emensageriapro.s1200.forms import form_s1200_infoperapur_infoagnocivo
from emensageriapro.s1200.forms import form_s1200_infoperapur_infoagnocivo
from emensageriapro.s1200.forms import form_s1200_infoperapur_infotrabinterm
from emensageriapro.s1200.forms import form_s1200_infoperapur_infotrabinterm
from emensageriapro.s1200.forms import form_s1200_infoperant
from emensageriapro.s1200.forms import form_s1200_infoperant
from emensageriapro.s1200.forms import form_s1200_infoperant_ideadc
from emensageriapro.s1200.forms import form_s1200_infoperant_ideadc
from emensageriapro.s1200.forms import form_s1200_infoperant_ideperiodo
from emensageriapro.s1200.forms import form_s1200_infoperant_ideperiodo
from emensageriapro.s1200.forms import form_s1200_infoperant_ideestablot
from emensageriapro.s1200.forms import form_s1200_infoperant_ideestablot
from emensageriapro.s1200.forms import form_s1200_infoperant_remunperant
from emensageriapro.s1200.forms import form_s1200_infoperant_remunperant
from emensageriapro.s1200.forms import form_s1200_infoperant_itensremun
from emensageriapro.s1200.forms import form_s1200_infoperant_itensremun
from emensageriapro.s1200.forms import form_s1200_infoperant_infoagnocivo
from emensageriapro.s1200.forms import form_s1200_infoperant_infoagnocivo
from emensageriapro.s1200.forms import form_s1200_infoperant_infotrabinterm
from emensageriapro.s1200.forms import form_s1200_infoperant_infotrabinterm
from emensageriapro.s1202.forms import form_s1202_infoperant_remunperant
from emensageriapro.s1202.forms import form_s1202_infoperant_remunperant
from emensageriapro.s1200.forms import form_s1200_infoperant_infocomplcont
from emensageriapro.s1200.forms import form_s1200_infoperant_infocomplcont
from emensageriapro.s1202.forms import form_s1202_procjudtrab
from emensageriapro.s1202.forms import form_s1202_procjudtrab
from emensageriapro.s1202.forms import form_s1202_dmdev
from emensageriapro.s1202.forms import form_s1202_dmdev
from emensageriapro.s1202.forms import form_s1202_infoperapur
from emensageriapro.s1202.forms import form_s1202_infoperapur
from emensageriapro.s1202.forms import form_s1202_infoperapur_ideestab
from emensageriapro.s1202.forms import form_s1202_infoperapur_ideestab
from emensageriapro.s1202.forms import form_s1202_infoperapur_remunperapur
from emensageriapro.s1202.forms import form_s1202_infoperapur_remunperapur
from emensageriapro.s1202.forms import form_s1202_infoperapur_itensremun
from emensageriapro.s1202.forms import form_s1202_infoperapur_itensremun
from emensageriapro.s1202.forms import form_s1202_infoperapur_infosaudecolet
from emensageriapro.s1202.forms import form_s1202_infoperapur_infosaudecolet
from emensageriapro.s1202.forms import form_s1202_infoperapur_detoper
from emensageriapro.s1202.forms import form_s1202_infoperapur_detoper
from emensageriapro.s1202.forms import form_s1202_infoperapur_detplano
from emensageriapro.s1202.forms import form_s1202_infoperapur_detplano
from emensageriapro.s1202.forms import form_s1202_infoperant
from emensageriapro.s1202.forms import form_s1202_infoperant
from emensageriapro.s1202.forms import form_s1202_infoperant_ideadc
from emensageriapro.s1202.forms import form_s1202_infoperant_ideadc
from emensageriapro.s1202.forms import form_s1202_infoperant_ideperiodo
from emensageriapro.s1202.forms import form_s1202_infoperant_ideperiodo
from emensageriapro.s1202.forms import form_s1202_infoperant_ideestab
from emensageriapro.s1202.forms import form_s1202_infoperant_ideestab
from emensageriapro.s1202.forms import form_s1202_infoperant_itensremun
from emensageriapro.s1202.forms import form_s1202_infoperant_itensremun
from emensageriapro.s1207.forms import form_s1207_procjudtrab
from emensageriapro.s1207.forms import form_s1207_procjudtrab
from emensageriapro.s1207.forms import form_s1207_dmdev
from emensageriapro.s1207.forms import form_s1207_dmdev
from emensageriapro.s1207.forms import form_s1207_itens
from emensageriapro.s1207.forms import form_s1207_itens
from emensageriapro.s1207.forms import form_s1207_infoperapur
from emensageriapro.s1207.forms import form_s1207_infoperapur
from emensageriapro.s1207.forms import form_s1207_infoperapur_ideestab
from emensageriapro.s1207.forms import form_s1207_infoperapur_ideestab
from emensageriapro.s1207.forms import form_s1207_infoperapur_remunperapur
from emensageriapro.s1207.forms import form_s1207_infoperapur_remunperapur
from emensageriapro.s1207.forms import form_s1207_infoperapur_itensremun
from emensageriapro.s1207.forms import form_s1207_infoperapur_itensremun
from emensageriapro.s1207.forms import form_s1207_infoperant
from emensageriapro.s1207.forms import form_s1207_infoperant
from emensageriapro.s1207.forms import form_s1207_infoperant_ideadc
from emensageriapro.s1207.forms import form_s1207_infoperant_ideadc
from emensageriapro.s1207.forms import form_s1207_infoperant_ideperiodo
from emensageriapro.s1207.forms import form_s1207_infoperant_ideperiodo
from emensageriapro.s1207.forms import form_s1207_infoperant_ideestab
from emensageriapro.s1207.forms import form_s1207_infoperant_ideestab
from emensageriapro.s1207.forms import form_s1207_infoperant_remunperant
from emensageriapro.s1207.forms import form_s1207_infoperant_remunperant
from emensageriapro.s1207.forms import form_s1207_infoperant_itensremun
from emensageriapro.s1207.forms import form_s1207_infoperant_itensremun
from emensageriapro.s1210.forms import form_s1210_deps
from emensageriapro.s1210.forms import form_s1210_deps
from emensageriapro.s1210.forms import form_s1210_infopgto
from emensageriapro.s1210.forms import form_s1210_infopgto
from emensageriapro.s1210.forms import form_s1210_detpgtofl
from emensageriapro.s1210.forms import form_s1210_detpgtofl
from emensageriapro.s1210.forms import form_s1210_detpgtofl_retpgtotot
from emensageriapro.s1210.forms import form_s1210_detpgtofl_retpgtotot
from emensageriapro.s1210.forms import form_s1210_detpgtofl_penalim
from emensageriapro.s1210.forms import form_s1210_detpgtofl_penalim
from emensageriapro.s1210.forms import form_s1210_detpgtofl_infopgtoparc
from emensageriapro.s1210.forms import form_s1210_detpgtofl_infopgtoparc
from emensageriapro.s1210.forms import form_s1210_detpgtobenpr
from emensageriapro.s1210.forms import form_s1210_detpgtobenpr
from emensageriapro.s1210.forms import form_s1210_detpgtobenpr_retpgtotot
from emensageriapro.s1210.forms import form_s1210_detpgtobenpr_retpgtotot
from emensageriapro.s1210.forms import form_s1210_detpgtobenpr_infopgtoparc
from emensageriapro.s1210.forms import form_s1210_detpgtobenpr_infopgtoparc
from emensageriapro.s1210.forms import form_s1210_detpgtofer
from emensageriapro.s1210.forms import form_s1210_detpgtofer
from emensageriapro.s1210.forms import form_s1210_detpgtofer_detrubrfer
from emensageriapro.s1210.forms import form_s1210_detpgtofer_detrubrfer
from emensageriapro.s1210.forms import form_s1210_detpgtofer_penalim
from emensageriapro.s1210.forms import form_s1210_detpgtofer_penalim
from emensageriapro.s1210.forms import form_s1210_detpgtoant
from emensageriapro.s1210.forms import form_s1210_detpgtoant
from emensageriapro.s1210.forms import form_s1210_detpgtoant_infopgtoant
from emensageriapro.s1210.forms import form_s1210_detpgtoant_infopgtoant
from emensageriapro.s1210.forms import form_s1210_idepgtoext
from emensageriapro.s1210.forms import form_s1210_idepgtoext
from emensageriapro.s1250.forms import form_s1250_tpaquis
from emensageriapro.s1250.forms import form_s1250_tpaquis
from emensageriapro.s1250.forms import form_s1250_ideprodutor
from emensageriapro.s1250.forms import form_s1250_ideprodutor
from emensageriapro.s1250.forms import form_s1250_nfs
from emensageriapro.s1250.forms import form_s1250_nfs
from emensageriapro.s1250.forms import form_s1250_infoprocjud
from emensageriapro.s1250.forms import form_s1250_infoprocjud
from emensageriapro.s1260.forms import form_s1260_tpcomerc
from emensageriapro.s1260.forms import form_s1260_tpcomerc
from emensageriapro.s1260.forms import form_s1260_ideadquir
from emensageriapro.s1260.forms import form_s1260_ideadquir
from emensageriapro.s1260.forms import form_s1260_nfs
from emensageriapro.s1260.forms import form_s1260_nfs
from emensageriapro.s2200.forms import form_s2200_infoceletista
from emensageriapro.s2200.forms import form_s2200_infoceletista
from emensageriapro.s1260.forms import form_s1260_infoprocjud
from emensageriapro.s1260.forms import form_s1260_infoprocjud
from emensageriapro.s1270.forms import form_s1270_remunavnp
from emensageriapro.s1270.forms import form_s1270_remunavnp
from emensageriapro.s1280.forms import form_s1280_infosubstpatr
from emensageriapro.s1280.forms import form_s1280_infosubstpatr
from emensageriapro.s1280.forms import form_s1280_infosubstpatropport
from emensageriapro.s1280.forms import form_s1280_infosubstpatropport
from emensageriapro.s1280.forms import form_s1280_infoativconcom
from emensageriapro.s1280.forms import form_s1280_infoativconcom
from emensageriapro.s1295.forms import form_s1295_iderespinf
from emensageriapro.s1295.forms import form_s1295_iderespinf
from emensageriapro.s1299.forms import form_s1299_iderespinf
from emensageriapro.s1299.forms import form_s1299_iderespinf
from emensageriapro.s1300.forms import form_s1300_contribsind
from emensageriapro.s1300.forms import form_s1300_contribsind
from emensageriapro.s2200.forms import form_s2200_documentos
from emensageriapro.s2200.forms import form_s2200_documentos
from emensageriapro.s2200.forms import form_s2200_ctps
from emensageriapro.s2200.forms import form_s2200_ctps
from emensageriapro.s2200.forms import form_s2200_ric
from emensageriapro.s2200.forms import form_s2200_ric
from emensageriapro.s2200.forms import form_s2200_rg
from emensageriapro.s2200.forms import form_s2200_rg
from emensageriapro.s2200.forms import form_s2200_rne
from emensageriapro.s2200.forms import form_s2200_rne
from emensageriapro.s2200.forms import form_s2200_oc
from emensageriapro.s2200.forms import form_s2200_oc
from emensageriapro.s2200.forms import form_s2200_cnh
from emensageriapro.s2200.forms import form_s2200_cnh
from emensageriapro.s2200.forms import form_s2200_brasil
from emensageriapro.s2200.forms import form_s2200_brasil
from emensageriapro.s2200.forms import form_s2200_exterior
from emensageriapro.s2200.forms import form_s2200_exterior
from emensageriapro.s2200.forms import form_s2200_trabestrangeiro
from emensageriapro.s2200.forms import form_s2200_trabestrangeiro
from emensageriapro.s2200.forms import form_s2200_infodeficiencia
from emensageriapro.s2200.forms import form_s2200_infodeficiencia
from emensageriapro.s2200.forms import form_s2200_dependente
from emensageriapro.s2200.forms import form_s2200_dependente
from emensageriapro.s2200.forms import form_s2200_aposentadoria
from emensageriapro.s2200.forms import form_s2200_aposentadoria
from emensageriapro.s2200.forms import form_s2200_contato
from emensageriapro.s2200.forms import form_s2200_contato
from emensageriapro.s2200.forms import form_s2200_trabtemporario
from emensageriapro.s2200.forms import form_s2200_trabtemporario
from emensageriapro.s2200.forms import form_s2200_ideestabvinc
from emensageriapro.s2200.forms import form_s2200_ideestabvinc
from emensageriapro.s2200.forms import form_s2200_idetrabsubstituido
from emensageriapro.s2200.forms import form_s2200_idetrabsubstituido
from emensageriapro.s2200.forms import form_s2200_aprend
from emensageriapro.s2200.forms import form_s2200_aprend
from emensageriapro.s2200.forms import form_s2200_infoestatutario
from emensageriapro.s2200.forms import form_s2200_infoestatutario
from emensageriapro.s2200.forms import form_s2200_infodecjud
from emensageriapro.s2200.forms import form_s2200_infodecjud
from emensageriapro.s2200.forms import form_s2200_localtrabgeral
from emensageriapro.s2200.forms import form_s2200_localtrabgeral
from emensageriapro.s2200.forms import form_s2200_localtrabdom
from emensageriapro.s2200.forms import form_s2200_localtrabdom
from emensageriapro.s2200.forms import form_s2200_horcontratual
from emensageriapro.s2200.forms import form_s2200_horcontratual
from emensageriapro.s2200.forms import form_s2200_horario
from emensageriapro.s2200.forms import form_s2200_horario
from emensageriapro.s2200.forms import form_s2200_filiacaosindical
from emensageriapro.s2200.forms import form_s2200_filiacaosindical
from emensageriapro.s2200.forms import form_s2200_alvarajudicial
from emensageriapro.s2200.forms import form_s2200_alvarajudicial
from emensageriapro.s2200.forms import form_s2200_observacoes
from emensageriapro.s2200.forms import form_s2200_observacoes
from emensageriapro.s2200.forms import form_s2200_sucessaovinc
from emensageriapro.s2200.forms import form_s2200_sucessaovinc
from emensageriapro.s2200.forms import form_s2200_transfdom
from emensageriapro.s2200.forms import form_s2200_transfdom
from emensageriapro.s2200.forms import form_s2200_afastamento
from emensageriapro.s2200.forms import form_s2200_afastamento
from emensageriapro.s2200.forms import form_s2200_desligamento
from emensageriapro.s2200.forms import form_s2200_desligamento
from emensageriapro.s2200.forms import form_s2200_cessao
from emensageriapro.s2200.forms import form_s2200_cessao
from emensageriapro.s2205.forms import form_s2205_documentos
from emensageriapro.s2205.forms import form_s2205_documentos
from emensageriapro.s2205.forms import form_s2205_ctps
from emensageriapro.s2205.forms import form_s2205_ctps
from emensageriapro.s2205.forms import form_s2205_ric
from emensageriapro.s2205.forms import form_s2205_ric
from emensageriapro.s2205.forms import form_s2205_rg
from emensageriapro.s2205.forms import form_s2205_rg
from emensageriapro.s2205.forms import form_s2205_rne
from emensageriapro.s2205.forms import form_s2205_rne
from emensageriapro.s2205.forms import form_s2205_oc
from emensageriapro.s2205.forms import form_s2205_oc
from emensageriapro.s2205.forms import form_s2205_cnh
from emensageriapro.s2205.forms import form_s2205_cnh
from emensageriapro.s2205.forms import form_s2205_brasil
from emensageriapro.s2205.forms import form_s2205_brasil
from emensageriapro.s2205.forms import form_s2205_exterior
from emensageriapro.s2205.forms import form_s2205_exterior
from emensageriapro.s2205.forms import form_s2205_trabestrangeiro
from emensageriapro.s2205.forms import form_s2205_trabestrangeiro
from emensageriapro.s2205.forms import form_s2205_infodeficiencia
from emensageriapro.s2205.forms import form_s2205_infodeficiencia
from emensageriapro.s2205.forms import form_s2205_dependente
from emensageriapro.s2205.forms import form_s2205_dependente
from emensageriapro.s2205.forms import form_s2205_aposentadoria
from emensageriapro.s2205.forms import form_s2205_aposentadoria
from emensageriapro.s2205.forms import form_s2205_contato
from emensageriapro.s2205.forms import form_s2205_contato
from emensageriapro.s2206.forms import form_s2206_infoceletista
from emensageriapro.s2206.forms import form_s2206_infoceletista
from emensageriapro.s2206.forms import form_s2206_trabtemp
from emensageriapro.s2206.forms import form_s2206_trabtemp
from emensageriapro.s2206.forms import form_s2206_aprend
from emensageriapro.s2206.forms import form_s2206_aprend
from emensageriapro.s2206.forms import form_s2206_infoestatutario
from emensageriapro.s2206.forms import form_s2206_infoestatutario
from emensageriapro.s2206.forms import form_s2206_localtrabgeral
from emensageriapro.s2206.forms import form_s2206_localtrabgeral
from emensageriapro.s2206.forms import form_s2206_localtrabdom
from emensageriapro.s2206.forms import form_s2206_localtrabdom
from emensageriapro.s2206.forms import form_s2206_horcontratual
from emensageriapro.s2206.forms import form_s2206_horcontratual
from emensageriapro.s2206.forms import form_s2206_horario
from emensageriapro.s2206.forms import form_s2206_horario
from emensageriapro.s2206.forms import form_s2206_filiacaosindical
from emensageriapro.s2206.forms import form_s2206_filiacaosindical
from emensageriapro.s2240.forms import form_s2240_iniexprisco_epc
from emensageriapro.s2240.forms import form_s2240_iniexprisco_epc
from emensageriapro.s2206.forms import form_s2206_alvarajudicial
from emensageriapro.s2206.forms import form_s2206_alvarajudicial
from emensageriapro.s2206.forms import form_s2206_observacoes
from emensageriapro.s2206.forms import form_s2206_observacoes
from emensageriapro.s2206.forms import form_s2206_servpubl
from emensageriapro.s2206.forms import form_s2206_servpubl
from emensageriapro.s2210.forms import form_s2210_idelocalacid
from emensageriapro.s2210.forms import form_s2210_idelocalacid
from emensageriapro.s2210.forms import form_s2210_parteatingida
from emensageriapro.s2210.forms import form_s2210_parteatingida
from emensageriapro.s2210.forms import form_s2210_agentecausador
from emensageriapro.s2210.forms import form_s2210_agentecausador
from emensageriapro.s2210.forms import form_s2210_atestado
from emensageriapro.s2210.forms import form_s2210_atestado
from emensageriapro.s2210.forms import form_s2210_catorigem
from emensageriapro.s2210.forms import form_s2210_catorigem
from emensageriapro.s2220.forms import form_s2220_exmedocup
from emensageriapro.s2220.forms import form_s2220_exmedocup
from emensageriapro.s2220.forms import form_s2220_exame
from emensageriapro.s2220.forms import form_s2220_exame
from emensageriapro.s2220.forms import form_s2220_toxicologico
from emensageriapro.s2220.forms import form_s2220_toxicologico
from emensageriapro.s2230.forms import form_s2230_iniafastamento
from emensageriapro.s2230.forms import form_s2230_iniafastamento
from emensageriapro.s2230.forms import form_s2230_infoatestado
from emensageriapro.s2230.forms import form_s2230_infoatestado
from emensageriapro.s2230.forms import form_s2230_emitente
from emensageriapro.s2230.forms import form_s2230_emitente
from emensageriapro.s2230.forms import form_s2230_infocessao
from emensageriapro.s2230.forms import form_s2230_infocessao
from emensageriapro.s2230.forms import form_s2230_infomandsind
from emensageriapro.s2230.forms import form_s2230_infomandsind
from emensageriapro.s2230.forms import form_s2230_inforetif
from emensageriapro.s2230.forms import form_s2230_inforetif
from emensageriapro.s2230.forms import form_s2230_fimafastamento
from emensageriapro.s2230.forms import form_s2230_fimafastamento
from emensageriapro.s2231.forms import form_s2231_inicessao
from emensageriapro.s2231.forms import form_s2231_inicessao
from emensageriapro.s2231.forms import form_s2231_fimcessao
from emensageriapro.s2231.forms import form_s2231_fimcessao
from emensageriapro.s2240.forms import form_s2240_iniexprisco
from emensageriapro.s2240.forms import form_s2240_iniexprisco
from emensageriapro.s2240.forms import form_s2240_iniexprisco_infoamb
from emensageriapro.s2240.forms import form_s2240_iniexprisco_infoamb
from emensageriapro.s2240.forms import form_s2240_iniexprisco_ativpericinsal
from emensageriapro.s2240.forms import form_s2240_iniexprisco_ativpericinsal
from emensageriapro.s2240.forms import form_s2240_iniexprisco_fatrisco
from emensageriapro.s2240.forms import form_s2240_iniexprisco_fatrisco
from emensageriapro.s2240.forms import form_s2240_iniexprisco_epi
from emensageriapro.s2240.forms import form_s2240_iniexprisco_epi
from emensageriapro.s2240.forms import form_s2240_iniexprisco_respreg
from emensageriapro.s2240.forms import form_s2240_iniexprisco_respreg
from emensageriapro.s2240.forms import form_s2240_iniexprisco_obs
from emensageriapro.s2240.forms import form_s2240_iniexprisco_obs
from emensageriapro.s2240.forms import form_s2240_altexprisco
from emensageriapro.s2240.forms import form_s2240_altexprisco
from emensageriapro.s2240.forms import form_s2240_altexprisco_infoamb
from emensageriapro.s2240.forms import form_s2240_altexprisco_infoamb
from emensageriapro.s2240.forms import form_s2240_altexprisco_fatrisco
from emensageriapro.s2240.forms import form_s2240_altexprisco_fatrisco
from emensageriapro.s2240.forms import form_s2240_altexprisco_epc
from emensageriapro.s2240.forms import form_s2240_altexprisco_epc
from emensageriapro.s2240.forms import form_s2240_altexprisco_epi
from emensageriapro.s2240.forms import form_s2240_altexprisco_epi
from emensageriapro.s2240.forms import form_s2240_fimexprisco
from emensageriapro.s2240.forms import form_s2240_fimexprisco
from emensageriapro.s2240.forms import form_s2240_fimexprisco_infoamb
from emensageriapro.s2240.forms import form_s2240_fimexprisco_infoamb
from emensageriapro.s2240.forms import form_s2240_fimexprisco_respreg
from emensageriapro.s2240.forms import form_s2240_fimexprisco_respreg
from emensageriapro.s2241.forms import form_s2241_insalperic
from emensageriapro.s2241.forms import form_s2241_insalperic
from emensageriapro.s2241.forms import form_s2241_iniinsalperic
from emensageriapro.s2241.forms import form_s2241_iniinsalperic
from emensageriapro.s2241.forms import form_s2241_iniinsalperic_infoamb
from emensageriapro.s2241.forms import form_s2241_iniinsalperic_infoamb
from emensageriapro.s2241.forms import form_s2241_iniinsalperic_fatrisco
from emensageriapro.s2241.forms import form_s2241_iniinsalperic_fatrisco
from emensageriapro.s2241.forms import form_s2241_altinsalperic
from emensageriapro.s2241.forms import form_s2241_altinsalperic
from emensageriapro.s2241.forms import form_s2241_altinsalperic_infoamb
from emensageriapro.s2241.forms import form_s2241_altinsalperic_infoamb
from emensageriapro.s2241.forms import form_s2241_altinsalperic_fatrisco
from emensageriapro.s2241.forms import form_s2241_altinsalperic_fatrisco
from emensageriapro.s2241.forms import form_s2241_fiminsalperic
from emensageriapro.s2241.forms import form_s2241_fiminsalperic
from emensageriapro.s2241.forms import form_s2241_fiminsalperic_infoamb
from emensageriapro.s2241.forms import form_s2241_fiminsalperic_infoamb
from emensageriapro.s2241.forms import form_s2241_aposentesp
from emensageriapro.s2241.forms import form_s2241_aposentesp
from emensageriapro.s2241.forms import form_s2241_iniaposentesp
from emensageriapro.s2241.forms import form_s2241_iniaposentesp
from emensageriapro.s2241.forms import form_s2241_iniaposentesp_infoamb
from emensageriapro.s2241.forms import form_s2241_iniaposentesp_infoamb
from emensageriapro.s2241.forms import form_s2241_iniaposentesp_fatrisco
from emensageriapro.s2241.forms import form_s2241_iniaposentesp_fatrisco
from emensageriapro.s2241.forms import form_s2241_altaposentesp
from emensageriapro.s2241.forms import form_s2241_altaposentesp
from emensageriapro.s2241.forms import form_s2241_altaposentesp_infoamb
from emensageriapro.s2241.forms import form_s2241_altaposentesp_infoamb
from emensageriapro.s2241.forms import form_s2241_altaposentesp_fatrisco
from emensageriapro.s2241.forms import form_s2241_altaposentesp_fatrisco
from emensageriapro.s2241.forms import form_s2241_fimaposentesp
from emensageriapro.s2241.forms import form_s2241_fimaposentesp
from emensageriapro.s2241.forms import form_s2241_fimaposentesp_infoamb
from emensageriapro.s2241.forms import form_s2241_fimaposentesp_infoamb
from emensageriapro.s2245.forms import form_s2245_ideprofresp
from emensageriapro.s2245.forms import form_s2245_ideprofresp
from emensageriapro.s2250.forms import form_s2250_detavprevio
from emensageriapro.s2250.forms import form_s2250_detavprevio
from emensageriapro.s2250.forms import form_s2250_cancavprevio
from emensageriapro.s2250.forms import form_s2250_cancavprevio
from emensageriapro.s2260.forms import form_s2260_localtrabinterm
from emensageriapro.s2260.forms import form_s2260_localtrabinterm
from emensageriapro.s2299.forms import form_s2299_observacoes
from emensageriapro.s2299.forms import form_s2299_observacoes
from emensageriapro.s2299.forms import form_s2299_sucessaovinc
from emensageriapro.s2299.forms import form_s2299_sucessaovinc
from emensageriapro.s2299.forms import form_s2299_transftit
from emensageriapro.s2299.forms import form_s2299_transftit
from emensageriapro.s2299.forms import form_s2299_verbasresc
from emensageriapro.s2299.forms import form_s2299_verbasresc
from emensageriapro.s2299.forms import form_s2299_dmdev
from emensageriapro.s2299.forms import form_s2299_dmdev
from emensageriapro.s2299.forms import form_s2299_infoperapur
from emensageriapro.s2299.forms import form_s2299_infoperapur
from emensageriapro.s2299.forms import form_s2299_infoperapur_ideestablot
from emensageriapro.s2299.forms import form_s2299_infoperapur_ideestablot
from emensageriapro.s2299.forms import form_s2299_infoperapur_detverbas
from emensageriapro.s2299.forms import form_s2299_infoperapur_detverbas
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosaudecolet
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosaudecolet
from emensageriapro.s2299.forms import form_s2299_infoperapur_detoper
from emensageriapro.s2299.forms import form_s2299_infoperapur_detoper
from emensageriapro.s2299.forms import form_s2299_infoperapur_detplano
from emensageriapro.s2299.forms import form_s2299_infoperapur_detplano
from emensageriapro.s2300.forms import form_s2300_infodirigentesindical
from emensageriapro.s2300.forms import form_s2300_infodirigentesindical
from emensageriapro.s2299.forms import form_s2299_infoperapur_infoagnocivo
from emensageriapro.s2299.forms import form_s2299_infoperapur_infoagnocivo
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosimples
from emensageriapro.s2299.forms import form_s2299_infoperapur_infosimples
from emensageriapro.s2299.forms import form_s2299_infoperant
from emensageriapro.s2299.forms import form_s2299_infoperant
from emensageriapro.s2299.forms import form_s2299_infoperant_ideadc
from emensageriapro.s2299.forms import form_s2299_infoperant_ideadc
from emensageriapro.s2299.forms import form_s2299_infoperant_ideperiodo
from emensageriapro.s2299.forms import form_s2299_infoperant_ideperiodo
from emensageriapro.s2299.forms import form_s2299_infoperant_ideestablot
from emensageriapro.s2299.forms import form_s2299_infoperant_ideestablot
from emensageriapro.s2299.forms import form_s2299_infoperant_detverbas
from emensageriapro.s2299.forms import form_s2299_infoperant_detverbas
from emensageriapro.s2299.forms import form_s2299_infoperant_infoagnocivo
from emensageriapro.s2299.forms import form_s2299_infoperant_infoagnocivo
from emensageriapro.s2299.forms import form_s2299_infoperant_infosimples
from emensageriapro.s2299.forms import form_s2299_infoperant_infosimples
from emensageriapro.s2299.forms import form_s2299_infotrabinterm
from emensageriapro.s2299.forms import form_s2299_infotrabinterm
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_procjudtrab
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_procjudtrab
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_infomv
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_infomv
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_remunoutrempr
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_remunoutrempr
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_proccs
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_proccs
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_quarentena
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_quarentena
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_consigfgts
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_consigfgts
from emensageriapro.s2300.forms import form_s2300_documentos
from emensageriapro.s2300.forms import form_s2300_documentos
from emensageriapro.s2300.forms import form_s2300_ctps
from emensageriapro.s2300.forms import form_s2300_ctps
from emensageriapro.s2300.forms import form_s2300_ric
from emensageriapro.s2300.forms import form_s2300_ric
from emensageriapro.s2300.forms import form_s2300_rg
from emensageriapro.s2300.forms import form_s2300_rg
from emensageriapro.s2300.forms import form_s2300_rne
from emensageriapro.s2300.forms import form_s2300_rne
from emensageriapro.s2300.forms import form_s2300_oc
from emensageriapro.s2300.forms import form_s2300_oc
from emensageriapro.s2300.forms import form_s2300_cnh
from emensageriapro.s2300.forms import form_s2300_cnh
from emensageriapro.s2300.forms import form_s2300_brasil
from emensageriapro.s2300.forms import form_s2300_brasil
from emensageriapro.s2300.forms import form_s2300_exterior
from emensageriapro.s2300.forms import form_s2300_exterior
from emensageriapro.s2300.forms import form_s2300_trabestrangeiro
from emensageriapro.s2300.forms import form_s2300_trabestrangeiro
from emensageriapro.s2300.forms import form_s2300_infodeficiencia
from emensageriapro.s2300.forms import form_s2300_infodeficiencia
from emensageriapro.s2300.forms import form_s2300_dependente
from emensageriapro.s2300.forms import form_s2300_dependente
from emensageriapro.s2300.forms import form_s2300_contato
from emensageriapro.s2300.forms import form_s2300_contato
from emensageriapro.s2300.forms import form_s2300_infocomplementares
from emensageriapro.s2300.forms import form_s2300_infocomplementares
from emensageriapro.s2300.forms import form_s2300_cargofuncao
from emensageriapro.s2300.forms import form_s2300_cargofuncao
from emensageriapro.s2300.forms import form_s2300_remuneracao
from emensageriapro.s2300.forms import form_s2300_remuneracao
from emensageriapro.s2300.forms import form_s2300_fgts
from emensageriapro.s2300.forms import form_s2300_fgts
from emensageriapro.s2300.forms import form_s2300_infotrabcedido
from emensageriapro.s2300.forms import form_s2300_infotrabcedido
from emensageriapro.s2300.forms import form_s2300_infoestagiario
from emensageriapro.s2300.forms import form_s2300_infoestagiario
from emensageriapro.s2300.forms import form_s2300_ageintegracao
from emensageriapro.s2300.forms import form_s2300_ageintegracao
from emensageriapro.s2300.forms import form_s2300_supervisorestagio
from emensageriapro.s2300.forms import form_s2300_supervisorestagio
from emensageriapro.s2300.forms import form_s2300_afastamento
from emensageriapro.s2300.forms import form_s2300_afastamento
from emensageriapro.s2300.forms import form_s2300_termino
from emensageriapro.s2300.forms import form_s2300_termino
from emensageriapro.s2306.forms import form_s2306_infocomplementares
from emensageriapro.s2306.forms import form_s2306_infocomplementares
from emensageriapro.s2306.forms import form_s2306_cargofuncao
from emensageriapro.s2306.forms import form_s2306_cargofuncao
from emensageriapro.s2306.forms import form_s2306_remuneracao
from emensageriapro.s2306.forms import form_s2306_remuneracao
from emensageriapro.s2306.forms import form_s2306_infotrabcedido
from emensageriapro.s2306.forms import form_s2306_infotrabcedido
from emensageriapro.s2306.forms import form_s2306_infoestagiario
from emensageriapro.s2306.forms import form_s2306_infoestagiario
from emensageriapro.s2306.forms import form_s2306_ageintegracao
from emensageriapro.s2306.forms import form_s2306_ageintegracao
from emensageriapro.s2306.forms import form_s2306_supervisorestagio
from emensageriapro.s2306.forms import form_s2306_supervisorestagio
from emensageriapro.s2399.forms import form_s2399_verbasresc
from emensageriapro.s2399.forms import form_s2399_verbasresc
from emensageriapro.s2399.forms import form_s2399_dmdev
from emensageriapro.s2399.forms import form_s2399_dmdev
from emensageriapro.s2399.forms import form_s2399_ideestablot
from emensageriapro.s2399.forms import form_s2399_ideestablot
from emensageriapro.s2399.forms import form_s2399_detverbas
from emensageriapro.s2399.forms import form_s2399_detverbas
from emensageriapro.s2399.forms import form_s2399_infosaudecolet
from emensageriapro.s2399.forms import form_s2399_infosaudecolet
from emensageriapro.s2399.forms import form_s2399_detoper
from emensageriapro.s2399.forms import form_s2399_detoper
from emensageriapro.s2399.forms import form_s2399_detplano
from emensageriapro.s2399.forms import form_s2399_detplano
from emensageriapro.s2399.forms import form_s2399_infoagnocivo
from emensageriapro.s2399.forms import form_s2399_infoagnocivo
from emensageriapro.s2399.forms import form_s2399_infosimples
from emensageriapro.s2399.forms import form_s2399_infosimples
from emensageriapro.s2399.forms import form_s2399_procjudtrab
from emensageriapro.s2399.forms import form_s2399_procjudtrab
from emensageriapro.s2399.forms import form_s2399_infomv
from emensageriapro.s2399.forms import form_s2399_infomv
from emensageriapro.s2399.forms import form_s2399_remunoutrempr
from emensageriapro.s2399.forms import form_s2399_remunoutrempr
from emensageriapro.s2399.forms import form_s2399_quarentena
from emensageriapro.s2399.forms import form_s2399_quarentena
from emensageriapro.s2400.forms import form_s2400_endereco
from emensageriapro.s2400.forms import form_s2400_endereco
from emensageriapro.s2400.forms import form_s2400_brasil
from emensageriapro.s2400.forms import form_s2400_brasil
from emensageriapro.s2400.forms import form_s2400_exterior
from emensageriapro.s2400.forms import form_s2400_exterior
from emensageriapro.s2400.forms import form_s2400_dependente
from emensageriapro.s2400.forms import form_s2400_dependente
from emensageriapro.s2405.forms import form_s2405_endereco
from emensageriapro.s2405.forms import form_s2405_endereco
from emensageriapro.s2405.forms import form_s2405_brasil
from emensageriapro.s2405.forms import form_s2405_brasil
from emensageriapro.s2405.forms import form_s2405_exterior
from emensageriapro.s2405.forms import form_s2405_exterior
from emensageriapro.s2405.forms import form_s2405_dependente
from emensageriapro.s2405.forms import form_s2405_dependente
from emensageriapro.s2410.forms import form_s2410_infopenmorte
from emensageriapro.s2410.forms import form_s2410_infopenmorte
from emensageriapro.s2410.forms import form_s2410_instpenmorte
from emensageriapro.s2410.forms import form_s2410_instpenmorte
from emensageriapro.s2410.forms import form_s2410_homologtc
from emensageriapro.s2410.forms import form_s2410_homologtc
from emensageriapro.s2416.forms import form_s2416_infopenmorte
from emensageriapro.s2416.forms import form_s2416_infopenmorte
from emensageriapro.s2416.forms import form_s2416_homologtc
from emensageriapro.s2416.forms import form_s2416_homologtc
from emensageriapro.s2416.forms import form_s2416_suspensao
from emensageriapro.s2416.forms import form_s2416_suspensao
from emensageriapro.s3000.forms import form_s3000_idetrabalhador
from emensageriapro.s3000.forms import form_s3000_idetrabalhador
from emensageriapro.s3000.forms import form_s3000_idefolhapagto
from emensageriapro.s3000.forms import form_s3000_idefolhapagto
from emensageriapro.s5001.forms import form_s5001_procjudtrab
from emensageriapro.s5001.forms import form_s5001_procjudtrab
from emensageriapro.s5001.forms import form_s5001_infocpcalc
from emensageriapro.s5001.forms import form_s5001_infocpcalc
from emensageriapro.s5001.forms import form_s5001_infocp
from emensageriapro.s5001.forms import form_s5001_infocp
from emensageriapro.s5001.forms import form_s5001_ideestablot
from emensageriapro.s5001.forms import form_s5001_ideestablot
from emensageriapro.s5001.forms import form_s5001_infocategincid
from emensageriapro.s5001.forms import form_s5001_infocategincid
from emensageriapro.s5001.forms import form_s5001_infobasecs
from emensageriapro.s5001.forms import form_s5001_infobasecs
from emensageriapro.s5001.forms import form_s5001_calcterc
from emensageriapro.s5001.forms import form_s5001_calcterc
from emensageriapro.s5002.forms import form_s5002_infodep
from emensageriapro.s5002.forms import form_s5002_infodep
from emensageriapro.s5002.forms import form_s5002_infoirrf
from emensageriapro.s5002.forms import form_s5002_infoirrf
from emensageriapro.s5002.forms import form_s5002_basesirrf
from emensageriapro.s5002.forms import form_s5002_basesirrf
from emensageriapro.s5002.forms import form_s5002_irrf
from emensageriapro.s5002.forms import form_s5002_irrf
from emensageriapro.s5002.forms import form_s5002_idepgtoext
from emensageriapro.s5002.forms import form_s5002_idepgtoext
from emensageriapro.s5011.forms import form_s5011_infocpseg
from emensageriapro.s5011.forms import form_s5011_infocpseg
from emensageriapro.s5011.forms import form_s5011_infopj
from emensageriapro.s5011.forms import form_s5011_infopj
from emensageriapro.s5011.forms import form_s5011_infoatconc
from emensageriapro.s5011.forms import form_s5011_infoatconc
from emensageriapro.s5011.forms import form_s5011_ideestab
from emensageriapro.s5011.forms import form_s5011_ideestab
from emensageriapro.s5011.forms import form_s5011_infoestab
from emensageriapro.s5011.forms import form_s5011_infoestab
from emensageriapro.s5011.forms import form_s5011_infocomplobra
from emensageriapro.s5011.forms import form_s5011_infocomplobra
from emensageriapro.s5011.forms import form_s5011_idelotacao
from emensageriapro.s5011.forms import form_s5011_idelotacao
from emensageriapro.s5011.forms import form_s5011_infotercsusp
from emensageriapro.s5011.forms import form_s5011_infotercsusp
from emensageriapro.s5011.forms import form_s5011_infoemprparcial
from emensageriapro.s5011.forms import form_s5011_infoemprparcial
from emensageriapro.s5011.forms import form_s5011_dadosopport
from emensageriapro.s5011.forms import form_s5011_dadosopport
from emensageriapro.s5011.forms import form_s5011_basesremun
from emensageriapro.s5011.forms import form_s5011_basesremun
from emensageriapro.s5011.forms import form_s5011_basesavnport
from emensageriapro.s5011.forms import form_s5011_basesavnport
from emensageriapro.s5011.forms import form_s5011_infosubstpatropport
from emensageriapro.s5011.forms import form_s5011_infosubstpatropport
from emensageriapro.s5011.forms import form_s5011_basesaquis
from emensageriapro.s5011.forms import form_s5011_basesaquis
from emensageriapro.s5011.forms import form_s5011_basescomerc
from emensageriapro.s5011.forms import form_s5011_basescomerc
from emensageriapro.s5011.forms import form_s5011_infocrestab
from emensageriapro.s5011.forms import form_s5011_infocrestab
from emensageriapro.s5011.forms import form_s5011_infocrcontrib
from emensageriapro.s5011.forms import form_s5011_infocrcontrib
from emensageriapro.s5012.forms import form_s5012_infocrcontrib
from emensageriapro.s5012.forms import form_s5012_infocrcontrib

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        usuarios_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if usuarios_id:
        usuarios = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuarios_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if usuarios_id:
            usuarios_form = form_usuarios(request.POST or None, instance = usuarios, slug = db_slug)
        else:
            usuarios_form = form_usuarios(request.POST or None, slug = db_slug, initial={'password': 'asdkl1231'})
        if request.method == 'POST':
            if usuarios_form.is_valid():
                dados = usuarios_form.cleaned_data
                if usuarios_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #usuarios_campos_multiple_passo1
                    Usuarios.objects.using(db_slug).filter(id=usuarios_id).update(**dados)
                    obj = Usuarios.objects.using(db_slug).get(id=usuarios_id)
                    #usuarios_editar_custom
                    #usuarios_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:
                    dados['password'] = 'asdkl1231'

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #usuarios_cadastrar_campos_multiple_passo1
                    obj = Usuarios(**dados)
                    obj.save(using = db_slug)
                    #usuarios_cadastrar_custom
                    #usuarios_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('usuarios_apagar', 'usuarios_salvar', 'usuarios'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if usuarios_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('usuarios_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        usuarios_form = disabled_form_fields(usuarios_form, permissao.permite_editar)
        #usuarios_campos_multiple_passo3

        for field in usuarios_form.fields.keys():
            usuarios_form.fields[field].widget.attrs['ng-model'] = 'usuarios_'+field
        if int(dict_hash['print']):
            usuarios_form = disabled_form_for_print(usuarios_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if usuarios_id:
            usuarios = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuarios_id)
            pass
        else:
            usuarios = None
        #usuarios_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'usuarios' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'usuarios_salvar'
        context = {
            'usuarios': usuarios,
            'usuarios_form': usuarios_form,
            'mensagem': mensagem,
            'usuarios_id': int(usuarios_id),
            'usuario': usuario,
       
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #usuarios_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'usuarios_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='usuarios_salvar.html',
                filename="usuarios.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('usuarios_salvar.html', context)
            filename = "usuarios.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
        context = {
            'usuario': usuario,
       
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class UsuariosList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = Usuarios.objects.using(db_slug).all()
    serializer_class = UsuariosSerializer
    permission_classes = (IsAdminUser,)


class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = Usuarios.objects.using(db_slug).all()
    serializer_class = UsuariosSerializer
    permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #usuarios_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_config_perfis': 1,
            'show_date_joined': 0,
            'show_last_login': 0,
            'show_is_active': 0,
            'show_is_staff': 0,
            'show_is_superuser': 0,
            'show_email': 1,
            'show_last_name': 1,
            'show_first_name': 1,
            'show_password': 0,
            'show_username': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'config_perfis': 'config_perfis',
                'email__icontains': 'email__icontains',
                'last_name__icontains': 'last_name__icontains',
                'first_name__icontains': 'first_name__icontains',
                'username__icontains': 'username__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'config_perfis': 'config_perfis',
                'email__icontains': 'email__icontains',
                'last_name__icontains': 'last_name__icontains',
                'first_name__icontains': 'first_name__icontains',
                'username__icontains': 'username__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        usuarios_lista = Usuarios.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(usuarios_lista) > 100:
            filtrar = True
            usuarios_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        config_perfis_lista = ConfigPerfis.objects.using( db_slug ).filter(excluido = False).all()
        #usuarios_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'usuarios'
        context = {
            'usuarios_lista': usuarios_lista,
       
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
  
            'config_perfis_lista': config_perfis_lista,
        }
        if for_print in (0,1):
            return render(request, 'usuarios_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='usuarios_listar.html',
                filename="usuarios.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('usuarios_listar.html', context)
            filename = "usuarios.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/usuarios_csv.html', context)
            filename = "usuarios.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,
       
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        usuarios_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='usuarios')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    usuarios = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuarios_id)
    if request.method == 'POST':
        Usuarios.objects.using( db_slug ).filter(id = usuarios_id).update(excluido = True)
        #usuarios_apagar_custom
        #usuarios_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'usuarios_salvar':
            return redirect('usuarios', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
   
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
   
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'usuarios_apagar.html', context)

