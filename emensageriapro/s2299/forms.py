# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s2299.models import * 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s2299evtDeslig 


__author__ = 'marcelovasconcellos'

"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

#custom_forms#




class form_s2299_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_dmdev, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['idedmdev'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_dmdev, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299dmDev
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperant_detverbas(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperant_detverbas, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperant_ideestablot'].queryset = s2299infoPerAntideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant_ideestablot'].widget.attrs['required'] = True        
        self.fields['codrubr'].widget.attrs['required'] = True        
        self.fields['idetabrubr'].widget.attrs['required'] = True        
        self.fields['vrrubr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperant_detverbas, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerAntdetVerbas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperant_ideadc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperant_ideadc, self).__init__(*args,**kwargs)
        
        self.fields['s2299_dmdev'].queryset = s2299dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_dmdev'].widget.attrs['required'] = True        
        self.fields['dtacconv'].widget.attrs['required'] = True        
        self.fields['tpacconv'].widget.attrs['required'] = True        
        self.fields['dtefacconv'].widget.attrs['required'] = True        
        self.fields['dsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperant_ideadc, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerAntideADC
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperant_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperant_ideestablot, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperant_ideperiodo'].queryset = s2299infoPerAntidePeriodo.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant_ideperiodo'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['codlotacao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperant_ideestablot, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerAntideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperant_ideperiodo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperant_ideperiodo, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperant_ideadc'].queryset = s2299infoPerAntideADC.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant_ideadc'].widget.attrs['required'] = True        
        self.fields['perref'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperant_ideperiodo, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerAntidePeriodo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperant_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperant_infoagnocivo, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperant_ideestablot'].widget.attrs['required'] = True        
        self.fields['grauexp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperant_infoagnocivo, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerAntinfoAgNocivo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperant_infosimples(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperant_infosimples, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperant_ideestablot'].widget.attrs['required'] = True        
        self.fields['indsimples'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperant_infosimples, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerAntinfoSimples
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperapur_detoper(forms.ModelForm):
    vrpgtit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperapur_detoper, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperapur_ideestablot'].queryset = s2299infoPerApurideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True        
        self.fields['cnpjoper'].widget.attrs['required'] = True        
        self.fields['regans'].widget.attrs['required'] = True        
        self.fields['vrpgtit'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperapur_detoper, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerApurdetOper
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperapur_detplano(forms.ModelForm):
    vlrpgdep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperapur_detplano, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperapur_detoper'].queryset = s2299infoPerApurdetOper.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur_detoper'].widget.attrs['required'] = True        
        self.fields['tpdep'].widget.attrs['required'] = True        
        self.fields['nmdep'].widget.attrs['required'] = True        
        self.fields['dtnascto'].widget.attrs['required'] = True        
        self.fields['vlrpgdep'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperapur_detplano, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerApurdetPlano
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperapur_detverbas(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperapur_detverbas, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperapur_ideestablot'].queryset = s2299infoPerApurideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True        
        self.fields['codrubr'].widget.attrs['required'] = True        
        self.fields['idetabrubr'].widget.attrs['required'] = True        
        self.fields['vrrubr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperapur_detverbas, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerApurdetVerbas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperapur_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperapur_ideestablot, self).__init__(*args,**kwargs)
        
        self.fields['s2299_dmdev'].queryset = s2299dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_dmdev'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['codlotacao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperapur_ideestablot, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerApurideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperapur_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperapur_infoagnocivo, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True        
        self.fields['grauexp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperapur_infoagnocivo, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerApurinfoAgNocivo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infoperapur_infosimples(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infoperapur_infosimples, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True        
        self.fields['indsimples'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infoperapur_infosimples, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoPerApurinfoSimples
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm, self).__init__(*args,**kwargs)
        
        self.fields['s2299_dmdev'].queryset = s2299dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_dmdev'].widget.attrs['required'] = True        
        self.fields['codconv'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabInterm
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm_consigfgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm_consigfgts, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['insconsig'].widget.attrs['required'] = True        
        self.fields['nrcontr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm_consigfgts, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabIntermconsigFGTS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm_infomv(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm_infomv, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['indmv'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm_infomv, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabInterminfoMV
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm_proccs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm_proccs, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['nrprocjud'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm_proccs, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabIntermprocCS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm_procjudtrab, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['tptrib'].widget.attrs['required'] = True        
        self.fields['nrprocjud'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm_procjudtrab, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabIntermprocJudTrab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm_quarentena(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm_quarentena, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['dtfimquar'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm_quarentena, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabIntermquarentena
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_infotrabinterm_remunoutrempr(forms.ModelForm):
    vlrremunoe = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_infotrabinterm_remunoutrempr, self).__init__(*args,**kwargs)
        
        self.fields['s2299_infotrabinterm_infomv'].queryset = s2299infoTrabInterminfoMV.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infotrabinterm_infomv'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['codcateg'].widget.attrs['required'] = True        
        self.fields['vlrremunoe'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_infotrabinterm_remunoutrempr, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299infoTrabIntermremunOutrEmpr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_mudancacpf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_mudancacpf, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['novocpf'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_mudancacpf, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299mudancaCPF
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_observacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_observacoes, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['observacao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_observacoes, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299observacoes
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_sucessaovinc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_sucessaovinc, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['tpinscsuc'].widget.attrs['required'] = True        
        self.fields['cnpjsucessora'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_sucessaovinc, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299sucessaoVinc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2299_transftit(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2299_transftit, self).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True        
        self.fields['cpfsubstituto'].widget.attrs['required'] = True        
        self.fields['dtnascto'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_transftit, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.excluido = False
            m.save()
        
        return m
        
    class Meta:
        model = s2299transfTit
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

