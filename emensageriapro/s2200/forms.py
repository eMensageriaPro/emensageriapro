# eMensageriaAI #
# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s2200.models import *


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






class form_s2200_cnh(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_cnh, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_cnh, self).save(commit=True, *args, **kwargs)

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

        model = s2200CNH
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_ctps(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_ctps, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_ctps, self).save(commit=True, *args, **kwargs)

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

        model = s2200CTPS
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_oc(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_oc, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_oc, self).save(commit=True, *args, **kwargs)

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

        model = s2200OC
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_rg(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_rg, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_rg, self).save(commit=True, *args, **kwargs)

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

        model = s2200RG
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_ric(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_ric, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_ric, self).save(commit=True, *args, **kwargs)

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

        model = s2200RIC
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_rne(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_rne, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_rne, self).save(commit=True, *args, **kwargs)

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

        model = s2200RNE
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_afastamento(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_afastamento, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_afastamento, self).save(commit=True, *args, **kwargs)

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

        model = s2200afastamento
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_alvarajudicial(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_alvarajudicial, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_alvarajudicial, self).save(commit=True, *args, **kwargs)

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

        model = s2200alvaraJudicial
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_aposentadoria(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_aposentadoria, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_aposentadoria, self).save(commit=True, *args, **kwargs)

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

        model = s2200aposentadoria
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_aprend(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_aprend, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_aprend, self).save(commit=True, *args, **kwargs)

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

        model = s2200aprend
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_brasil(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_brasil, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_brasil, self).save(commit=True, *args, **kwargs)

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

        model = s2200brasil
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_cessao(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_cessao, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_cessao, self).save(commit=True, *args, **kwargs)

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

        model = s2200cessao
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_contato(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_contato, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_contato, self).save(commit=True, *args, **kwargs)

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

        model = s2200contato
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_dependente(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_dependente, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_dependente, self).save(commit=True, *args, **kwargs)

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

        model = s2200dependente
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_desligamento(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_desligamento, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_desligamento, self).save(commit=True, *args, **kwargs)

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

        model = s2200desligamento
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_documentos(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_documentos, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_documentos, self).save(commit=True, *args, **kwargs)

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

        model = s2200documentos
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_exterior(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_exterior, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_exterior, self).save(commit=True, *args, **kwargs)

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

        model = s2200exterior
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_filiacaosindical(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_filiacaosindical, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_filiacaosindical, self).save(commit=True, *args, **kwargs)

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

        model = s2200filiacaoSindical
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_horcontratual(forms.ModelForm):

    qtdhrssem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )

    def __init__(self, *args, **kwargs):

        super(form_s2200_horcontratual, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_horcontratual, self).save(commit=True, *args, **kwargs)

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

        model = s2200horContratual
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_horario(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_horario, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_horario, self).save(commit=True, *args, **kwargs)

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

        model = s2200horario
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_ideestabvinc(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_ideestabvinc, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_ideestabvinc, self).save(commit=True, *args, **kwargs)

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

        model = s2200ideEstabVinc
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_idetrabsubstituido(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_idetrabsubstituido, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_idetrabsubstituido, self).save(commit=True, *args, **kwargs)

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

        model = s2200ideTrabSubstituido
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_infoceletista(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_infoceletista, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_infoceletista, self).save(commit=True, *args, **kwargs)

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

        model = s2200infoCeletista
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_infodecjud(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_infodecjud, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_infodecjud, self).save(commit=True, *args, **kwargs)

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

        model = s2200infoDecJud
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_infodeficiencia(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_infodeficiencia, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_infodeficiencia, self).save(commit=True, *args, **kwargs)

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

        model = s2200infoDeficiencia
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_infoestatutario(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_infoestatutario, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_infoestatutario, self).save(commit=True, *args, **kwargs)

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

        model = s2200infoEstatutario
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_localtrabdom(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_localtrabdom, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_localtrabdom, self).save(commit=True, *args, **kwargs)

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

        model = s2200localTrabDom
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_localtrabgeral(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_localtrabgeral, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_localtrabgeral, self).save(commit=True, *args, **kwargs)

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

        model = s2200localTrabGeral
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_mudancacpf(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_mudancacpf, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_mudancacpf, self).save(commit=True, *args, **kwargs)

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

        model = s2200mudancaCPF
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_observacoes(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_observacoes, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_observacoes, self).save(commit=True, *args, **kwargs)

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

        model = s2200observacoes
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_sucessaovinc(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_sucessaovinc, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_sucessaovinc, self).save(commit=True, *args, **kwargs)

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

        model = s2200sucessaoVinc
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_trabestrangeiro(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_trabestrangeiro, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_trabestrangeiro, self).save(commit=True, *args, **kwargs)

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

        model = s2200trabEstrangeiro
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_trabtemporario(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_trabtemporario, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_trabtemporario, self).save(commit=True, *args, **kwargs)

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

        model = s2200trabTemporario
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_s2200_transfdom(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_s2200_transfdom, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_s2200_transfdom, self).save(commit=True, *args, **kwargs)

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

        model = s2200transfDom
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]