# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.s1005.models import * 
from emensageriapro.esocial.models import s1005evtTabEstab 


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




class form_s1005_alteracao(forms.ModelForm):
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao, self).__init__(*args,**kwargs)
        
        self.fields['s1005_evttabestab'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True        
        self.fields['cnaeprep'].widget.attrs['required'] = True        
        self.fields['aliqrat'].widget.attrs['required'] = True        
        self.fields['regpt'].widget.attrs['required'] = True        
        self.fields['contapr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_infocaepf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_infocaepf, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['tpcaepf'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_infocaepf, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaoinfoCaepf
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_infoenteduc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_infoenteduc, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].queryset = s1005alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_infoenteduc, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaoinfoEntEduc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_infoobra(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_infoobra, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['indsubstpatrobra'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_infoobra, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaoinfoObra
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_infopcd(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_infopcd, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['contpcd'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_infopcd, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaoinfoPCD
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_novavalidade, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_novavalidade, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaonovaValidade
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_procadmjudfap(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_procadmjudfap, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_procadmjudfap, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaoprocAdmJudFap
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_alteracao_procadmjudrat(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_alteracao_procadmjudrat, self).__init__(*args,**kwargs)
        
        self.fields['s1005_alteracao'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_alteracao_procadmjudrat, self).save(commit=True, *args, **kwargs)

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
        model = s1005alteracaoprocAdmJudRat
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_exclusao, self).__init__(*args,**kwargs)
        
        self.fields['s1005_evttabestab'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_exclusao, self).save(commit=True, *args, **kwargs)

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
        model = s1005exclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao(forms.ModelForm):
    fap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    aliqratajust = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao, self).__init__(*args,**kwargs)
        
        self.fields['s1005_evttabestab'].widget.attrs['required'] = True        
        self.fields['tpinsc'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True        
        self.fields['inivalid'].widget.attrs['required'] = True        
        self.fields['cnaeprep'].widget.attrs['required'] = True        
        self.fields['aliqrat'].widget.attrs['required'] = True        
        self.fields['regpt'].widget.attrs['required'] = True        
        self.fields['contapr'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao_infocaepf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao_infocaepf, self).__init__(*args,**kwargs)
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True        
        self.fields['tpcaepf'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao_infocaepf, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusaoinfoCaepf
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao_infoenteduc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao_infoenteduc, self).__init__(*args,**kwargs)
        
        self.fields['s1005_inclusao'].queryset = s1005inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1005_inclusao'].widget.attrs['required'] = True        
        self.fields['nrinsc'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao_infoenteduc, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusaoinfoEntEduc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao_infoobra(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao_infoobra, self).__init__(*args,**kwargs)
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True        
        self.fields['indsubstpatrobra'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao_infoobra, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusaoinfoObra
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao_infopcd(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao_infopcd, self).__init__(*args,**kwargs)
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True        
        self.fields['contpcd'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao_infopcd, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusaoinfoPCD
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao_procadmjudfap(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao_procadmjudfap, self).__init__(*args,**kwargs)
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao_procadmjudfap, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusaoprocAdmJudFap
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1005_inclusao_procadmjudrat(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1005_inclusao_procadmjudrat, self).__init__(*args,**kwargs)
        
        self.fields['s1005_inclusao'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_inclusao_procadmjudrat, self).save(commit=True, *args, **kwargs)

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
        model = s1005inclusaoprocAdmJudRat
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

