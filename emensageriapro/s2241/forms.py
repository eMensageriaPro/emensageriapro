# coding: utf-8
from django import forms
from emensageriapro.s2241.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import eSocialFatoresRisco 
from emensageriapro.esocial.models import s2241evtInsApo 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2241_insalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_insalperic,self ).__init__(*args,**kwargs)
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241insalPeric
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_iniinsalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniinsalperic,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_insalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniInsalPeric
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_iniinsalperic_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniinsalperic_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_iniinsalperic'].queryset = s2241iniInsalPeric.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniinsalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniInsalPericinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_iniinsalperic_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniinsalperic_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_iniinsalperic_infoamb'].queryset = s2241iniInsalPericinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniinsalperic_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniInsalPericfatRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_altinsalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altinsalperic,self ).__init__(*args,**kwargs)
        
        self.fields['dtaltcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_insalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241altInsalPeric
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_altinsalperic_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altinsalperic_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_altinsalperic'].queryset = s2241altInsalPeric.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altinsalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241altInsalPericinfoamb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_altinsalperic_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altinsalperic_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_altinsalperic_infoamb'].queryset = s2241altInsalPericinfoamb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altinsalperic_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241altInsalPericfatRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_fiminsalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fiminsalperic,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_insalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimInsalPeric
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_fiminsalperic_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fiminsalperic_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_fiminsalperic'].queryset = s2241fimInsalPeric.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_fiminsalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimInsalPericinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_aposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_aposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241aposentEsp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_iniaposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniaposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_aposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniAposentEsp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_iniaposentesp_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniaposentesp_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_iniaposentesp'].queryset = s2241iniAposentEsp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniaposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniAposentEspinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_iniaposentesp_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniaposentesp_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_iniaposentesp_infoamb'].queryset = s2241iniAposentEspinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniaposentesp_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniAposentEspfatRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_altaposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altaposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['dtaltcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_aposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241altAposentEsp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_altaposentesp_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altaposentesp_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_altaposentesp'].queryset = s2241altAposentEsp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altaposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241altAposentEspinfoamb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_altaposentesp_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altaposentesp_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_altaposentesp_infoamb'].queryset = s2241altAposentEspinfoamb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altaposentesp_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241altAposentEspfatRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_fimaposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fimaposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_aposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimAposentEsp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2241_fimaposentesp_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fimaposentesp_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_fimaposentesp'].queryset = s2241fimAposentEsp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_fimaposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimAposentEspinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

