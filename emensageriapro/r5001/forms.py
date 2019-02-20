# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.r5001.models import * 
from emensageriapro.efdreinf.models import r5001evtTotal 


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




class form_r5001_rcprb(forms.ModelForm):
    vlrcrcprb = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrcprbsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_rcprb, self).__init__(*args,**kwargs)
        
        self.fields['r5001_infototal'].queryset = r5001infoTotal.objects.using( slug ).filter(excluido=False).all()
        self.fields['r5001_infototal'].widget.attrs['required'] = True        
        self.fields['crcprb'].widget.attrs['required'] = True        
        self.fields['vlrcrcprb'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_rcprb, self).save(commit=True, *args, **kwargs)

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
        model = r5001RCPRB
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_rcoml(forms.ModelForm):
    vlrcrcoml = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrcomlsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_rcoml, self).__init__(*args,**kwargs)
        
        self.fields['r5001_infototal'].queryset = r5001infoTotal.objects.using( slug ).filter(excluido=False).all()
        self.fields['r5001_infototal'].widget.attrs['required'] = True        
        self.fields['crcoml'].widget.attrs['required'] = True        
        self.fields['vlrcrcoml'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_rcoml, self).save(commit=True, *args, **kwargs)

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
        model = r5001RComl
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_rprest(forms.ModelForm):
    vlrtotalbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_rprest, self).__init__(*args,**kwargs)
        
        self.fields['r5001_infototal'].widget.attrs['required'] = True        
        self.fields['tpinsctomador'].widget.attrs['required'] = True        
        self.fields['nrinsctomador'].widget.attrs['required'] = True        
        self.fields['vlrtotalbaseret'].widget.attrs['required'] = True        
        self.fields['vlrtotalretprinc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_rprest, self).save(commit=True, *args, **kwargs)

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
        model = r5001RPrest
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_rrecespetdesp(forms.ModelForm):
    vlrreceitatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrrecespetdesp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrrecespetdespsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_rrecespetdesp, self).__init__(*args,**kwargs)
        
        self.fields['r5001_infototal'].widget.attrs['required'] = True        
        self.fields['crrecespetdesp'].widget.attrs['required'] = True        
        self.fields['vlrreceitatotal'].widget.attrs['required'] = True        
        self.fields['vlrcrrecespetdesp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_rrecespetdesp, self).save(commit=True, *args, **kwargs)

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
        model = r5001RRecEspetDesp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_rrecrepad(forms.ModelForm):
    vlrtotalrep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrrecrepad = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrrecrepadsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_rrecrepad, self).__init__(*args,**kwargs)
        
        self.fields['r5001_infototal'].queryset = r5001infoTotal.objects.using( slug ).filter(excluido=False).all()
        self.fields['r5001_infototal'].widget.attrs['required'] = True        
        self.fields['cnpjassocdesp'].widget.attrs['required'] = True        
        self.fields['vlrtotalrep'].widget.attrs['required'] = True        
        self.fields['crrecrepad'].widget.attrs['required'] = True        
        self.fields['vlrcrrecrepad'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_rrecrepad, self).save(commit=True, *args, **kwargs)

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
        model = r5001RRecRepAD
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_rtom(forms.ModelForm):
    vlrtotalbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_rtom, self).__init__(*args,**kwargs)
        
        self.fields['r5001_infototal'].widget.attrs['required'] = True        
        self.fields['cnpjprestador'].widget.attrs['required'] = True        
        self.fields['vlrtotalbaseret'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_rtom, self).save(commit=True, *args, **kwargs)

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
        model = r5001RTom
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_infocrtom(forms.ModelForm):
    vlrcrtom = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcrtomsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_infocrtom, self).__init__(*args,**kwargs)
        
        self.fields['r5001_rtom'].queryset = r5001RTom.objects.using( slug ).filter(excluido=False).all()
        self.fields['r5001_rtom'].widget.attrs['required'] = True        
        self.fields['crtom'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_infocrtom, self).save(commit=True, *args, **kwargs)

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
        model = r5001infoCRTom
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_infototal(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_infototal, self).__init__(*args,**kwargs)
        
        self.fields['r5001_evttotal'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_infototal, self).save(commit=True, *args, **kwargs)

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
        model = r5001infoTotal
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r5001_regocorrs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r5001_regocorrs, self).__init__(*args,**kwargs)
        
        self.fields['r5001_evttotal'].queryset = r5001evtTotal.objects.using( slug ).filter(excluido=False).all()
        self.fields['r5001_evttotal'].widget.attrs['required'] = True        
        self.fields['tpocorr'].widget.attrs['required'] = True        
        self.fields['localerroaviso'].widget.attrs['required'] = True        
        self.fields['codresp'].widget.attrs['required'] = True        
        self.fields['dscresp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_regocorrs, self).save(commit=True, *args, **kwargs)

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
        model = r5001regOcorrs
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

