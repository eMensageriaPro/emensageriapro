# coding: utf-8
from django import forms
from emensageriapro.s1050.models import * 
from emensageriapro.esocial.models import s1050evtTabHorTur 


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




class form_s1050_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1050_alteracao, self).__init__(*args,**kwargs)
        
        self.fields['s1050_evttabhortur'].widget.attrs['required'] = True        
        self.fields['codhorcontrat'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True        
        self.fields['hrentr'].widget.attrs['required'] = True        
        self.fields['hrsaida'].widget.attrs['required'] = True        
        self.fields['durjornada'].widget.attrs['required'] = True        
        self.fields['perhorflexivel'].widget.attrs['required'] = True
        
    class Meta:
        model = s1050alteracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1050_alteracao_horariointervalo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1050_alteracao_horariointervalo, self).__init__(*args,**kwargs)
        
        self.fields['s1050_alteracao'].queryset = s1050alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1050_alteracao'].widget.attrs['required'] = True        
        self.fields['tpinterv'].widget.attrs['required'] = True        
        self.fields['durinterv'].widget.attrs['required'] = True
        
    class Meta:
        model = s1050alteracaohorarioIntervalo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1050_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1050_alteracao_novavalidade, self).__init__(*args,**kwargs)
        
        self.fields['s1050_alteracao'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True
        
    class Meta:
        model = s1050alteracaonovaValidade
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1050_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1050_exclusao, self).__init__(*args,**kwargs)
        
        self.fields['s1050_evttabhortur'].widget.attrs['required'] = True        
        self.fields['codhorcontrat'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True
        
    class Meta:
        model = s1050exclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1050_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1050_inclusao, self).__init__(*args,**kwargs)
        
        self.fields['s1050_evttabhortur'].widget.attrs['required'] = True        
        self.fields['codhorcontrat'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True        
        self.fields['hrentr'].widget.attrs['required'] = True        
        self.fields['hrsaida'].widget.attrs['required'] = True        
        self.fields['durjornada'].widget.attrs['required'] = True        
        self.fields['perhorflexivel'].widget.attrs['required'] = True
        
    class Meta:
        model = s1050inclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1050_inclusao_horariointervalo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1050_inclusao_horariointervalo, self).__init__(*args,**kwargs)
        
        self.fields['s1050_inclusao'].queryset = s1050inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1050_inclusao'].widget.attrs['required'] = True        
        self.fields['tpinterv'].widget.attrs['required'] = True        
        self.fields['durinterv'].widget.attrs['required'] = True
        
    class Meta:
        model = s1050inclusaohorarioIntervalo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

