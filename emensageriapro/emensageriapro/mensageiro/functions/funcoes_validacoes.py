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


def validar_schema(request, file_schema_xsd, file_xml, lang=None):

    from emensageriapro.settings import BASE_DIR
    from googletrans import Translator
    import os.path

    file_schema_xsd = BASE_DIR + '/xsd/' + file_schema_xsd

    # print file_schema_xsd

    if os.path.isfile(file_schema_xsd):

        file_xml = BASE_DIR + '/' + file_xml

        schema = etree.parse(file_schema_xsd)
        xmlschema = etree.XMLSchema(schema)

        quant_erros = 0

        try:
            document = etree.parse(file_xml)

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

    else:

        from django.contrib import messages

        messages.warning(request, '''
                        Não foi validar o evento pelo XSD pois o mesmo 
                        não está contido na pasta!''')

        return 0, []


def get_schema_name(arquivo):
    from emensageriapro.functions import get_versao_evento, get_evento_nome
    from emensageriapro.padrao import ler_arquivo

    xml = ler_arquivo(arquivo).replace("s:", "")

    if 'eSocial' in xml:
        tipo = 'esocial'

    elif 'Reinf' in xml:
        tipo = 'efdreinf'

    versao = get_versao_evento(xml)

    evento_nome = get_evento_nome(xml)

    schema_filename = '%s/%s/%s.xsd' % (tipo, versao, evento_nome)

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