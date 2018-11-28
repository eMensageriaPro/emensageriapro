# coding: utf-8
from django import forms
from emensageriapro.s5001.models import * 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s5001evtBasesTrab 


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



class form_s5001_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_procjudtrab,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        self.fields['s5001_evtbasestrab'].queryset = s5001evtBasesTrab.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_evtbasestrab'].widget.attrs['required'] = True

    class Meta:
        model = s5001procJudTrab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5001_infocpcalc(forms.ModelForm):
    vrdescseg = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpseg = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_infocpcalc,self ).__init__(*args,**kwargs)
        
        self.fields['vrdescseg'].widget.attrs['required'] = True
        
        self.fields['vrcpseg'].widget.attrs['required'] = True
        
        self.fields['tpcr'].widget.attrs['required'] = True
        self.fields['s5001_evtbasestrab'].queryset = s5001evtBasesTrab.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_evtbasestrab'].widget.attrs['required'] = True

    class Meta:
        model = s5001infoCpCalc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5001_infocategincid(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_infocategincid,self ).__init__(*args,**kwargs)
        
        self.fields['codcateg'].widget.attrs['required'] = True
        self.fields['s5001_ideestablot'].queryset = s5001ideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s5001infoCategIncid
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5001_infobasecs(forms.ModelForm):
    valor = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_infobasecs,self ).__init__(*args,**kwargs)
        
        self.fields['valor'].widget.attrs['required'] = True
        
        self.fields['tpvalor'].widget.attrs['required'] = True
        
        self.fields['ind13'].widget.attrs['required'] = True
        self.fields['s5001_infocategincid'].queryset = s5001infoCategIncid.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_infocategincid'].widget.attrs['required'] = True

    class Meta:
        model = s5001infoBaseCS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5001_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_ideestablot,self ).__init__(*args,**kwargs)
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s5001_evtbasestrab'].queryset = s5001evtBasesTrab.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_evtbasestrab'].widget.attrs['required'] = True

    class Meta:
        model = s5001ideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5001_calcterc(forms.ModelForm):
    vrdescterc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcssegterc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_calcterc,self ).__init__(*args,**kwargs)
        
        self.fields['vrdescterc'].widget.attrs['required'] = True
        
        self.fields['vrcssegterc'].widget.attrs['required'] = True
        
        self.fields['tpcr'].widget.attrs['required'] = True
        self.fields['s5001_infocategincid'].queryset = s5001infoCategIncid.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_infocategincid'].widget.attrs['required'] = True

    class Meta:
        model = s5001calcTerc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

