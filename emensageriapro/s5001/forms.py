# coding: utf-8
from django import forms
from emensageriapro.s5001.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s5001evtBasesTrab 


__author__ = 'marcelovasconcellos'



#custom_forms#



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
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
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
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
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
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s5001_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_ideestablot,self ).__init__(*args,**kwargs)
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s5001_infocp'].queryset = s5001infoCp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5001_infocp'].widget.attrs['required'] = True

    class Meta:
        model = s5001ideEstabLot
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s5001_infocp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_infocp,self ).__init__(*args,**kwargs)
        
        self.fields['s5001_evtbasestrab'].widget.attrs['required'] = True

    class Meta:
        model = s5001infoCp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
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
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


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
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

