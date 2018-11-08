# coding: utf-8
from django import forms
from emensageriapro.s2306.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.esocial.models import s2306evtTSVAltContr 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2306_infoestagiario(forms.ModelForm):
    vlrbolsa = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_infoestagiario,self ).__init__(*args,**kwargs)
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['dtprevterm'].widget.attrs['required'] = True
        
        self.fields['nivestagio'].widget.attrs['required'] = True
        
        self.fields['natestagio'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306infoEstagiario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_ageintegracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_ageintegracao,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjagntinteg'].widget.attrs['required'] = True
        
        self.fields['s2306_infoestagiario'].widget.attrs['required'] = True

    class Meta:
        model = s2306ageIntegracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_infocomplementares(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_infocomplementares,self ).__init__(*args,**kwargs)
        
        self.fields['s2306_evttsvaltcontr'].widget.attrs['required'] = True

    class Meta:
        model = s2306infoComplementares
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_cargofuncao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_cargofuncao,self ).__init__(*args,**kwargs)
        
        self.fields['codcargo'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306cargoFuncao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_remuneracao(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_remuneracao,self ).__init__(*args,**kwargs)
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306remuneracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_infotrabcedido(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_infotrabcedido,self ).__init__(*args,**kwargs)
        
        self.fields['indremuncargo'].widget.attrs['required'] = True
        
        self.fields['s2306_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2306infoTrabCedido
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2306_supervisorestagio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_supervisorestagio,self ).__init__(*args,**kwargs)
        
        self.fields['nmsuperv'].widget.attrs['required'] = True
        
        self.fields['cpfsupervisor'].widget.attrs['required'] = True
        
        self.fields['s2306_infoestagiario'].widget.attrs['required'] = True

    class Meta:
        model = s2306supervisorEstagio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

