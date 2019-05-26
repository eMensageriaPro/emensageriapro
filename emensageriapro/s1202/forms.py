# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1202.models import *


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






class form_s1202_dmdev(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_dmdev, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_dmdev, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202dmDev
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperant(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperant, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperant, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerAnt
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperant_ideadc(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperant_ideadc, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperant_ideadc, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerAntideADC
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperant_ideestab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperant_ideestab, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperant_ideestab, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerAntideEstab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperant_ideperiodo(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperant_ideperiodo, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperant_ideperiodo, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerAntidePeriodo
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperant_itensremun(forms.ModelForm):

    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperant_itensremun, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperant_itensremun, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerAntitensRemun
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperant_remunperant(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperant_remunperant, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperant_remunperant, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerAntremunPerAnt
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApur
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur_detoper(forms.ModelForm):

    vrpgtit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur_detoper, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur_detoper, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApurdetOper
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur_detplano(forms.ModelForm):

    vlrpgdep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur_detplano, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur_detplano, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApurdetPlano
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur_ideestab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur_ideestab, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur_ideestab, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApurideEstab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur_infosaudecolet(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur_infosaudecolet, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur_infosaudecolet, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApurinfoSaudeColet
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur_itensremun(forms.ModelForm):

    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur_itensremun, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur_itensremun, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApuritensRemun
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_infoperapur_remunperapur(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_infoperapur_remunperapur, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_infoperapur_remunperapur, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202infoPerApurremunPerApur
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s1202_procjudtrab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_procjudtrab, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_procjudtrab, self).save(commit=True, *args, **kwargs)

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
    
        model = s1202procJudTrab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]