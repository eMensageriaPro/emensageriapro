#coding: utf-8
#templatetags.py

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

from django.db import models
from django import template
from emensageriapro.r3010.models import *
from emensageriapro.padrao import *
import decimal
import locale
try: locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except: locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

register = template.Library()

<<<<<<< HEAD
@register.filter(name='multiply')
def multiply(value, arg):
    return value*arg
=======

>>>>>>> 3217f7abcc9a9c37261d88e43626ba3e9fb91ee3

@register.filter(name='lista_json_table_esocial')
def lista_json_table_esocial(texto):
    texto = texto.replace('codresp','codigo').replace('dscresp','descricao').replace('localerroaviso','localizacao')
    html_txt = ''
    lista = texto.split('|')
    for txt in lista:
        dados = json_to_dict(str(txt))
        html_txt += '<strong>%(codigo)s - %(descricao)s</strong><br>(%(localizacao)s)<br>' % dados
    return html_txt
    

@register.filter(name='underline_to_hyphen')
def underline_to_hyphen(value):
    return value.replace("_", "-")

@register.filter(name='format_number_2dec_xml_reinf')
def format_number_2dec_xml_reinf(value):
    return str(value).replace('.',',')

@register.filter(name='format_number_4dec_xml_reinf')
def format_number_4dec_xml_reinf(value):
    return str(value).replace('.',',')



@register.filter(name='format_number_2dec_xml')
def format_number_2dec_xml(value):
    return "{:0.2f}".format(value)

@register.filter(name='format_number_4dec_xml')
def format_number_4dec_xml(value):
    return "{:0.4f}".format(value)

@register.filter(name='inteiro_xml')
def inteiro_xml(value):
    return str(int(value))

@register.filter(name='validacoes_esocial_efdreinf')
def validacoes_esocial_efdreinf(var, tab_campo):
    from emensageriapro.padrao import executar_sql
    tab = tab_campo.split('.')
    lista = executar_sql("""
    SELECT tipo, tamanho, casas_decimais, obrigatorio, 
          valores_validos, validacoes_precedencia, validacoes, elemento
      FROM public.regras_validacao WHERE tabela='%s' AND lower(registro_campo)='%s';
    """ % (tab[0], tab[1]), True)
    if lista:
        if not var and var != 0: var = ''
        dado = lista[0]
        dados = {}
        dados['tipo'] = dado[0] or ''
        dados['tamanho'] = dado[1] or ''
        if dados['tamanho'] == '-': dados['tamanho'] = 0
        dados['casas_decimais'] = dado[2] or ''
        dados['obrigatorio'] = dado[3] or ''
        dados['valores_validos'] = dado[4] or ''
        dados['validacoes_precedencia'] = dado[5] or ''
        dados['validacoes'] = dado[6] or ''
        dados['elemento'] = dado[7] or ''
        quant_erros = 0
        if 'nrinsc' == tab[1] or ('cpf' in tab[1] and var != ''):
            txt = validate_CPF(var)
            if not txt:
                quant_erros += 1
        if dados['elemento']=='E' and len(str(var)) > int(dados['tamanho']):
            quant_erros += 1
        if dados['obrigatorio'] and not var and var != 0:
            quant_erros += 1
        if dados['valores_validos'] and str(var) and (str(var) not in dados['valores_validos'].split(',') ):
            quant_erros += 1
        if quant_erros:
            return '#FF0000'
            


@register.assignment_tag
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)

@register.filter(name='to_xml')
def to_xml(texto):
    try:
        #texto = str(texto)
        texto = texto.replace(">",'&gt;')
        texto = texto.replace("<",'&lt;')
        texto = texto.replace("&",'&amp;')
        texto = texto.replace('"','&quot;')
        texto = texto.replace("'",'&apos;')
    except:
        pass
    return texto

@register.filter(name='auditoria_json')
def auditoria_json(texto):
    html = ''
    if texto:
        dados = json_to_dict(texto)
        for a in dados.keys():
            html += '<strong>%s:</strong> %s<br>' % (a, dados[a])
        return html
    else:
        return ''


@register.filter(name='dec_to_int')
def dec_to_int(var):
    return int(var)

@register.filter(name='valor')  
def valor(var):
    a = str(var).replace('.','')
    return a

@register.filter('json_tab')
def json_return_page(json_str, variavel):
    if json_str == '{}':
        json_str = json_str.replace('}', '"tab": "%s"}' % variavel)
    else:
        json_str = json_str.replace('}', ', "tab": "%s"}' % variavel)
    return json_str

@register.filter('json_return_page')
def json_return_page(json_str, variavel):
    if json_str == '{}':
        json_str = json_str.replace('}', '"return_page": "%s"}' % variavel)
    else:
        json_str = json_str.replace('}', ', "return_page": "%s"}' % variavel)
    return json_str

@register.filter('json_return_hash')
def json_return_hash(json_str, variavel):
    if json_str == '{}':
        json_str = json_str.replace('}', '"return_hash": "%s"}' % variavel)
    else:
        json_str = json_str.replace('}', ', "return_hash": "%s"}' % variavel)
    return json_str

@register.filter('json_id')
def json_id(json_str, variavel):
    if json_str == '{}':
        json_str = json_str.replace('}', '"id": "%s"}' % variavel)
    else:
        json_str = json_str.replace('}', ', "id": "%s"}' % variavel)
    return json_str

