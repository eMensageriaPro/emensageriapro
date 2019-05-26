# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s5011.models import *


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






class form_s5011_basesaquis(forms.ModelForm):

    vlraquis = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenarnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpcalcpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratcalcpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenarcalc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_basesaquis, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_basesaquis, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011basesAquis
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_basesavnport(forms.ModelForm):

    vrbccp00 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp13 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbcfgts = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrdesccp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_basesavnport, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_basesavnport, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011basesAvNPort
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_basescomerc(forms.ModelForm):

    vrbccompr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenarsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_basescomerc, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_basescomerc, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011basesComerc
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_basesremun(forms.ModelForm):

    vrbccp00 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrbccp25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsuspbccp00 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsuspbccp15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsuspbccp20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsuspbccp25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrdescsest = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcalcsest = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrdescsenat = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcalcsenat = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsalfam = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsalmat = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_basesremun, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_basesremun, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011basesRemun
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_dadosopport(forms.ModelForm):

    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_dadosopport, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_dadosopport, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011dadosOpPort
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_ideestab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_ideestab, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_ideestab, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011ideEstab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_idelotacao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_idelotacao, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_idelotacao, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011ideLotacao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infoatconc(forms.ModelForm):

    fatormes = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )
    fator13 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infoatconc, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infoatconc, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoAtConc
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infocpseg(forms.ModelForm):

    vrdesccp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpseg = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infocpseg, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infocpseg, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoCPSeg
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infocrcontrib(forms.ModelForm):

    vrcr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcrsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infocrcontrib, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infocrcontrib, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoCRContrib
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infocrestab(forms.ModelForm):

    vrcr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsuspcr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infocrestab, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infocrestab, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoCREstab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infocomplobra(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infocomplobra, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infocomplobra, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoComplObra
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infoemprparcial(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infoemprparcial, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infoemprparcial, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoEmprParcial
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infoestab(forms.ModelForm):

    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=True, )

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infoestab, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infoestab, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoEstab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infopj(forms.ModelForm):

    percredcontrib = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )

    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infopj, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infopj, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoPJ
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infosubstpatropport(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infosubstpatropport, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infosubstpatropport, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoSubstPatrOpPort
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]


class form_s5011_infotercsusp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_infotercsusp, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_infotercsusp, self).save(commit=True, *args, **kwargs)

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
    
        model = s5011infoTercSusp
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',]