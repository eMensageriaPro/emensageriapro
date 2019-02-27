# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1207.models import * 
from emensageriapro.esocial.models import s1207evtBenPrRP 


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




class form_s1207_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_dmdev, self).__init__(*args,**kwargs)
        
        self.fields['s1207_evtbenprrp'].queryset = s1207evtBenPrRP.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_evtbenprrp'].widget.attrs['required'] = True        
        self.fields['tpbenef'].widget.attrs['required'] = True        
        self.fields['nrbenefic'].widget.attrs['required'] = True        
        self.fields['idedmdev'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_dmdev, self).save(commit=True, *args, **kwargs)

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
        model = s1207dmDev
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_infoperant_ideadc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_infoperant_ideadc, self).__init__(*args,**kwargs)
        
        self.fields['s1207_dmdev'].queryset = s1207dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_dmdev'].widget.attrs['required'] = True        
        self.fields['tpacconv'].widget.attrs['required'] = True        
        self.fields['dsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_infoperant_ideadc, self).save(commit=True, *args, **kwargs)

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
        model = s1207infoPerAntideADC
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_infoperant_ideestab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_infoperant_ideestab, self).__init__(*args,**kwargs)
        
        self.fields['s1207_infoperant_ideperiodo'].queryset = s1207infoPerAntidePeriodo.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_infoperant_ideperiodo'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_infoperant_ideestab, self).save(commit=True, *args, **kwargs)

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
        model = s1207infoPerAntideEstab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_infoperant_ideperiodo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_infoperant_ideperiodo, self).__init__(*args,**kwargs)
        
        self.fields['s1207_infoperant_ideadc'].queryset = s1207infoPerAntideADC.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_infoperant_ideadc'].widget.attrs['required'] = True        
        self.fields['perref'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_infoperant_ideperiodo, self).save(commit=True, *args, **kwargs)

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
        model = s1207infoPerAntidePeriodo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_infoperant_itensremun(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_infoperant_itensremun, self).__init__(*args,**kwargs)
        
        self.fields['s1207_infoperant_ideestab'].queryset = s1207infoPerAntideEstab.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_infoperant_ideestab'].widget.attrs['required'] = True        
        self.fields['codrubr'].widget.attrs['required'] = True        
        self.fields['idetabrubr'].widget.attrs['required'] = True        
        self.fields['vrrubr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_infoperant_itensremun, self).save(commit=True, *args, **kwargs)

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
        model = s1207infoPerAntitensRemun
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_infoperapur_ideestab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_infoperapur_ideestab, self).__init__(*args,**kwargs)
        
        self.fields['s1207_dmdev'].queryset = s1207dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_dmdev'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_infoperapur_ideestab, self).save(commit=True, *args, **kwargs)

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
        model = s1207infoPerApurideEstab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_infoperapur_itensremun(forms.ModelForm):
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_infoperapur_itensremun, self).__init__(*args,**kwargs)
        
        self.fields['s1207_infoperapur_ideestab'].queryset = s1207infoPerApurideEstab.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_infoperapur_ideestab'].widget.attrs['required'] = True        
        self.fields['codrubr'].widget.attrs['required'] = True        
        self.fields['idetabrubr'].widget.attrs['required'] = True        
        self.fields['vrrubr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_infoperapur_itensremun, self).save(commit=True, *args, **kwargs)

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
        model = s1207infoPerApuritensRemun
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_itens(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_itens, self).__init__(*args,**kwargs)
        
        self.fields['s1207_dmdev'].queryset = s1207dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_dmdev'].widget.attrs['required'] = True        
        self.fields['codrubr'].widget.attrs['required'] = True        
        self.fields['idetabrubr'].widget.attrs['required'] = True        
        self.fields['vrrubr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_itens, self).save(commit=True, *args, **kwargs)

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
        model = s1207itens
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1207_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1207_procjudtrab, self).__init__(*args,**kwargs)
        
        self.fields['s1207_evtbenprrp'].queryset = s1207evtBenPrRP.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1207_evtbenprrp'].widget.attrs['required'] = True        
        self.fields['tptrib'].widget.attrs['required'] = True        
        self.fields['nrprocjud'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_procjudtrab, self).save(commit=True, *args, **kwargs)

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
        model = s1207procJudTrab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

