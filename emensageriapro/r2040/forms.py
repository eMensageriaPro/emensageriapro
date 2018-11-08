# coding: utf-8
from django import forms
from emensageriapro.r2040.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r2040evtAssocDespRep 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r2040_infoproc(forms.ModelForm):
    vlrnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2040_infoproc,self ).__init__(*args,**kwargs)
        
        self.fields['vlrnret'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['r2040_recursosrep'].queryset = r2040recursosRep.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2040_recursosrep'].widget.attrs['required'] = True

    class Meta:
        model = r2040infoProc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2040_inforecurso(forms.ModelForm):
    vlrretapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2040_inforecurso,self ).__init__(*args,**kwargs)
        
        self.fields['vlrretapur'].widget.attrs['required'] = True
        
        self.fields['vlrbruto'].widget.attrs['required'] = True
        
        self.fields['descrecurso'].widget.attrs['required'] = True
        
        self.fields['tprepasse'].widget.attrs['required'] = True
        self.fields['r2040_recursosrep'].queryset = r2040recursosRep.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2040_recursosrep'].widget.attrs['required'] = True

    class Meta:
        model = r2040infoRecurso
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2040_recursosrep(forms.ModelForm):
    vlrtotalnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalrep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2040_recursosrep,self ).__init__(*args,**kwargs)
        
        self.fields['vlrtotalret'].widget.attrs['required'] = True
        
        self.fields['vlrtotalrep'].widget.attrs['required'] = True
        
        self.fields['cnpjassocdesp'].widget.attrs['required'] = True
        self.fields['r2040_evtassocdesprep'].queryset = r2040evtAssocDespRep.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2040_evtassocdesprep'].widget.attrs['required'] = True

    class Meta:
        model = r2040recursosRep
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

