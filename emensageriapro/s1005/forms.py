# coding: utf-8
from django import forms
from emensageriapro.s1005.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1005evtTabEstab 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1005_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s1005_evttabestab'].widget.attrs['required'] = True

    class Meta:
        model = s1005exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_infopcd(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_infopcd,self ).__init__(*args,**kwargs)
        
        self.fields['contpcd'].widget.attrs['required'] = True
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaoinfoPCD
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_infoenteduc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_infoenteduc,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        self.fields['s1005_alteracao'].queryset = s1005alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaoinfoEntEduc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_infoobra(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_infoobra,self ).__init__(*args,**kwargs)
        
        self.fields['indsubstpatrobra'].widget.attrs['required'] = True
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaoinfoObra
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_infocaepf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_infocaepf,self ).__init__(*args,**kwargs)
        
        self.fields['tpcaepf'].widget.attrs['required'] = True
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaoinfoCaepf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_procadmjudfap(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_procadmjudfap,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaoprocAdmJudFap
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao_procadmjudrat(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao_procadmjudrat,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracaoprocAdmJudRat
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_alteracao(forms.ModelForm):
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['contapr'].widget.attrs['required'] = True
        
        self.fields['regpt'].widget.attrs['required'] = True
        
        self.fields['aliqrat'].widget.attrs['required'] = True
        
        self.fields['cnaeprep'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s1005_evttabestab'].widget.attrs['required'] = True

    class Meta:
        model = s1005alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao_infopcd(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao_infopcd,self ).__init__(*args,**kwargs)
        
        self.fields['contpcd'].widget.attrs['required'] = True
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusaoinfoPCD
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao_infoenteduc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao_infoenteduc,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        self.fields['s1005_inclusao'].queryset = s1005inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1005_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusaoinfoEntEduc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao_infoobra(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao_infoobra,self ).__init__(*args,**kwargs)
        
        self.fields['indsubstpatrobra'].widget.attrs['required'] = True
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusaoinfoObra
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao_infocaepf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao_infocaepf,self ).__init__(*args,**kwargs)
        
        self.fields['tpcaepf'].widget.attrs['required'] = True
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusaoinfoCaepf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao_procadmjudfap(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao_procadmjudfap,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusaoprocAdmJudFap
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao_procadmjudrat(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao_procadmjudrat,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusaoprocAdmJudRat
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1005_inclusao(forms.ModelForm):
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['contapr'].widget.attrs['required'] = True
        
        self.fields['regpt'].widget.attrs['required'] = True
        
        self.fields['aliqrat'].widget.attrs['required'] = True
        
        self.fields['cnaeprep'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s1005_evttabestab'].widget.attrs['required'] = True

    class Meta:
        model = s1005inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

