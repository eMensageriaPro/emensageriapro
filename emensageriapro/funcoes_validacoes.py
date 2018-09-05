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

from lxml import etree

VERSAO_ATUAL = ('v02_04_02','v1_03_02')

def validar_schema(file_schema_xsd, file_xml, lang=None):
    from emensageriapro.settings import BASE_DIR
    from googletrans import Translator
    file_schema_xsd = BASE_DIR+'/xsd/' + file_schema_xsd
    #print file_schema_xsd
    file_xml = BASE_DIR+'/'+file_xml

    schema = etree.parse(file_schema_xsd)
    xmlschema = etree.XMLSchema(schema)

    quant_erros = 0

    try:
        document = etree.parse(file_xml)
        #print "Parse complete!"
    except etree.XMLSyntaxError, e:
        quant_erros += 1
        error_list = []
        if lang:
            translator = Translator()
            erro = translator.translate(e, src='en', dest=lang)
            errors = erro.text
            return quant_erros, error_list.append(errors)
        else:
            return quant_erros, error_list.append(e)

    xmlschema.validate(document)

    error_list = []
    
    if xmlschema.error_log:

        for error in xmlschema.error_log:
            error_list.append("LINE %s: %s" % (error.line, error.message.encode("utf-8")))
            quant_erros += 1

        if error_list and lang:
            try:
                translator = Translator()
                erro_translate = translator.translate('|'.join(error_list), src='en', dest=lang)
                errors = erro_translate.text
                error_list = errors.split('|')
            except:
                pass

        return quant_erros, error_list

    else:

        return 0, []


