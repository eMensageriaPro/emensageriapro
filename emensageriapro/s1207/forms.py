# eMensageriaAI #
# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1207.models import *


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






class form_s1207_dmdev(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_dmdev, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_dmdev, self).save(commit=True, *args, **kwargs)

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

        model = s1207dmDev
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperant(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperant, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperant, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerAnt
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperant_ideadc(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperant_ideadc, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperant_ideadc, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerAntideADC
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperant_ideestab(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperant_ideestab, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperant_ideestab, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerAntideEstab
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperant_ideperiodo(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperant_ideperiodo, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperant_ideperiodo, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerAntidePeriodo
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperant_itensremun(forms.ModelForm):

    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperant_itensremun, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperant_itensremun, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerAntitensRemun
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperant_remunperant(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperant_remunperant, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperant_remunperant, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerAntremunPerAnt
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperapur(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperapur, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperapur, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerApur
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperapur_ideestab(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperapur_ideestab, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperapur_ideestab, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerApurideEstab
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperapur_itensremun(forms.ModelForm):

    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperapur_itensremun, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperapur_itensremun, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerApuritensRemun
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_infoperapur_remunperapur(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_infoperapur_remunperapur, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_infoperapur_remunperapur, self).save(commit=True, *args, **kwargs)

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

        model = s1207infoPerApurremunPerApur
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_itens(forms.ModelForm):

    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_s1207_itens, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_itens, self).save(commit=True, *args, **kwargs)

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

        model = s1207itens
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s1207_procjudtrab(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s1207_procjudtrab, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s1207_procjudtrab, self).save(commit=True, *args, **kwargs)

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

        model = s1207procJudTrab
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]