@register.filter('json_print')
def json_print(json_str, variavel):
    if json_str == '{}':
        json_str = json_str.replace('}', '"print": "%s"}' % variavel)
    else:
        json_str = json_str.replace('}', ', "print": "%s"}' % variavel)
    return json_str        


import re
from django.core.validators import EMPTY_VALUES


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0

@register.filter(name='validate_CPF')
def validate_CPF(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """
    value = value.replace('.','').replace('-','')
    if value in EMPTY_VALUES:
        return False
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        return False
    if len(value) != 11:
        return False
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        return False
    return True

@register.filter('addstr')
def addstr(arg1, arg2):
    # concatenate arg1 & arg2
    return str(arg1) + str(arg2)

@register.filter('add')
def add(arg1, arg2):
    # concatenate arg1 & arg2
    return str(arg1) + '|' + str(arg2)


@register.filter('get_permissao')
def get_permissao(dict, key):
    #print dict[str(key)], key
    try:
        if dict[ str(key) ] == 0:
            return False
        if dict[str(key)] == 1:
            return True
    except:
        return False

@register.filter('divide')
def divide(value, arg):
    if not arg:
        arg=0
    if not value:
        value=0
    #from __future__ import division
    quant_total = (arg*100.00)
    if int(quant_total) == 0:
        quant_total = 1
    quant_nao_enviado = (value*100.00)
    quant_enviado = quant_total - quant_nao_enviado
    #print quant_total, quant_nao_enviado, quant_enviado
    divide = (quant_enviado / quant_total)*100
    #print divide
    return int(divide)

#@register.filter('base64_encode_me')
#def base64_encode_me(text, obj_id):
#    url = str(text).replace('_', '-')
#    #print url
#    #print str(obj_id)
#    text = url+'|'+str(obj_id)
#    #print text
#    import base64
#    encode_to_url = base64.urlsafe_b64encode( text )
#    #print encode_to_url
#    return encode_to_url

@register.filter('base64_encode_me')
def base64_encode_me(text):
    import base64
    encode_to_url = base64.urlsafe_b64encode( text )
    return encode_to_url


@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    # 
    # usage example {{ your_dict|get_value_from_dict:your_key }}
    # 
    if key:
        a = dict_data.get(key)
        #print key, a
        try:
            a = int(a)
        except:
            pass
        if not a: a = ''
        return a

# @register.simple_tag
# def quant_eleitores_cidade(obj, conta_id):
#     quantidade = Eleitores.objects.using('default').filter(cidade=obj.id, conta=conta_id, excluido=False).all()
#     return len(quantidade)
#
# @register.simple_tag
# def quant_eleitores_partido(obj, conta_id):
#     quantidade = Eleitores.objects.using('default').filter(partido=obj.id, conta=conta_id, excluido=False).all()
#     return len(quantidade)

@register.filter(name='addcss')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='addcss_select2')
def addcss_select2(value, arg):
    return value.as_widget(attrs={'class': arg, 'style': 'width: 100%'})
#register = Library()



@register.filter(name='notNone')
def notNone(var):
    a = ''
    if var:
        a = var
    return a


@register.filter(name='mes_ano')  
def mes_ano(var):
    mes = var[4:7]
    ano = var[2:4]
    if mes == '01': mes = 'Jan/'
    if mes == '02': mes = 'Fev/'
    if mes == '03': mes = 'Mar/'
    if mes == '04': mes = 'Abr/'
    if mes == '05': mes = 'Mai/'
    if mes == '06': mes = 'Jun/'
    if mes == '07': mes = 'Jul/'
    if mes == '08': mes = 'Ago/'
    if mes == '09': mes = 'Set/'
    if mes == '10': mes = 'Out/'
    if mes == '11': mes = 'Nov/'
    if mes == '12': mes = 'Dez/'
    return mes+ano

@register.filter(name='ano_mes_extenso')
def ano_mes_extenso(value):
    a = value.split('-')
    ano = a[0]
    mes = a[1]
    if mes == '01': mes_extenso=u'Janeiro'
    elif mes == '02': mes_extenso=u'Fevereiro'
    elif mes == '03': mes_extenso=u'Março'
    elif mes == '04': mes_extenso=u'Abril'
    elif mes == '05': mes_extenso=u'Maio'
    elif mes == '06': mes_extenso=u'Junho'
    elif mes == '07': mes_extenso=u'Julho'
    elif mes == '08': mes_extenso=u'Agosto'
    elif mes == '09': mes_extenso=u'Setembro'
    elif mes == '10': mes_extenso=u'Outubro'
    elif mes == '11': mes_extenso=u'Novembro'
    elif mes == '12': mes_extenso=u'Dezembro'
    return mes_extenso + '/' + ano

# @register.filter(name='total')
# def total(list, arg):
#     soma = sum(d[arg] for d in list)
#     soma = round(soma, 2)
#     soma = soma*1.00
#     valor = real(soma)
#     return valor

@register.filter(name='inteiro')
def inteiro(var):
    #print var
    a = str(var).split('.')
    b = a[0]
    #print b
    return int(b)


@register.filter(name='padrao_americano')
def padrao_americano(var):
    #print var
    #a = str(var).replace('.','')
    #print a
    return str(var)


@register.filter(name='total_quant') 
def total_quant(list, arg):
    soma = sum( d[arg] for d in list)
    return soma

@register.filter(name='percentage')  
def percentage(fraction, population):  
    #{{ yes.count|percentage:votes.count }} votes.count - total ||| yes.count - parcial
    try:  
        return "%.2f%%" % ((float(fraction) / float(population)) * 100)  
    except ValueError:  
        return '' 