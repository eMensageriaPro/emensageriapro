# eMensageriaAI #
# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.r2010.models import *


__author__ = 'marcelovasconcellos'


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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






class form_r2010_infoprocretad(forms.ModelForm):

    valoradic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r2010_infoprocretad, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r2010_infoprocretad, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()

        return m

    class Meta:

        model = r2010infoProcRetAd
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_r2010_infoprocretpr(forms.ModelForm):

    valorprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r2010_infoprocretpr, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r2010_infoprocretpr, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()

        return m

    class Meta:

        model = r2010infoProcRetPr
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_r2010_infotpserv(forms.ModelForm):

    vlrbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretencao = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretsub = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlradicional = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r2010_infotpserv, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r2010_infotpserv, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()

        return m

    class Meta:

        model = r2010infoTpServ
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_r2010_nfs(forms.ModelForm):

    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r2010_nfs, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r2010_nfs, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()

        return m

    class Meta:

        model = r2010nfs
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]