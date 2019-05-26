# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.r9002.models import *


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






class form_r9002_infototal(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9002_infototal, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_infototal, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002infoTotal
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_r9002_regocorrs(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9002_regocorrs, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_regocorrs, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002regOcorrs
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_r9002_totapurdec(forms.ModelForm):

    vlrbasecrdec = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrdec = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasecrdecsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrdecsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r9002_totapurdec, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_totapurdec, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002totApurDec
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_r9002_totapurdia(forms.ModelForm):

    vlrbasecrdia = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrdia = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasecrdiasusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrdiasusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r9002_totapurdia, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_totapurdia, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002totApurDia
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_r9002_totapurmen(forms.ModelForm):

    vlrbasecrmen = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrmen = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasecrmensusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrmensusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r9002_totapurmen, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_totapurmen, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002totApurMen
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_r9002_totapurqui(forms.ModelForm):

    vlrbasecrqui = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrqui = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasecrquisusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrquisusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r9002_totapurqui, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_totapurqui, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002totApurQui
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_r9002_totapursem(forms.ModelForm):

    vlrbasecrsem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrsem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbasecrsemsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrsemsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r9002_totapursem, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_totapursem, self).save(commit=True, *args, **kwargs)

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
    
        model = r9002totApurSem
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]