# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1260.models import * 
from emensageriapro.esocial.models import s1260evtComProd 


__author__ = 'marcelovasconcellos'

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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




class form_s1260_ideadquir(forms.ModelForm):
    vrcomerc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1260_ideadquir, self).__init__(*args,**kwargs)
        
        self.fields['s1260_tpcomerc'].queryset = s1260tpComerc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_tpcomerc'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['vrcomerc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1260_ideadquir, self).save(commit=True, *args, **kwargs)

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
        model = s1260ideAdquir
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1260_infoprocjud(forms.ModelForm):
    vrcpsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenarsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1260_infoprocjud, self).__init__(*args,**kwargs)
        
        self.fields['s1260_tpcomerc'].queryset = s1260tpComerc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_tpcomerc'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1260_infoprocjud, self).save(commit=True, *args, **kwargs)

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
        model = s1260infoProcJud
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1260_nfs(forms.ModelForm):
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1260_nfs, self).__init__(*args,**kwargs)
        
        self.fields['s1260_ideadquir'].queryset = s1260ideAdquir.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_ideadquir'].widget.attrs['required'] = True        
        self.fields['nrdocto'].widget.attrs['required'] = True        
        self.fields['dtemisnf'].widget.attrs['required'] = True        
        self.fields['vlrbruto'].widget.attrs['required'] = True        
        self.fields['vrcpdescpr'].widget.attrs['required'] = True        
        self.fields['vrratdescpr'].widget.attrs['required'] = True        
        self.fields['vrsenardesc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1260_nfs, self).save(commit=True, *args, **kwargs)

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
        model = s1260nfs
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1260_tpcomerc(forms.ModelForm):
    vrtotcom = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1260_tpcomerc, self).__init__(*args,**kwargs)
        
        self.fields['s1260_evtcomprod'].queryset = s1260evtComProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_evtcomprod'].widget.attrs['required'] = True        
        self.fields['indcomerc'].widget.attrs['required'] = True        
        self.fields['vrtotcom'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1260_tpcomerc, self).save(commit=True, *args, **kwargs)

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
        model = s1260tpComerc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

