# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1070.models import * 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.esocial.models import s1070evtTabProcesso 


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




class form_s1070_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_alteracao, self).__init__(*args,**kwargs)
        
        self.fields['s1070_evttabprocesso'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True        
        self.fields['indmatproc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_alteracao, self).save(commit=True, *args, **kwargs)

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
        model = s1070alteracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_alteracao_dadosprocjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_alteracao_dadosprocjud, self).__init__(*args,**kwargs)
        
        self.fields['s1070_alteracao'].widget.attrs['required'] = True        
        self.fields['ufvara'].widget.attrs['required'] = True        
        self.fields['codmunic'].widget.attrs['required'] = True        
        self.fields['idvara'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_alteracao_dadosprocjud, self).save(commit=True, *args, **kwargs)

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
        model = s1070alteracaodadosProcJud
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_alteracao_infosusp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_alteracao_infosusp, self).__init__(*args,**kwargs)
        
        self.fields['s1070_alteracao'].queryset = s1070alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1070_alteracao'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True        
        self.fields['indsusp'].widget.attrs['required'] = True        
        self.fields['dtdecisao'].widget.attrs['required'] = True        
        self.fields['inddeposito'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_alteracao_infosusp, self).save(commit=True, *args, **kwargs)

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
        model = s1070alteracaoinfoSusp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_alteracao_novavalidade, self).__init__(*args,**kwargs)
        
        self.fields['s1070_alteracao'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_alteracao_novavalidade, self).save(commit=True, *args, **kwargs)

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
        model = s1070alteracaonovaValidade
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_exclusao, self).__init__(*args,**kwargs)
        
        self.fields['s1070_evttabprocesso'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_exclusao, self).save(commit=True, *args, **kwargs)

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
        model = s1070exclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_inclusao, self).__init__(*args,**kwargs)
        
        self.fields['s1070_evttabprocesso'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True        
        self.fields['indmatproc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_inclusao, self).save(commit=True, *args, **kwargs)

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
        model = s1070inclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_inclusao_dadosprocjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_inclusao_dadosprocjud, self).__init__(*args,**kwargs)
        
        self.fields['s1070_inclusao'].widget.attrs['required'] = True        
        self.fields['ufvara'].widget.attrs['required'] = True        
        self.fields['codmunic'].widget.attrs['required'] = True        
        self.fields['idvara'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_inclusao_dadosprocjud, self).save(commit=True, *args, **kwargs)

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
        model = s1070inclusaodadosProcJud
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1070_inclusao_infosusp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1070_inclusao_infosusp, self).__init__(*args,**kwargs)
        
        self.fields['s1070_inclusao'].queryset = s1070inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1070_inclusao'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True        
        self.fields['indsusp'].widget.attrs['required'] = True        
        self.fields['dtdecisao'].widget.attrs['required'] = True        
        self.fields['inddeposito'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_inclusao_infosusp, self).save(commit=True, *args, **kwargs)

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
        model = s1070inclusaoinfoSusp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

