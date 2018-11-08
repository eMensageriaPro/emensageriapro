# coding: utf-8
from django import forms
from emensageriapro.s2206.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialLogradourosTipos 
from emensageriapro.esocial.models import s2206evtAltContratual 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2206_infoceletista(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_infoceletista,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjsindcategprof'].widget.attrs['required'] = True
        
        self.fields['natatividade'].widget.attrs['required'] = True
        
        self.fields['tpregjor'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206infoCeletista
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_trabtemp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_trabtemp,self ).__init__(*args,**kwargs)
        
        self.fields['justprorr'].widget.attrs['required'] = True
        
        self.fields['s2206_infoceletista'].widget.attrs['required'] = True

    class Meta:
        model = s2206trabTemp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_aprend(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_aprend,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s2206_infoceletista'].widget.attrs['required'] = True

    class Meta:
        model = s2206aprend
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_infoestatutario(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_infoestatutario,self ).__init__(*args,**kwargs)
        
        self.fields['tpplanrp'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206infoEstatutario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_localtrabgeral(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_localtrabgeral,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206localTrabGeral
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_localtrabdom(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_localtrabdom,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206localTrabDom
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_horcontratual(forms.ModelForm):
    qtdhrssem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_horcontratual,self ).__init__(*args,**kwargs)
        
        self.fields['tmpparc'].widget.attrs['required'] = True
        
        self.fields['tpjornada'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206horContratual
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_horario(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_horario,self ).__init__(*args,**kwargs)
        
        self.fields['codhorcontrat'].widget.attrs['required'] = True
        
        self.fields['dia'].widget.attrs['required'] = True
        self.fields['s2206_horcontratual'].queryset = s2206horContratual.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2206_horcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206horario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_filiacaosindical(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_filiacaosindical,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjsindtrab'].widget.attrs['required'] = True
        self.fields['s2206_evtaltcontratual'].queryset = s2206evtAltContratual.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206filiacaoSindical
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_alvarajudicial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_alvarajudicial,self ).__init__(*args,**kwargs)
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206alvaraJudicial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_observacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_observacoes,self ).__init__(*args,**kwargs)
        
        self.fields['observacao'].widget.attrs['required'] = True
        self.fields['s2206_evtaltcontratual'].queryset = s2206evtAltContratual.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206observacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2206_servpubl(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_servpubl,self ).__init__(*args,**kwargs)
        
        self.fields['mtvalter'].widget.attrs['required'] = True
        
        self.fields['s2206_evtaltcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2206servPubl
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

