# coding: utf-8
from django import forms
from emensageriapro.s2230.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2230evtAfastTemp 


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



class form_s2230_fimafastamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_fimafastamento,self ).__init__(*args,**kwargs)
        
        self.fields['dttermafast'].widget.attrs['required'] = True
        
        self.fields['s2230_evtafasttemp'].widget.attrs['required'] = True

    class Meta:
        model = s2230fimAfastamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_inforetif(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_inforetif,self ).__init__(*args,**kwargs)
        
        self.fields['origretif'].widget.attrs['required'] = True
        
        self.fields['s2230_evtafasttemp'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoRetif
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_infomandsind(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_infomandsind,self ).__init__(*args,**kwargs)
        
        self.fields['infonusremun'].widget.attrs['required'] = True
        
        self.fields['cnpjsind'].widget.attrs['required'] = True
        
        self.fields['s2230_iniafastamento'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoMandSind
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_infocessao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_infocessao,self ).__init__(*args,**kwargs)
        
        self.fields['infonus'].widget.attrs['required'] = True
        
        self.fields['cnpjcess'].widget.attrs['required'] = True
        
        self.fields['s2230_iniafastamento'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoCessao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_emitente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_emitente,self ).__init__(*args,**kwargs)
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['ideoc'].widget.attrs['required'] = True
        
        self.fields['nmemit'].widget.attrs['required'] = True
        
        self.fields['s2230_infoatestado'].widget.attrs['required'] = True

    class Meta:
        model = s2230emitente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_infoatestado(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_infoatestado,self ).__init__(*args,**kwargs)
        
        self.fields['qtddiasafast'].widget.attrs['required'] = True
        self.fields['s2230_iniafastamento'].queryset = s2230iniAfastamento.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2230_iniafastamento'].widget.attrs['required'] = True

    class Meta:
        model = s2230infoAtestado
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2230_iniafastamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_iniafastamento,self ).__init__(*args,**kwargs)
        
        self.fields['codmotafast'].widget.attrs['required'] = True
        
        self.fields['dtiniafast'].widget.attrs['required'] = True
        
        self.fields['s2230_evtafasttemp'].widget.attrs['required'] = True

    class Meta:
        model = s2230iniAfastamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