def get_schema_name(arquivo):
    from emensageriapro.funcoes_importacao import get_versao_evento
    from emensageriapro.padrao import ler_arquivo
    xml = ler_arquivo(arquivo).replace("s:", "")
    if 'eSocial' in xml:
        tipo = 'esocial'
    elif 'Reinf' in xml:
        tipo = 'efdreinf'
    versao = get_versao_evento(xml)
    schema_filename = ''

    if tipo == 'esocial':

        if 'evtInfoEmpregador' in xml:
            schema_filename = '%s/%s/evtInfoEmpregador.xsd' % (tipo, versao)

        elif 'evtTabEstab' in xml:
            schema_filename = '%s/%s/evtTabEstab.xsd' % (tipo, versao)

        elif 'evtTabRubrica' in xml:
            schema_filename = '%s/%s/evtTabRubrica.xsd' % (tipo, versao)

        elif 'evtTabLotacao' in xml:
            schema_filename = '%s/%s/evtTabLotacao.xsd' % (tipo, versao)

        elif 'evtTabCargo' in xml:
            schema_filename = '%s/%s/evtTabCargo.xsd' % (tipo, versao)

        elif 'evtTabCarreira' in xml:
            schema_filename = '%s/%s/evtTabCarreira.xsd' % (tipo, versao)

        elif 'evtTabFuncao' in xml:
            schema_filename = '%s/%s/evtTabFuncao.xsd' % (tipo, versao)

        elif 'evtTabHorTur' in xml:
            schema_filename = '%s/%s/evtTabHorTur.xsd' % (tipo, versao)

        elif 'evtTabAmbiente' in xml:
            schema_filename = '%s/%s/evtTabAmbiente.xsd' % (tipo, versao)

        elif 'evtTabProcesso' in xml:
            schema_filename = '%s/%s/evtTabProcesso.xsd' % (tipo, versao)

        elif 'evtTabOperPort' in xml:
            schema_filename = '%s/%s/evtTabOperPort.xsd' % (tipo, versao)

        elif 'evtRemun' in xml:
            schema_filename = '%s/%s/evtRemun.xsd' % (tipo, versao)

        elif 'evtRmnRPPS' in xml:
            schema_filename = '%s/%s/evtRmnRPPS.xsd' % (tipo, versao)

        elif 'evtBenPrRP' in xml:
            schema_filename = '%s/%s/evtBenPrRP.xsd' % (tipo, versao)

        elif 'evtPgtos' in xml:
            schema_filename = '%s/%s/evtPgtos.xsd' % (tipo, versao)

        elif 'evtAqProd' in xml:
            schema_filename = '%s/%s/evtAqProd.xsd' % (tipo, versao)

        elif 'evtComProd' in xml:
            schema_filename = '%s/%s/evtComProd.xsd' % (tipo, versao)

        elif 'evtContratAvNP' in xml:
            schema_filename = '%s/%s/evtContratAvNP.xsd' % (tipo, versao)

        elif 'evtInfoComplPer' in xml:
            schema_filename = '%s/%s/evtInfoComplPer.xsd' % (tipo, versao)

        elif 'evtTotConting' in xml:
            schema_filename = '%s/%s/evtTotConting.xsd' % (tipo, versao)

        elif 'evtReabreEvPer' in xml:
            schema_filename = '%s/%s/evtReabreEvPer.xsd' % (tipo, versao)

        elif 'evtFechaEvPer' in xml:
            schema_filename = '%s/%s/evtFechaEvPer.xsd' % (tipo, versao)

        elif 'evtContrSindPatr' in xml:
            schema_filename = '%s/%s/evtContrSindPatr.xsd' % (tipo, versao)

        elif 'evtAdmPrelim' in xml:
            schema_filename = '%s/%s/evtAdmPrelim.xsd' % (tipo, versao)

        elif 'evtAdmissao' in xml:
            schema_filename = '%s/%s/evtAdmissao.xsd' % (tipo, versao)

        elif 'evtAltCadastral' in xml:
            schema_filename = '%s/%s/evtAltCadastral.xsd' % (tipo, versao)

        elif 'evtAltContratual' in xml:
            schema_filename = '%s/%s/evtAltContratual.xsd' % (tipo, versao)

        elif 'evtCAT' in xml:
            schema_filename = '%s/%s/evtCAT.xsd' % (tipo, versao)

        elif 'evtMonit' in xml:
            schema_filename = '%s/%s/evtMonit.xsd' % (tipo, versao)

        elif 'evtAfastTemp' in xml:
            schema_filename = '%s/%s/evtAfastTemp.xsd' % (tipo, versao)

        elif 'evtExpRisco' in xml:
            schema_filename = '%s/%s/evtExpRisco.xsd' % (tipo, versao)

        elif 'evtInsApo' in xml:
            schema_filename = '%s/%s/evtInsApo.xsd' % (tipo, versao)

        elif 'evtAvPrevio' in xml:
            schema_filename = '%s/%s/evtAvPrevio.xsd' % (tipo, versao)

        elif 'evtConvInterm' in xml:
            schema_filename = '%s/%s/evtConvInterm.xsd' % (tipo, versao)

        elif 'evtReintegr' in xml:
            schema_filename = '%s/%s/evtReintegr.xsd' % (tipo, versao)

        elif 'evtDeslig' in xml:
            schema_filename = '%s/%s/evtDeslig.xsd' % (tipo, versao)

        elif 'evtTSVInicio' in xml:
            schema_filename = '%s/%s/evtTSVInicio.xsd' % (tipo, versao)

        elif 'evtTSVAltContr' in xml:
            schema_filename = '%s/%s/evtTSVAltContr.xsd' % (tipo, versao)

        elif 'evtTSVTermino' in xml:
            schema_filename = '%s/%s/evtTSVTermino.xsd' % (tipo, versao)

        elif 'evtCdBenPrRP' in xml:
            schema_filename = '%s/%s/evtCdBenPrRP.xsd' % (tipo, versao)

        elif 'evtExclusao' in xml:
            schema_filename = '%s/%s/evtExclusao.xsd' % (tipo, versao)

        elif 'evtBasesTrab' in xml:
            schema_filename = '%s/%s/evtBasesTrab.xsd' % (tipo, versao)

        elif 'evtIrrfBenef' in xml:
            schema_filename = '%s/%s/evtIrrfBenef.xsd' % (tipo, versao)

        elif 'evtCS' in xml:
            schema_filename = '%s/%s/evtCS.xsd' % (tipo, versao)

        elif 'evtIrrf' in xml:
            schema_filename = '%s/%s/evtIrrf.xsd' % (tipo, versao)

    if tipo == 'efdreinf':

        if 'evtInfoContri' in xml:
            schema_filename = '%s/%s/evtInfoContribuinte.xsd' % (tipo, versao)

        elif 'evtTabProcesso' in xml:
            schema_filename = '%s/%s/evtTabProcesso.xsd' % (tipo, versao)

        elif 'evtServTom' in xml:
            schema_filename = '%s/%s/evtTomadorServicos.xsd' % (tipo, versao)

        elif 'evtServPrest' in xml:
            schema_filename = '%s/%s/evtPrestadorServicos.xsd' % (tipo, versao)

        elif 'evtAssocDespRec' in xml:
            schema_filename = '%s/%s/evtRecursoRecebidoAssociacao.xsd' % (tipo, versao)

        elif 'evtAssocDespRep' in xml:
            schema_filename = '%s/%s/evtRecursoRepassadoAssociacao.xsd' % (tipo, versao)

        elif 'evtComProd' in xml:
            schema_filename = '%s/%s/evtInfoProdRural.xsd' % (tipo, versao)

        elif 'evtCPRB' in xml:
            schema_filename = '%s/%s/evtInfoCPRB.xsd' % (tipo, versao)

        elif 'evtPgtosDivs' in xml:
            schema_filename = '%s/%s/r2070_evtpgtosdivs' % (tipo, versao)

        elif 'evtReabreEvPer' in xml:
            schema_filename = '%s/%s/evtReabreEvPer.xsd' % (tipo, versao)

        elif 'evtFechaEvPer' in xml:
            schema_filename = '%s/%s/evtFechamento.xsd' % (tipo, versao)

        elif 'evtEspDesportivo' in xml:
            schema_filename = '%s/%s/evtEspDesportivo.xsd' % (tipo, versao)

        elif 'evtTotal' in xml:
            schema_filename = '%s/%s/r5001_evttotal' % (tipo, versao)

        elif 'evtTotalContrib' in xml:
            schema_filename = '%s/%s/r5011_evttotalcontrib' % (tipo, versao)

        elif 'evtExclusao' in xml:
            schema_filename = '%s/%s/evtExclusao.xsd' % (tipo, versao)

    return schema_filename


def validar_campo(validacoes_lista, evento_campo, valor, obrigatorio, valores_validos):
    if obrigatorio:
        if not valor:
            validacoes_lista.append(u'O valor do campo %s é obrigatório' % (evento_campo))
        if valores_validos and valor not in valores_validos:
            validacoes_lista.append(u'O valor do campo %s é %s, não está dentro dos valores válidos permitidos (valores permitidos: %s) ' % (evento_campo, valor, valores_validos))
    if not obrigatorio and valor and valores_validos:
        if valor not in valores_validos:
            validacoes_lista.append(u'O valor do campo %s é %s, não está dentro dos valores válidos permitidos (valores permitidos: %s) ' % (evento_campo, valor, valores_validos))

    return validacoes_lista