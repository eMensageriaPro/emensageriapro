# eMensageriaAI #
# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.controle_de_acesso.models import *


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






class form_config_perfis(forms.ModelForm):


    def __init__(self, *args, **kwargs):

        super(form_config_perfis, self).__init__(*args, **kwargs)


    def save(self, commit=True, *args, **kwargs):

        request = None

        if kwargs.has_key('request'):

            request = kwargs.pop('request')

        m =  super(form_config_perfis, self).save(commit=True, *args, **kwargs)

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

        model = ConfigPerfis
        exclude = [
            'criado_em',
            'criado_por',
            'modificado_em',
            'modificado_por',
            'desativado_em',
            'desativado_por',]


from django.contrib.auth.models import User


class form_users(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(form_users, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['required'] = True
        self.fields['first_name'].widget.attrs['required'] = True
        self.fields['last_name'].widget.attrs['required'] = True
        self.fields['email'].widget.attrs['required'] = True
        self.fields['is_superuser'].widget.attrs['required'] = True

    class Meta:

        model = User
        exclude = [
            'password',
            'last_login',
            'date_joined',
            'groups',
            'user_permissions',
        ]


class form_usuarios(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super (form_usuarios, self ).__init__(*args, **kwargs)
        self.fields['config_perfis'].widget.attrs['required'] = True
        self.fields['name'].widget.attrs['required'] = True

    class Meta:

        model = Usuarios
        exclude = [
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'desativado_em', 'desativado_por',
            'ativo', 'user',
        ]