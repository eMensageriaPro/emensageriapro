# coding: utf-8
from django import forms
from emensageriapro.s1080.models import * 
from emensageriapro.esocial.models import s1080evtTabOperPort 


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



class form_s1080_inclusao(forms.ModelForm):
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['s1080_evttaboperport'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['aliqrat'].widget.attrs['required'] = True
        
        self.fields['fap'].widget.attrs['required'] = True
        
        self.fields['aliqratajust'].widget.attrs['required'] = True

    class Meta:
        model = s1080inclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1080_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['s1080_evttaboperport'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True

    class Meta:
        model = s1080exclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1080_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['s1080_alteracao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True

    class Meta:
        model = s1080alteracaonovaValidade
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1080_alteracao(forms.ModelForm):
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['s1080_evttaboperport'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['aliqrat'].widget.attrs['required'] = True
        
        self.fields['fap'].widget.attrs['required'] = True
        
        self.fields['aliqratajust'].widget.attrs['required'] = True

    class Meta:
        model = s1080alteracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

