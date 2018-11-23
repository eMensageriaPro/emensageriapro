# coding: utf-8
from django import forms
from emensageriapro.s1000.models import * 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialNaturezasJuridicas 
from emensageriapro.esocial.models import s1000evtInfoEmpregador 


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



class form_s1000_inclusao_softwarehouse(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_softwarehouse,self ).__init__(*args,**kwargs)
        
        self.fields['email'].widget.attrs['required'] = True
        
        self.fields['telefone'].widget.attrs['required'] = True
        
        self.fields['nmcont'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjsofthouse'].widget.attrs['required'] = True
        self.fields['s1000_inclusao'].queryset = s1000inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaosoftwareHouse
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_situacaopj(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_situacaopj,self ).__init__(*args,**kwargs)
        
        self.fields['indsitpj'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaosituacaoPJ
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_situacaopf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_situacaopf,self ).__init__(*args,**kwargs)
        
        self.fields['indsitpf'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaosituacaoPF
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_infoorginternacional(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_infoorginternacional,self ).__init__(*args,**kwargs)
        
        self.fields['indacordoisenmulta'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaoinfoOrgInternacional
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_infoop(forms.ModelForm):
    vrtetorem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_infoop,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjefr'].widget.attrs['required'] = True
        
        self.fields['ideefr'].widget.attrs['required'] = True
        
        self.fields['vrtetorem'].widget.attrs['required'] = True
        
        self.fields['poderop'].widget.attrs['required'] = True
        
        self.fields['esferaop'].widget.attrs['required'] = True
        
        self.fields['indugrpps'].widget.attrs['required'] = True
        
        self.fields['nrsiafi'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaoinfoOP
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_infoente(forms.ModelForm):
    vrsubteto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_infoente,self ).__init__(*args,**kwargs)
        
        self.fields['vrsubteto'].widget.attrs['required'] = True
        
        self.fields['subteto'].widget.attrs['required'] = True
        
        self.fields['indrpps'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['nmente'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao_infoop'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaoinfoEnte
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_infoefr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_infoefr,self ).__init__(*args,**kwargs)
        
        self.fields['prevcomp'].widget.attrs['required'] = True
        
        self.fields['indrpps'].widget.attrs['required'] = True
        
        self.fields['cnpjefr'].widget.attrs['required'] = True
        
        self.fields['ideefr'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao_infoop'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaoinfoEFR
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao_dadosisencao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao_dadosisencao,self ).__init__(*args,**kwargs)
        
        self.fields['pagdou'].widget.attrs['required'] = True
        
        self.fields['dtdou'].widget.attrs['required'] = True
        
        self.fields['dtprotrenov'].widget.attrs['required'] = True
        
        self.fields['nrprotrenov'].widget.attrs['required'] = True
        
        self.fields['dtvenccertif'].widget.attrs['required'] = True
        
        self.fields['dtemiscertif'].widget.attrs['required'] = True
        
        self.fields['nrcertif'].widget.attrs['required'] = True
        
        self.fields['ideminlei'].widget.attrs['required'] = True
        
        self.fields['s1000_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusaodadosIsencao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['email'].widget.attrs['required'] = True
        
        self.fields['fonecel'].widget.attrs['required'] = True
        
        self.fields['fonefixo'].widget.attrs['required'] = True
        
        self.fields['cpfctt'].widget.attrs['required'] = True
        
        self.fields['nmctt'].widget.attrs['required'] = True
        
        self.fields['nrregett'].widget.attrs['required'] = True
        
        self.fields['indett'].widget.attrs['required'] = True
        
        self.fields['indented'].widget.attrs['required'] = True
        
        self.fields['indoptregeletron'].widget.attrs['required'] = True
        
        self.fields['indopccp'].widget.attrs['required'] = True
        
        self.fields['inddesfolha'].widget.attrs['required'] = True
        
        self.fields['indconstr'].widget.attrs['required'] = True
        
        self.fields['indcoop'].widget.attrs['required'] = True
        
        self.fields['natjurid'].widget.attrs['required'] = True
        
        self.fields['classtrib'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['fimvalid'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1000_evtinfoempregador'].widget.attrs['required'] = True

    class Meta:
        model = s1000inclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['fimvalid'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1000_evtinfoempregador'].widget.attrs['required'] = True

    class Meta:
        model = s1000exclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_softwarehouse(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_softwarehouse,self ).__init__(*args,**kwargs)
        
        self.fields['email'].widget.attrs['required'] = True
        
        self.fields['telefone'].widget.attrs['required'] = True
        
        self.fields['nmcont'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjsofthouse'].widget.attrs['required'] = True
        self.fields['s1000_alteracao'].queryset = s1000alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaosoftwareHouse
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_situacaopj(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_situacaopj,self ).__init__(*args,**kwargs)
        
        self.fields['indsitpj'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaosituacaoPJ
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_situacaopf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_situacaopf,self ).__init__(*args,**kwargs)
        
        self.fields['indsitpf'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaosituacaoPF
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['fimvalid'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaonovaValidade
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_infoorginternacional(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_infoorginternacional,self ).__init__(*args,**kwargs)
        
        self.fields['indacordoisenmulta'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaoinfoOrgInternacional
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_infoop(forms.ModelForm):
    vrtetorem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_infoop,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjefr'].widget.attrs['required'] = True
        
        self.fields['ideefr'].widget.attrs['required'] = True
        
        self.fields['vrtetorem'].widget.attrs['required'] = True
        
        self.fields['poderop'].widget.attrs['required'] = True
        
        self.fields['esferaop'].widget.attrs['required'] = True
        
        self.fields['indugrpps'].widget.attrs['required'] = True
        
        self.fields['nrsiafi'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaoinfoOP
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_infoente(forms.ModelForm):
    vrsubteto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_infoente,self ).__init__(*args,**kwargs)
        
        self.fields['vrsubteto'].widget.attrs['required'] = True
        
        self.fields['subteto'].widget.attrs['required'] = True
        
        self.fields['indrpps'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['nmente'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao_infoop'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaoinfoEnte
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_infoefr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_infoefr,self ).__init__(*args,**kwargs)
        
        self.fields['prevcomp'].widget.attrs['required'] = True
        
        self.fields['indrpps'].widget.attrs['required'] = True
        
        self.fields['cnpjefr'].widget.attrs['required'] = True
        
        self.fields['ideefr'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao_infoop'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaoinfoEFR
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao_dadosisencao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao_dadosisencao,self ).__init__(*args,**kwargs)
        
        self.fields['pagdou'].widget.attrs['required'] = True
        
        self.fields['dtdou'].widget.attrs['required'] = True
        
        self.fields['dtprotrenov'].widget.attrs['required'] = True
        
        self.fields['nrprotrenov'].widget.attrs['required'] = True
        
        self.fields['dtvenccertif'].widget.attrs['required'] = True
        
        self.fields['dtemiscertif'].widget.attrs['required'] = True
        
        self.fields['nrcertif'].widget.attrs['required'] = True
        
        self.fields['ideminlei'].widget.attrs['required'] = True
        
        self.fields['s1000_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracaodadosIsencao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1000_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['email'].widget.attrs['required'] = True
        
        self.fields['fonecel'].widget.attrs['required'] = True
        
        self.fields['fonefixo'].widget.attrs['required'] = True
        
        self.fields['cpfctt'].widget.attrs['required'] = True
        
        self.fields['nmctt'].widget.attrs['required'] = True
        
        self.fields['nrregett'].widget.attrs['required'] = True
        
        self.fields['indett'].widget.attrs['required'] = True
        
        self.fields['indented'].widget.attrs['required'] = True
        
        self.fields['indoptregeletron'].widget.attrs['required'] = True
        
        self.fields['indopccp'].widget.attrs['required'] = True
        
        self.fields['inddesfolha'].widget.attrs['required'] = True
        
        self.fields['indconstr'].widget.attrs['required'] = True
        
        self.fields['indcoop'].widget.attrs['required'] = True
        
        self.fields['natjurid'].widget.attrs['required'] = True
        
        self.fields['classtrib'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['fimvalid'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1000_evtinfoempregador'].widget.attrs['required'] = True

    class Meta:
        model = s1000alteracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

