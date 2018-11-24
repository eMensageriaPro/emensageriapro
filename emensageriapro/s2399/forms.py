# coding: utf-8
from django import forms
from emensageriapro.s2399.models import * 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s2399evtTSVTermino 


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



class form_s2399_detoper(forms.ModelForm):
    vrpgtit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_detoper,self ).__init__(*args,**kwargs)
        self.fields['s2399_ideestablot'].queryset = s2399ideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True
        
        self.fields['cnpjoper'].widget.attrs['required'] = True
        
        self.fields['regans'].widget.attrs['required'] = True
        
        self.fields['vrpgtit'].widget.attrs['required'] = True

    class Meta:
        model = s2399detOper
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_detplano(forms.ModelForm):
    vlrpgdep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_detplano,self ).__init__(*args,**kwargs)
        self.fields['s2399_detoper'].queryset = s2399detOper.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_detoper'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['vlrpgdep'].widget.attrs['required'] = True

    class Meta:
        model = s2399detPlano
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_detverbas(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_detverbas,self ).__init__(*args,**kwargs)
        self.fields['s2399_ideestablot'].queryset = s2399ideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['vrrubr'].widget.attrs['required'] = True

    class Meta:
        model = s2399detVerbas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_dmdev,self ).__init__(*args,**kwargs)
        self.fields['s2399_evttsvtermino'].queryset = s2399evtTSVTermino.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True
        
        self.fields['idedmdev'].widget.attrs['required'] = True

    class Meta:
        model = s2399dmDev
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_ideestablot,self ).__init__(*args,**kwargs)
        self.fields['s2399_dmdev'].queryset = s2399dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_dmdev'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True

    class Meta:
        model = s2399ideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infoagnocivo,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True
        
        self.fields['grauexp'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoAgNocivo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_infomv(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infomv,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True
        
        self.fields['indmv'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoMV
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_infosimples(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infosimples,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True
        
        self.fields['indsimples'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoSimples
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_mudancacpf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_mudancacpf,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True
        
        self.fields['novocpf'].widget.attrs['required'] = True

    class Meta:
        model = s2399mudancaCPF
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_procjudtrab,self ).__init__(*args,**kwargs)
        self.fields['s2399_evttsvtermino'].queryset = s2399evtTSVTermino.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True
        
        self.fields['tptrib'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True

    class Meta:
        model = s2399procJudTrab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_quarentena(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_quarentena,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True
        
        self.fields['dtfimquar'].widget.attrs['required'] = True

    class Meta:
        model = s2399quarentena
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2399_remunoutrempr(forms.ModelForm):
    vlrremunoe = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_remunoutrempr,self ).__init__(*args,**kwargs)
        self.fields['s2399_infomv'].queryset = s2399infoMV.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_infomv'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['vlrremunoe'].widget.attrs['required'] = True

    class Meta:
        model = s2399remunOutrEmpr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

