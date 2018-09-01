# coding: utf-8
from django import forms
from emensageriapro.s1070.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.esocial.models import s1070evtTabProcesso 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1070_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1070_evttabprocesso'].widget.attrs['required'] = True

    class Meta:
        model = s1070exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1070_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1070alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_alteracao_infosusp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_alteracao_infosusp,self ).__init__(*args,**kwargs)
        
        self.fields['inddeposito'].widget.attrs['required'] = True
        
        self.fields['dtdecisao'].widget.attrs['required'] = True
        
        self.fields['indsusp'].widget.attrs['required'] = True
        
        self.fields['codsusp'].widget.attrs['required'] = True
        self.fields['s1070_alteracao'].queryset = s1070alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1070_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1070alteracaoinfoSusp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_alteracao_dadosprocjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_alteracao_dadosprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['idvara'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['ufvara'].widget.attrs['required'] = True
        
        self.fields['s1070_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1070alteracaodadosProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['indmatproc'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1070_evttabprocesso'].widget.attrs['required'] = True

    class Meta:
        model = s1070alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_inclusao_infosusp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_inclusao_infosusp,self ).__init__(*args,**kwargs)
        
        self.fields['inddeposito'].widget.attrs['required'] = True
        
        self.fields['dtdecisao'].widget.attrs['required'] = True
        
        self.fields['indsusp'].widget.attrs['required'] = True
        
        self.fields['codsusp'].widget.attrs['required'] = True
        self.fields['s1070_inclusao'].queryset = s1070inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1070_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1070inclusaoinfoSusp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_inclusao_dadosprocjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_inclusao_dadosprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['idvara'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['ufvara'].widget.attrs['required'] = True
        
        self.fields['s1070_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1070inclusaodadosProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1070_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['indmatproc'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        
        self.fields['s1070_evttabprocesso'].widget.attrs['required'] = True

    class Meta:
        model = s1070inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

