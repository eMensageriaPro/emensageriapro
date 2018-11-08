# coding: utf-8
from django import forms
from emensageriapro.s1020.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1020evtTabLotacao 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1020_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['codtercs'].widget.attrs['required'] = True
        
        self.fields['fpas'].widget.attrs['required'] = True
        
        self.fields['tplotacao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['s1020_evttablotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao_infoprocjudterceiros(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao_infoprocjudterceiros,self ).__init__(*args,**kwargs)
        
        self.fields['s1020_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusaoinfoProcJudTerceiros
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao_procjudterceiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao_procjudterceiro,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['codterc'].widget.attrs['required'] = True
        self.fields['s1020_inclusao_infoprocjudterceiros'].queryset = s1020inclusaoinfoProcJudTerceiros.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1020_inclusao_infoprocjudterceiros'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusaoprocJudTerceiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_inclusao_infoemprparcial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_inclusao_infoemprparcial,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscprop'].widget.attrs['required'] = True
        
        self.fields['tpinscprop'].widget.attrs['required'] = True
        
        self.fields['nrinsccontrat'].widget.attrs['required'] = True
        
        self.fields['tpinsccontrat'].widget.attrs['required'] = True
        
        self.fields['s1020_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1020inclusaoinfoEmprParcial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['codtercs'].widget.attrs['required'] = True
        
        self.fields['fpas'].widget.attrs['required'] = True
        
        self.fields['tplotacao'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['s1020_evttablotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_infoprocjudterceiros(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_infoprocjudterceiros,self ).__init__(*args,**kwargs)
        
        self.fields['s1020_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaoinfoProcJudTerceiros
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_procjudterceiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_procjudterceiro,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['codterc'].widget.attrs['required'] = True
        self.fields['s1020_alteracao_infoprocjudterceiros'].queryset = s1020alteracaoinfoProcJudTerceiros.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1020_alteracao_infoprocjudterceiros'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaoprocJudTerceiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_infoemprparcial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_infoemprparcial,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscprop'].widget.attrs['required'] = True
        
        self.fields['tpinscprop'].widget.attrs['required'] = True
        
        self.fields['nrinsccontrat'].widget.attrs['required'] = True
        
        self.fields['tpinsccontrat'].widget.attrs['required'] = True
        
        self.fields['s1020_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaoinfoEmprParcial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1020_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1020alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1020_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['s1020_evttablotacao'].widget.attrs['required'] = True

    class Meta:
        model = s1020exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

