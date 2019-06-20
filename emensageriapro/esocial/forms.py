# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.esocial.models import *


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






class form_s1000_evtinfoempregador(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1000_evtinfoempregador, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1000_evtinfoempregador, self).save(commit=True, *args, **kwargs)

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
        model = s1000evtInfoEmpregador
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1005_evttabestab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1005_evttabestab, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1005_evttabestab, self).save(commit=True, *args, **kwargs)

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
        model = s1005evtTabEstab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1010_evttabrubrica(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1010_evttabrubrica, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1010_evttabrubrica, self).save(commit=True, *args, **kwargs)

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
        model = s1010evtTabRubrica
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1020_evttablotacao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1020_evttablotacao, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1020_evttablotacao, self).save(commit=True, *args, **kwargs)

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
        model = s1020evtTabLotacao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1030_evttabcargo(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1030_evttabcargo, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1030_evttabcargo, self).save(commit=True, *args, **kwargs)

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
        model = s1030evtTabCargo
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1035_evttabcarreira(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1035_evttabcarreira, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1035_evttabcarreira, self).save(commit=True, *args, **kwargs)

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
        model = s1035evtTabCarreira
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1040_evttabfuncao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1040_evttabfuncao, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1040_evttabfuncao, self).save(commit=True, *args, **kwargs)

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
        model = s1040evtTabFuncao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1050_evttabhortur(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1050_evttabhortur, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1050_evttabhortur, self).save(commit=True, *args, **kwargs)

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
        model = s1050evtTabHorTur
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1060_evttabambiente(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1060_evttabambiente, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1060_evttabambiente, self).save(commit=True, *args, **kwargs)

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
        model = s1060evtTabAmbiente
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1070_evttabprocesso(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1070_evttabprocesso, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1070_evttabprocesso, self).save(commit=True, *args, **kwargs)

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
        model = s1070evtTabProcesso
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1080_evttaboperport(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1080_evttaboperport, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1080_evttaboperport, self).save(commit=True, *args, **kwargs)

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
        model = s1080evtTabOperPort
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1200_evtremun(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1200_evtremun, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1200_evtremun, self).save(commit=True, *args, **kwargs)

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
        model = s1200evtRemun
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1202_evtrmnrpps(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1202_evtrmnrpps, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1202_evtrmnrpps, self).save(commit=True, *args, **kwargs)

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
        model = s1202evtRmnRPPS
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1207_evtbenprrp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1207_evtbenprrp, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1207_evtbenprrp, self).save(commit=True, *args, **kwargs)

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
        model = s1207evtBenPrRP
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1210_evtpgtos(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1210_evtpgtos, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1210_evtpgtos, self).save(commit=True, *args, **kwargs)

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
        model = s1210evtPgtos
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1250_evtaqprod(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1250_evtaqprod, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1250_evtaqprod, self).save(commit=True, *args, **kwargs)

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
        model = s1250evtAqProd
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1260_evtcomprod(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1260_evtcomprod, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1260_evtcomprod, self).save(commit=True, *args, **kwargs)

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
        model = s1260evtComProd
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1270_evtcontratavnp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1270_evtcontratavnp, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1270_evtcontratavnp, self).save(commit=True, *args, **kwargs)

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
        model = s1270evtContratAvNP
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1280_evtinfocomplper(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1280_evtinfocomplper, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1280_evtinfocomplper, self).save(commit=True, *args, **kwargs)

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
        model = s1280evtInfoComplPer
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1295_evttotconting(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1295_evttotconting, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1295_evttotconting, self).save(commit=True, *args, **kwargs)

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
        model = s1295evtTotConting
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1298_evtreabreevper(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1298_evtreabreevper, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1298_evtreabreevper, self).save(commit=True, *args, **kwargs)

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
        model = s1298evtReabreEvPer
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1299_evtfechaevper(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1299_evtfechaevper, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1299_evtfechaevper, self).save(commit=True, *args, **kwargs)

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
        model = s1299evtFechaEvPer
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s1300_evtcontrsindpatr(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s1300_evtcontrsindpatr, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s1300_evtcontrsindpatr, self).save(commit=True, *args, **kwargs)

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
        model = s1300evtContrSindPatr
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2190_evtadmprelim(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2190_evtadmprelim, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2190_evtadmprelim, self).save(commit=True, *args, **kwargs)

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
        model = s2190evtAdmPrelim
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2200_evtadmissao(forms.ModelForm):

    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s2200_evtadmissao, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2200_evtadmissao, self).save(commit=True, *args, **kwargs)

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
        model = s2200evtAdmissao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2205_evtaltcadastral(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2205_evtaltcadastral, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2205_evtaltcadastral, self).save(commit=True, *args, **kwargs)

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
        model = s2205evtAltCadastral
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2206_evtaltcontratual(forms.ModelForm):

    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s2206_evtaltcontratual, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2206_evtaltcontratual, self).save(commit=True, *args, **kwargs)

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
        model = s2206evtAltContratual
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2210_evtcat(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2210_evtcat, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2210_evtcat, self).save(commit=True, *args, **kwargs)

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
        model = s2210evtCAT
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2220_evtmonit(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2220_evtmonit, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2220_evtmonit, self).save(commit=True, *args, **kwargs)

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
        model = s2220evtMonit
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2221_evttoxic(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2221_evttoxic, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2221_evttoxic, self).save(commit=True, *args, **kwargs)

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
        model = s2221evtToxic
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2230_evtafasttemp(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2230_evtafasttemp, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2230_evtafasttemp, self).save(commit=True, *args, **kwargs)

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
        model = s2230evtAfastTemp
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2231_evtcessao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2231_evtcessao, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2231_evtcessao, self).save(commit=True, *args, **kwargs)

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
        model = s2231evtCessao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2240_evtexprisco(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2240_evtexprisco, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2240_evtexprisco, self).save(commit=True, *args, **kwargs)

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
        model = s2240evtExpRisco
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2241_evtinsapo(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2241_evtinsapo, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2241_evtinsapo, self).save(commit=True, *args, **kwargs)

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
        model = s2241evtInsApo
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2245_evttreicap(forms.ModelForm):

    durtreicap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )

    def __init__(self, *args, **kwargs):
        
        super(form_s2245_evttreicap, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2245_evttreicap, self).save(commit=True, *args, **kwargs)

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
        model = s2245evtTreiCap
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2250_evtavprevio(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2250_evtavprevio, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2250_evtavprevio, self).save(commit=True, *args, **kwargs)

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
        model = s2250evtAvPrevio
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2260_evtconvinterm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2260_evtconvinterm, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2260_evtconvinterm, self).save(commit=True, *args, **kwargs)

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
        model = s2260evtConvInterm
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2298_evtreintegr(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2298_evtreintegr, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2298_evtreintegr, self).save(commit=True, *args, **kwargs)

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
        model = s2298evtReintegr
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2299_evtdeslig(forms.ModelForm):

    percaliment = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    vralim = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s2299_evtdeslig, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2299_evtdeslig, self).save(commit=True, *args, **kwargs)

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
        model = s2299evtDeslig
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2300_evttsvinicio(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2300_evttsvinicio, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2300_evttsvinicio, self).save(commit=True, *args, **kwargs)

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
        model = s2300evtTSVInicio
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2306_evttsvaltcontr(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2306_evttsvaltcontr, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2306_evttsvaltcontr, self).save(commit=True, *args, **kwargs)

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
        model = s2306evtTSVAltContr
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2399_evttsvtermino(forms.ModelForm):

    percaliment = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )
    vralim = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s2399_evttsvtermino, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2399_evttsvtermino, self).save(commit=True, *args, **kwargs)

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
        model = s2399evtTSVTermino
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2400_evtcdbenefin(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2400_evtcdbenefin, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2400_evtcdbenefin, self).save(commit=True, *args, **kwargs)

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
        model = s2400evtCdBenefIn
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2405_evtcdbenefalt(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2405_evtcdbenefalt, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2405_evtcdbenefalt, self).save(commit=True, *args, **kwargs)

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
        model = s2405evtCdBenefAlt
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2410_evtcdbenin(forms.ModelForm):

    vrbeneficio = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self, *args, **kwargs):
        
        super(form_s2410_evtcdbenin, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2410_evtcdbenin, self).save(commit=True, *args, **kwargs)

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
        model = s2410evtCdBenIn
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2416_evtcdbenalt(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2416_evtcdbenalt, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2416_evtcdbenalt, self).save(commit=True, *args, **kwargs)

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
        model = s2416evtCdBenAlt
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s2420_evtcdbenterm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s2420_evtcdbenterm, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s2420_evtcdbenterm, self).save(commit=True, *args, **kwargs)

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
        model = s2420evtCdBenTerm
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s3000_evtexclusao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s3000_evtexclusao, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['readonly'] = True
        self.fields['tpamb'].widget.attrs['disabled'] = True
        self.fields['tpamb'].widget.attrs['required'] = True
        self.fields['procemi'].widget.attrs['readonly'] = True
        self.fields['procemi'].widget.attrs['disabled'] = True
        self.fields['procemi'].widget.attrs['required'] = True
        self.fields['verproc'].widget.attrs['readonly'] = True
        self.fields['verproc'].widget.attrs['required'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s3000_evtexclusao, self).save(commit=True, *args, **kwargs)

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
        model = s3000evtExclusao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s5001_evtbasestrab(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5001_evtbasestrab, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5001_evtbasestrab, self).save(commit=True, *args, **kwargs)

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
        model = s5001evtBasesTrab
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s5002_evtirrfbenef(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5002_evtirrfbenef, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5002_evtirrfbenef, self).save(commit=True, *args, **kwargs)

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
        model = s5002evtIrrfBenef
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s5003_evtbasesfgts(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5003_evtbasesfgts, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5003_evtbasesfgts, self).save(commit=True, *args, **kwargs)

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
        model = s5003evtBasesFGTS
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s5011_evtcs(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5011_evtcs, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5011_evtcs, self).save(commit=True, *args, **kwargs)

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
        model = s5011evtCS
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s5012_evtirrf(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5012_evtirrf, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5012_evtirrf, self).save(commit=True, *args, **kwargs)

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
        model = s5012evtIrrf
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]


class form_s5013_evtfgts(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        
        super(form_s5013_evtfgts, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
        request = None
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
        
        m =  super(form_s5013_evtfgts, self).save(commit=True, *args, **kwargs)

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
        model = s5013evtFGTS
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retornos_eventos'
            'ocorrencias'
            'validacao_precedencia'
            'validacoes'
            'arquivo_original'
            'arquivo' ]