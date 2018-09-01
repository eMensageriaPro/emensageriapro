# coding: utf-8
from django import forms
from emensageriapro.s2205.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.esocial.models import s2205evtAltCadastral 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2205_contato(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_contato,self ).__init__(*args,**kwargs)
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205contato
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_aposentadoria(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_aposentadoria,self ).__init__(*args,**kwargs)
        
        self.fields['trabaposent'].widget.attrs['required'] = True
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205aposentadoria
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_dependente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_dependente,self ).__init__(*args,**kwargs)
        
        self.fields['inctrab'].widget.attrs['required'] = True
        
        self.fields['depsf'].widget.attrs['required'] = True
        
        self.fields['depirrf'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        self.fields['s2205_evtaltcadastral'].queryset = s2205evtAltCadastral.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205dependente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_infodeficiencia(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_infodeficiencia,self ).__init__(*args,**kwargs)
        
        self.fields['reabreadap'].widget.attrs['required'] = True
        
        self.fields['defintelectual'].widget.attrs['required'] = True
        
        self.fields['defmental'].widget.attrs['required'] = True
        
        self.fields['defauditiva'].widget.attrs['required'] = True
        
        self.fields['defvisual'].widget.attrs['required'] = True
        
        self.fields['deffisica'].widget.attrs['required'] = True
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205infoDeficiencia
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_trabestrangeiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_trabestrangeiro,self ).__init__(*args,**kwargs)
        
        self.fields['filhosbr'].widget.attrs['required'] = True
        
        self.fields['casadobr'].widget.attrs['required'] = True
        
        self.fields['classtrabestrang'].widget.attrs['required'] = True
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205trabEstrangeiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['paisresid'].widget.attrs['required'] = True
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205exterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_brasil(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_brasil,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205brasil
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_cnh(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_cnh,self ).__init__(*args,**kwargs)
        
        self.fields['categoriacnh'].widget.attrs['required'] = True
        
        self.fields['dtvalid'].widget.attrs['required'] = True
        
        self.fields['ufcnh'].widget.attrs['required'] = True
        
        self.fields['nrregcnh'].widget.attrs['required'] = True
        
        self.fields['s2205_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2205CNH
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_oc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_oc,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['s2205_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2205OC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_rne(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_rne,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrrne'].widget.attrs['required'] = True
        
        self.fields['s2205_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2205RNE
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_rg(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_rg,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrrg'].widget.attrs['required'] = True
        
        self.fields['s2205_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2205RG
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_ric(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_ric,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrric'].widget.attrs['required'] = True
        
        self.fields['s2205_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2205RIC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_ctps(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_ctps,self ).__init__(*args,**kwargs)
        
        self.fields['ufctps'].widget.attrs['required'] = True
        
        self.fields['seriectps'].widget.attrs['required'] = True
        
        self.fields['nrctps'].widget.attrs['required'] = True
        
        self.fields['s2205_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2205CTPS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2205_documentos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_documentos,self ).__init__(*args,**kwargs)
        
        self.fields['s2205_evtaltcadastral'].widget.attrs['required'] = True

    class Meta:
        model = s2205documentos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

