# coding: utf-8
from django import forms
from emensageriapro.s2210.models import * 
from emensageriapro.esocial.models import s2210evtCAT 


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




class form_s2210_agentecausador(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2210_agentecausador, self).__init__(*args,**kwargs)
        
        self.fields['s2210_evtcat'].queryset = s2210evtCAT.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2210_evtcat'].widget.attrs['required'] = True        
        self.fields['codagntcausador'].widget.attrs['required'] = True
        
    class Meta:
        model = s2210agenteCausador
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2210_atestado(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2210_atestado, self).__init__(*args,**kwargs)
        
        self.fields['s2210_evtcat'].widget.attrs['required'] = True        
        self.fields['dtatendimento'].widget.attrs['required'] = True        
        self.fields['hratendimento'].widget.attrs['required'] = True        
        self.fields['indinternacao'].widget.attrs['required'] = True        
        self.fields['durtrat'].widget.attrs['required'] = True        
        self.fields['indafast'].widget.attrs['required'] = True        
        self.fields['dsclesao'].widget.attrs['required'] = True        
        self.fields['codcid'].widget.attrs['required'] = True        
        self.fields['nmemit'].widget.attrs['required'] = True        
        self.fields['ideoc'].widget.attrs['required'] = True        
        self.fields['nroc'].widget.attrs['required'] = True
        
    class Meta:
        model = s2210atestado
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2210_catorigem(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2210_catorigem, self).__init__(*args,**kwargs)
        
        self.fields['s2210_evtcat'].widget.attrs['required'] = True        
        self.fields['dtcatorig'].widget.attrs['required'] = True        
        self.fields['nrreccatorig'].widget.attrs['required'] = True
        
    class Meta:
        model = s2210catOrigem
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2210_idelocalacid(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2210_idelocalacid, self).__init__(*args,**kwargs)
        
        self.fields['s2210_evtcat'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
    class Meta:
        model = s2210ideLocalAcid
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2210_parteatingida(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2210_parteatingida, self).__init__(*args,**kwargs)
        
        self.fields['s2210_evtcat'].queryset = s2210evtCAT.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2210_evtcat'].widget.attrs['required'] = True        
        self.fields['codparteating'].widget.attrs['required'] = True        
        self.fields['lateralidade'].widget.attrs['required'] = True
        
    class Meta:
        model = s2210parteAtingida
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

