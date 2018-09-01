# coding: utf-8
from django import forms
from emensageriapro.r2030.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r2030evtAssocDespRec 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r2030_infoproc(forms.ModelForm):
    vlrnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2030_infoproc,self ).__init__(*args,**kwargs)
        
        self.fields['vlrnret'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['r2030_recursosrec'].queryset = r2030recursosRec.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2030_recursosrec'].widget.attrs['required'] = True

    class Meta:
        model = r2030infoProc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2030_inforecurso(forms.ModelForm):
    vlrretapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2030_inforecurso,self ).__init__(*args,**kwargs)
        
        self.fields['vlrretapur'].widget.attrs['required'] = True
        
        self.fields['vlrbruto'].widget.attrs['required'] = True
        
        self.fields['descrecurso'].widget.attrs['required'] = True
        
        self.fields['tprepasse'].widget.attrs['required'] = True
        self.fields['r2030_recursosrec'].queryset = r2030recursosRec.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2030_recursosrec'].widget.attrs['required'] = True

    class Meta:
        model = r2030infoRecurso
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2030_recursosrec(forms.ModelForm):
    vlrtotalnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalrec = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2030_recursosrec,self ).__init__(*args,**kwargs)
        
        self.fields['vlrtotalret'].widget.attrs['required'] = True
        
        self.fields['vlrtotalrec'].widget.attrs['required'] = True
        
        self.fields['cnpjorigrecurso'].widget.attrs['required'] = True
        self.fields['r2030_evtassocdesprec'].queryset = r2030evtAssocDespRec.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2030_evtassocdesprec'].widget.attrs['required'] = True

    class Meta:
        model = r2030recursosRec
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

