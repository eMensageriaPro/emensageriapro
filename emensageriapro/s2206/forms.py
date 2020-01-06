# eMensageriaAI #
# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s2206.models import *


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






class form_s2206_alvarajudicial(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_alvarajudicial, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_alvarajudicial, self).save(commit=True, *args, **kwargs)

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

        model = s2206alvaraJudicial
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_aprend(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_aprend, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_aprend, self).save(commit=True, *args, **kwargs)

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

        model = s2206aprend
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_filiacaosindical(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_filiacaosindical, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_filiacaosindical, self).save(commit=True, *args, **kwargs)

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

        model = s2206filiacaoSindical
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_horcontratual(forms.ModelForm):

    qtdhrssem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )

    def __init__(self, *args, **kwargs):

        super(form_s2206_horcontratual, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_horcontratual, self).save(commit=True, *args, **kwargs)

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

        model = s2206horContratual
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_horario(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_horario, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_horario, self).save(commit=True, *args, **kwargs)

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

        model = s2206horario
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_infoceletista(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_infoceletista, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_infoceletista, self).save(commit=True, *args, **kwargs)

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

        model = s2206infoCeletista
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_infoestatutario(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_infoestatutario, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_infoestatutario, self).save(commit=True, *args, **kwargs)

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

        model = s2206infoEstatutario
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_localtrabdom(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_localtrabdom, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_localtrabdom, self).save(commit=True, *args, **kwargs)

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

        model = s2206localTrabDom
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_localtrabgeral(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_localtrabgeral, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_localtrabgeral, self).save(commit=True, *args, **kwargs)

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

        model = s2206localTrabGeral
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_observacoes(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_observacoes, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_observacoes, self).save(commit=True, *args, **kwargs)

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

        model = s2206observacoes
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_servpubl(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_servpubl, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_servpubl, self).save(commit=True, *args, **kwargs)

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

        model = s2206servPubl
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]


class form_s2206_trabtemp(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2206_trabtemp, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2206_trabtemp, self).save(commit=True, *args, **kwargs)

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

        model = s2206trabTemp
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por',]