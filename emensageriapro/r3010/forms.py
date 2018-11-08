# coding: utf-8
from django import forms
from emensageriapro.r3010.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.efdreinf.models import r3010evtEspDesportivo 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r3010_infoproc(forms.ModelForm):
    vlrcpsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_infoproc,self ).__init__(*args,**kwargs)
        
        self.fields['vlrcpsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['r3010_ideestab'].queryset = r3010ideEstab.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_ideestab'].widget.attrs['required'] = True

    class Meta:
        model = r3010infoProc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r3010_outrasreceitas(forms.ModelForm):
    vlrreceita = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_outrasreceitas,self ).__init__(*args,**kwargs)
        
        self.fields['descreceita'].widget.attrs['required'] = True
        
        self.fields['vlrreceita'].widget.attrs['required'] = True
        
        self.fields['tpreceita'].widget.attrs['required'] = True
        self.fields['r3010_boletim'].queryset = r3010boletim.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_boletim'].widget.attrs['required'] = True

    class Meta:
        model = r3010outrasReceitas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r3010_receitaingressos(forms.ModelForm):
    vlrtotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    precoindiv = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_receitaingressos,self ).__init__(*args,**kwargs)
        
        self.fields['vlrtotal'].widget.attrs['required'] = True
        
        self.fields['precoindiv'].widget.attrs['required'] = True
        
        self.fields['qtdeingrdev'].widget.attrs['required'] = True
        
        self.fields['qtdeingrvendidos'].widget.attrs['required'] = True
        
        self.fields['qtdeingrvenda'].widget.attrs['required'] = True
        
        self.fields['descingr'].widget.attrs['required'] = True
        
        self.fields['tpingresso'].widget.attrs['required'] = True
        self.fields['r3010_boletim'].queryset = r3010boletim.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_boletim'].widget.attrs['required'] = True

    class Meta:
        model = r3010receitaIngressos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r3010_boletim(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_boletim,self ).__init__(*args,**kwargs)
        
        self.fields['qtdenaopagantes'].widget.attrs['required'] = True
        
        self.fields['qtdepagantes'].widget.attrs['required'] = True
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['pracadesportiva'].widget.attrs['required'] = True
        
        self.fields['cnpjmandante'].widget.attrs['required'] = True
        
        self.fields['nomecompeticao'].widget.attrs['required'] = True
        
        self.fields['moddesportiva'].widget.attrs['required'] = True
        
        self.fields['categevento'].widget.attrs['required'] = True
        
        self.fields['tpcompeticao'].widget.attrs['required'] = True
        
        self.fields['nrboletim'].widget.attrs['required'] = True
        self.fields['r3010_ideestab'].queryset = r3010ideEstab.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_ideestab'].widget.attrs['required'] = True

    class Meta:
        model = r3010boletim
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r3010_ideestab(forms.ModelForm):
    vlrretparc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrreceitaclubes = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrreceitatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_ideestab,self ).__init__(*args,**kwargs)
        
        self.fields['vlrretparc'].widget.attrs['required'] = True
        
        self.fields['vlrreceitaclubes'].widget.attrs['required'] = True
        
        self.fields['vlrcp'].widget.attrs['required'] = True
        
        self.fields['vlrreceitatotal'].widget.attrs['required'] = True
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        self.fields['r3010_evtespdesportivo'].queryset = r3010evtEspDesportivo.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_evtespdesportivo'].widget.attrs['required'] = True

    class Meta:
        model = r3010ideEstab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

