# coding: utf-8
from django import forms
from emensageriapro.r1000.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r1000evtInfoContri 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r1000_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['r1000_evtinfocontri'].widget.attrs['required'] = True

    class Meta:
        model = r1000exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['r1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = r1000alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_alteracao_infoefr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_alteracao_infoefr,self ).__init__(*args,**kwargs)
        
        self.fields['ideefr'].widget.attrs['required'] = True
        
        self.fields['r1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = r1000alteracaoinfoEFR
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_alteracao_softhouse(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_alteracao_softhouse,self ).__init__(*args,**kwargs)
        
        self.fields['nmcont'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjsofthouse'].widget.attrs['required'] = True
        self.fields['r1000_alteracao'].queryset = r1000alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['r1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = r1000alteracaosoftHouse
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['cpfctt'].widget.attrs['required'] = True
        
        self.fields['nmctt'].widget.attrs['required'] = True
        
        self.fields['indacordoisenmulta'].widget.attrs['required'] = True
        
        self.fields['inddesoneracao'].widget.attrs['required'] = True
        
        self.fields['indescrituracao'].widget.attrs['required'] = True
        
        self.fields['classtrib'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['r1000_evtinfocontri'].widget.attrs['required'] = True

    class Meta:
        model = r1000alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_inclusao_infoefr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_inclusao_infoefr,self ).__init__(*args,**kwargs)
        
        self.fields['ideefr'].widget.attrs['required'] = True
        
        self.fields['r1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = r1000inclusaoinfoEFR
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_inclusao_softhouse(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_inclusao_softhouse,self ).__init__(*args,**kwargs)
        
        self.fields['nmcont'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjsofthouse'].widget.attrs['required'] = True
        self.fields['r1000_inclusao'].queryset = r1000inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['r1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = r1000inclusaosoftHouse
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r1000_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['cpfctt'].widget.attrs['required'] = True
        
        self.fields['nmctt'].widget.attrs['required'] = True
        
        self.fields['indacordoisenmulta'].widget.attrs['required'] = True
        
        self.fields['inddesoneracao'].widget.attrs['required'] = True
        
        self.fields['indescrituracao'].widget.attrs['required'] = True
        
        self.fields['classtrib'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['r1000_evtinfocontri'].widget.attrs['required'] = True

    class Meta:
        model = r1000inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

