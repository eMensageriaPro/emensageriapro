# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1010.models import *


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






class form_s1010_alteracao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_alteracao_ideprocessocp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao_ideprocessocp, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao_ideprocessocp, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracaoideProcessoCP
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_alteracao_ideprocessocprp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao_ideprocessocprp, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao_ideprocessocprp, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracaoideProcessoCPRP
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_alteracao_ideprocessofgts(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao_ideprocessofgts, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao_ideprocessofgts, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracaoideProcessoFGTS
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_alteracao_ideprocessoirrf(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao_ideprocessoirrf, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao_ideprocessoirrf, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracaoideProcessoIRRF
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_alteracao_ideprocessosind(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao_ideprocessosind, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao_ideprocessosind, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracaoideProcessoSIND
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_alteracao_novavalidade(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_alteracao_novavalidade, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_alteracao_novavalidade, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010alteracaonovaValidade
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_exclusao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_exclusao, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_exclusao, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010exclusao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_inclusao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_inclusao, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_inclusao, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010inclusao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_inclusao_ideprocessocp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_inclusao_ideprocessocp, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_inclusao_ideprocessocp, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010inclusaoideProcessoCP
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_inclusao_ideprocessocprp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_inclusao_ideprocessocprp, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_inclusao_ideprocessocprp, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010inclusaoideProcessoCPRP
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_inclusao_ideprocessofgts(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_inclusao_ideprocessofgts, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_inclusao_ideprocessofgts, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010inclusaoideProcessoFGTS
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_inclusao_ideprocessoirrf(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_inclusao_ideprocessoirrf, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_inclusao_ideprocessoirrf, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010inclusaoideProcessoIRRF
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]


class form_s1010_inclusao_ideprocessosind(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_inclusao_ideprocessosind, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_inclusao_ideprocessosind, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = s1010inclusaoideProcessoSIND
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'deativado_em', 
            'deativado_por', ]