# coding: utf-8
from django import forms
from emensageriapro.s1200.models import * 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s1200evtRemun 


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



class form_s1200_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_dmdev,self ).__init__(*args,**kwargs)
        self.fields['s1200_evtremun'].queryset = s1200evtRemun.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_evtremun'].widget.attrs['required'] = True
        
        self.fields['idedmdev'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True

    class Meta:
        model = s1200dmDev
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infocomplem(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infocomplem,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_evtremun'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoComplem
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infointerm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infointerm,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_evtremun'].widget.attrs['required'] = True
        
        self.fields['qtddiasinterm'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoInterm
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infomv(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infomv,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_evtremun'].widget.attrs['required'] = True
        
        self.fields['indmv'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoMV
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_ideadc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_ideadc,self ).__init__(*args,**kwargs)
        self.fields['s1200_dmdev'].queryset = s1200dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_dmdev'].widget.attrs['required'] = True
        
        self.fields['tpacconv'].widget.attrs['required'] = True
        
        self.fields['dsc'].widget.attrs['required'] = True
        
        self.fields['remunsuc'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntideADC
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_ideestablot,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperant_ideperiodo'].queryset = s1200infoPerAntidePeriodo.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperant_ideperiodo'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_ideperiodo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_ideperiodo,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperant_ideadc'].queryset = s1200infoPerAntideADC.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperant_ideadc'].widget.attrs['required'] = True
        
        self.fields['perref'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntidePeriodo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_infoagnocivo,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_infoperant_remunperant'].widget.attrs['required'] = True
        
        self.fields['grauexp'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntinfoAgNocivo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_infocomplcont(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_infocomplcont,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_dmdev'].widget.attrs['required'] = True
        
        self.fields['codcbo'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntinfoComplCont
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_infotrabinterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_infotrabinterm,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperant_remunperant'].queryset = s1200infoPerAntremunPerAnt.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperant_remunperant'].widget.attrs['required'] = True
        
        self.fields['codconv'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntinfoTrabInterm
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_itensremun(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_itensremun,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperant_remunperant'].queryset = s1200infoPerAntremunPerAnt.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperant_remunperant'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['vrrubr'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntitensRemun
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperant_remunperant(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperant_remunperant,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperant_ideestablot'].queryset = s1200infoPerAntideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperant_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerAntremunPerAnt
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_detoper(forms.ModelForm):
    vrpgtit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_detoper,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperapur_remunperapur'].queryset = s1200infoPerApurremunPerApur.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperapur_remunperapur'].widget.attrs['required'] = True
        
        self.fields['cnpjoper'].widget.attrs['required'] = True
        
        self.fields['regans'].widget.attrs['required'] = True
        
        self.fields['vrpgtit'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApurdetOper
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_detplano(forms.ModelForm):
    vlrpgdep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_detplano,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperapur_detoper'].queryset = s1200infoPerApurdetOper.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperapur_detoper'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['vlrpgdep'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApurdetPlano
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_ideestablot,self ).__init__(*args,**kwargs)
        self.fields['s1200_dmdev'].queryset = s1200dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_dmdev'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApurideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_infoagnocivo,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_infoperapur_remunperapur'].widget.attrs['required'] = True
        
        self.fields['grauexp'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApurinfoAgNocivo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_infotrabinterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_infotrabinterm,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperapur_remunperapur'].queryset = s1200infoPerApurremunPerApur.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperapur_remunperapur'].widget.attrs['required'] = True
        
        self.fields['codconv'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApurinfoTrabInterm
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_itensremun(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_itensremun,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperapur_remunperapur'].queryset = s1200infoPerApurremunPerApur.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperapur_remunperapur'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['vrrubr'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApuritensRemun
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_infoperapur_remunperapur(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_infoperapur_remunperapur,self ).__init__(*args,**kwargs)
        self.fields['s1200_infoperapur_ideestablot'].queryset = s1200infoPerApurideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infoperapur_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s1200infoPerApurremunPerApur
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_procjudtrab,self ).__init__(*args,**kwargs)
        self.fields['s1200_evtremun'].queryset = s1200evtRemun.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_evtremun'].widget.attrs['required'] = True
        
        self.fields['tptrib'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True

    class Meta:
        model = s1200procJudTrab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_remunoutrempr(forms.ModelForm):
    vlrremunoe = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_remunoutrempr,self ).__init__(*args,**kwargs)
        self.fields['s1200_infomv'].queryset = s1200infoMV.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1200_infomv'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['vlrremunoe'].widget.attrs['required'] = True

    class Meta:
        model = s1200remunOutrEmpr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1200_sucessaovinc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_sucessaovinc,self ).__init__(*args,**kwargs)
        
        self.fields['s1200_infocomplem'].widget.attrs['required'] = True
        
        self.fields['tpinscant'].widget.attrs['required'] = True
        
        self.fields['cnpjempregant'].widget.attrs['required'] = True
        
        self.fields['dtadm'].widget.attrs['required'] = True

    class Meta:
        model = s1200sucessaoVinc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

