# coding: utf-8
from django import forms
from emensageriapro.controle_de_acesso.models import * 


__author__ = 'marcelovasconcellos'

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

#custom_forms#



class form_auditoria(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_auditoria,self ).__init__(*args,**kwargs)
        
        self.fields['tabela'].widget.attrs['required'] = True
        self.fields['tabela'].widget.attrs['readonly'] = True
        
        self.fields['identidade'].widget.attrs['required'] = True
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['situacao_anterior'].widget.attrs['required'] = True
        self.fields['situacao_anterior'].widget.attrs['readonly'] = True
        
        self.fields['situacao_posterior'].widget.attrs['required'] = True
        self.fields['situacao_posterior'].widget.attrs['readonly'] = True
        self.fields['operador'].queryset = Usuarios.objects.using( slug ).filter(excluido=False).all()
        self.fields['operador'].widget.attrs['required'] = True
        self.fields['operador'].widget.attrs['readonly'] = True
        
        self.fields['data_hora'].widget.attrs['required'] = True
        self.fields['data_hora'].widget.attrs['readonly'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True

    class Meta:
        model = Auditoria
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_usuarios(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_usuarios,self ).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['required'] = True
        
        self.fields['first_name'].widget.attrs['required'] = True
        
        self.fields['last_name'].widget.attrs['required'] = True
        
        self.fields['email'].widget.attrs['required'] = True
        self.fields['config_perfis'].queryset = ConfigPerfis.objects.using( slug ).filter(excluido=False).all()
        self.fields['config_perfis'].widget.attrs['required'] = True

    class Meta:
        model = Usuarios
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined',
 
        ]


class form_config_permissoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_config_permissoes,self ).__init__(*args,**kwargs)
        self.fields['config_perfis'].queryset = ConfigPerfis.objects.using( slug ).filter(excluido=False).all()
        self.fields['config_perfis'].widget.attrs['required'] = True
        self.fields['config_paginas'].queryset = ConfigPaginas.objects.using( slug ).filter(excluido=False).all()
        self.fields['config_paginas'].widget.attrs['required'] = True
        
        self.fields['permite_listar'].widget.attrs['required'] = True
        
        self.fields['permite_cadastrar'].widget.attrs['required'] = True
        
        self.fields['permite_editar'].widget.attrs['required'] = True
        
        self.fields['permite_visualizar'].widget.attrs['required'] = True
        
        self.fields['permite_apagar'].widget.attrs['required'] = True

    class Meta:
        model = ConfigPermissoes
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_config_perfis(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_config_perfis,self ).__init__(*args,**kwargs)
        
        self.fields['titulo'].widget.attrs['required'] = True

    class Meta:
        model = ConfigPerfis
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'permissoes',
            'modulos_permitidos',
            'paginas_permitidas',
 
        ]


class form_config_paginas(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_config_paginas,self ).__init__(*args,**kwargs)
        self.fields['config_modulos'].queryset = ConfigModulos.objects.using( slug ).filter(excluido=False).all()
        self.fields['config_modulos'].widget.attrs['required'] = True
        
        self.fields['titulo'].widget.attrs['required'] = True
        
        self.fields['endereco'].widget.attrs['required'] = True
        
        self.fields['exibe_menu'].widget.attrs['required'] = True
        
        self.fields['tipo'].widget.attrs['required'] = True
        
        self.fields['ordem'].widget.attrs['required'] = True

    class Meta:
        model = ConfigPaginas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_config_modulos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_config_modulos,self ).__init__(*args,**kwargs)
        
        self.fields['titulo'].widget.attrs['required'] = True
        
        self.fields['slug'].widget.attrs['required'] = True
        self.fields['modulo_pai'].queryset = ConfigModulos.objects.using( slug ).filter(excluido=False).all()
        
        self.fields['ordem'].widget.attrs['required'] = True

    class Meta:
        model = ConfigModulos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

