# coding: utf-8
from django import forms
from emensageriapro.s2399.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2399evtTSVTermino 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2399_quarentena(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_quarentena,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimquar'].widget.attrs['required'] = True
        
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True

    class Meta:
        model = s2399quarentena
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_remunoutrempr(forms.ModelForm):
    vlrremunoe = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_remunoutrempr,self ).__init__(*args,**kwargs)
        
        self.fields['vlrremunoe'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s2399_infomv'].queryset = s2399infoMV.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_infomv'].widget.attrs['required'] = True

    class Meta:
        model = s2399remunOutrEmpr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_infomv(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infomv,self ).__init__(*args,**kwargs)
        
        self.fields['indmv'].widget.attrs['required'] = True
        
        self.fields['s2399_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoMV
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_procjudtrab,self ).__init__(*args,**kwargs)
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['tptrib'].widget.attrs['required'] = True
        self.fields['s2399_verbasresc'].queryset = s2399verbasResc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2399procJudTrab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_infosimples(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infosimples,self ).__init__(*args,**kwargs)
        
        self.fields['indsimples'].widget.attrs['required'] = True
        
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoSimples
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infoagnocivo,self ).__init__(*args,**kwargs)
        
        self.fields['grauexp'].widget.attrs['required'] = True
        
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoAgNocivo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_detplano(forms.ModelForm):
    vlrpgdep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_detplano,self ).__init__(*args,**kwargs)
        
        self.fields['vlrpgdep'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        self.fields['s2399_detoper'].queryset = s2399detOper.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_detoper'].widget.attrs['required'] = True

    class Meta:
        model = s2399detPlano
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_detoper(forms.ModelForm):
    vrpgtit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_detoper,self ).__init__(*args,**kwargs)
        
        self.fields['vrpgtit'].widget.attrs['required'] = True
        
        self.fields['regans'].widget.attrs['required'] = True
        
        self.fields['cnpjoper'].widget.attrs['required'] = True
        self.fields['s2399_infosaudecolet'].queryset = s2399infoSaudeColet.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_infosaudecolet'].widget.attrs['required'] = True

    class Meta:
        model = s2399detOper
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_infosaudecolet(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_infosaudecolet,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2399infoSaudeColet
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_detverbas(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_detverbas,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s2399_ideestablot'].queryset = s2399ideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2399detVerbas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_ideestablot,self ).__init__(*args,**kwargs)
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s2399_dmdev'].queryset = s2399dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_dmdev'].widget.attrs['required'] = True

    class Meta:
        model = s2399ideEstabLot
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_dmdev,self ).__init__(*args,**kwargs)
        
        self.fields['idedmdev'].widget.attrs['required'] = True
        self.fields['s2399_verbasresc'].queryset = s2399verbasResc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2399_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2399dmDev
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2399_verbasresc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_verbasresc,self ).__init__(*args,**kwargs)
        
        self.fields['s2399_evttsvtermino'].widget.attrs['required'] = True

    class Meta:
        model = s2399verbasResc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

