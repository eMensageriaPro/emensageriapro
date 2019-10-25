# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.r4020.models import *


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






class form_r4020_csll(forms.ModelForm):

    vlrbasecsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasencsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrncsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdepcsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_csll, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_csll, self).save(commit=True, *args, **kwargs)

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

        model = r4020CSLL
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_cofins(forms.ModelForm):

    vlrbasecofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasencofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrncofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdepcofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_cofins, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_cofins, self).save(commit=True, *args, **kwargs)

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

        model = r4020Cofins
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_fci(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_r4020_fci, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_fci, self).save(commit=True, *args, **kwargs)

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

        model = r4020FCI
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_ir(forms.ModelForm):

    vlrbaseir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasenir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdepir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_ir, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_ir, self).save(commit=True, *args, **kwargs)

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

        model = r4020IR
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_pp(forms.ModelForm):

    vlrbasepp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrpp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasenpp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnpp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdeppp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_pp, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_pp, self).save(commit=True, *args, **kwargs)

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

        model = r4020PP
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_scp(forms.ModelForm):

    percscp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )

    def __init__(self, *args, **kwargs):

        super(form_r4020_scp, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_scp, self).save(commit=True, *args, **kwargs)

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

        model = r4020SCP
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_despprocjud(forms.ModelForm):

    vlrdespcustas = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdespadvogados = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_despprocjud, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_despprocjud, self).save(commit=True, *args, **kwargs)

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

        model = r4020despProcJud
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_ideadv(forms.ModelForm):

    vlradv = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_ideadv, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_ideadv, self).save(commit=True, *args, **kwargs)

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

        model = r4020ideAdv
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_idepgto(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_r4020_idepgto, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_idepgto, self).save(commit=True, *args, **kwargs)

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

        model = r4020idePgto
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_infopgto(forms.ModelForm):

    vlrtotalpag = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalcred = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_infopgto, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_infopgto, self).save(commit=True, *args, **kwargs)

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

        model = r4020infoPgto
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_infopgtoext(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_r4020_infopgtoext, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_infopgtoext, self).save(commit=True, *args, **kwargs)

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

        model = r4020infoPgtoExt
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_infoprocjud(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_r4020_infoprocjud, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_infoprocjud, self).save(commit=True, *args, **kwargs)

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

        model = r4020infoProcJud
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_infoprocret(forms.ModelForm):

    nir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    depir = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    ncsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    depcsll = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    ncofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    depcofins = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    npp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    deppp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):

        super(form_r4020_infoprocret, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_infoprocret, self).save(commit=True, *args, **kwargs)

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

        model = r4020infoProcRet
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]


class form_r4020_origemrec(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_r4020_origemrec, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')

        m =  super(form_r4020_origemrec, self).save(commit=True, *args, **kwargs)

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

        model = r4020origemRec
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'deativado_em',
            'deativado_por', ]