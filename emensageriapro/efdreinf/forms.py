# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.efdreinf.models import *


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






class form_r1000_evtinfocontri(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r1000_evtinfocontri, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r1000_evtinfocontri, self).save(commit=True, *args, **kwargs)

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
        model = r1000evtInfoContri
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r1070_evttabprocesso(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r1070_evttabprocesso, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r1070_evttabprocesso, self).save(commit=True, *args, **kwargs)

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
        model = r1070evtTabProcesso
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2010_evtservtom(forms.ModelForm):

    vlrtotalbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r2010_evtservtom, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2010_evtservtom, self).save(commit=True, *args, **kwargs)

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
        model = r2010evtServTom
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2020_evtservprest(forms.ModelForm):

    vlrtotalbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r2020_evtservprest, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2020_evtservprest, self).save(commit=True, *args, **kwargs)

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
        model = r2020evtServPrest
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2030_evtassocdesprec(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r2030_evtassocdesprec, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2030_evtassocdesprec, self).save(commit=True, *args, **kwargs)

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
        model = r2030evtAssocDespRec
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2040_evtassocdesprep(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r2040_evtassocdesprep, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2040_evtassocdesprep, self).save(commit=True, *args, **kwargs)

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
        model = r2040evtAssocDespRep
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2050_evtcomprod(forms.ModelForm):

    vlrrecbrutatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrratapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrsenarapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrratsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrsenarsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r2050_evtcomprod, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2050_evtcomprod, self).save(commit=True, *args, **kwargs)

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
        model = r2050evtComProd
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2060_evtcprb(forms.ModelForm):

    vlrrecbrutatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpapurtotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcprbsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r2060_evtcprb, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2060_evtcprb, self).save(commit=True, *args, **kwargs)

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
        model = r2060evtCPRB
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2070_evtpgtosdivs(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r2070_evtpgtosdivs, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2070_evtpgtosdivs, self).save(commit=True, *args, **kwargs)

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
        model = r2070evtPgtosDivs
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2098_evtreabreevper(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r2098_evtreabreevper, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2098_evtreabreevper, self).save(commit=True, *args, **kwargs)

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
        model = r2098evtReabreEvPer
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r2099_evtfechaevper(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r2099_evtfechaevper, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r2099_evtfechaevper, self).save(commit=True, *args, **kwargs)

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
        model = r2099evtFechaEvPer
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r3010_evtespdesportivo(forms.ModelForm):

    vlrreceitatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrreceitaclubes = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretparc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_r3010_evtespdesportivo, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r3010_evtespdesportivo, self).save(commit=True, *args, **kwargs)

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
        model = r3010evtEspDesportivo
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r4010_evtretpf(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r4010_evtretpf, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r4010_evtretpf, self).save(commit=True, *args, **kwargs)

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
        model = r4010evtRetPF
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r4020_evtretpj(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r4020_evtretpj, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r4020_evtretpj, self).save(commit=True, *args, **kwargs)

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
        model = r4020evtRetPJ
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r4040_evtbenefnid(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r4040_evtbenefnid, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r4040_evtbenefnid, self).save(commit=True, *args, **kwargs)

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
        model = r4040evtBenefNId
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r4098_evtreab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r4098_evtreab, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r4098_evtreab, self).save(commit=True, *args, **kwargs)

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
        model = r4098evtReab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r4099_evtfech(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r4099_evtfech, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r4099_evtfech, self).save(commit=True, *args, **kwargs)

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
        model = r4099evtFech
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r5001_evttotal(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r5001_evttotal, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5001_evttotal, self).save(commit=True, *args, **kwargs)

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
        model = r5001evtTotal
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r5011_evttotalcontrib(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r5011_evttotalcontrib, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r5011_evttotalcontrib, self).save(commit=True, *args, **kwargs)

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
        model = r5011evtTotalContrib
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r9000_evtexclusao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9000_evtexclusao, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9000_evtexclusao, self).save(commit=True, *args, **kwargs)

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
        model = r9000evtExclusao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_r5001'
            'retornos_r5011'
            'retornos_r9001'
            'retornos_r9002'
            'retornos_r9011'
            'retornos_r9012'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r9001_evttotal(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9001_evttotal, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9001_evttotal, self).save(commit=True, *args, **kwargs)

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
        model = r9001evtTotal
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r9002_evtret(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9002_evtret, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9002_evtret, self).save(commit=True, *args, **kwargs)

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
        model = r9002evtRet
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r9011_evttotalcontrib(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9011_evttotalcontrib, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9011_evttotalcontrib, self).save(commit=True, *args, **kwargs)

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
        model = r9011evtTotalContrib
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]


class form_r9012_evtretcons(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_r9012_evtretcons, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_r9012_evtretcons, self).save(commit=True, *args, **kwargs)

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
        model = r9012evtRetCons
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo'
            'cdretorno'
            'descretorno'
            'dhprocess' ]