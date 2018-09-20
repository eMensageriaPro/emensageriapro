# coding: utf-8
from django import forms
from emensageriapro.s2300.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialPaises 
from emensageriapro.tabelas.models import eSocialLogradourosTipos 
from emensageriapro.esocial.models import s2300evtTSVInicio 


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



class form_s2300_documentos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_documentos,self ).__init__(*args,**kwargs)
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300documentos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_ctps(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_ctps,self ).__init__(*args,**kwargs)
        
        self.fields['ufctps'].widget.attrs['required'] = True
        
        self.fields['seriectps'].widget.attrs['required'] = True
        
        self.fields['nrctps'].widget.attrs['required'] = True
        
        self.fields['s2300_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2300CTPS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_ric(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_ric,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrric'].widget.attrs['required'] = True
        
        self.fields['s2300_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2300RIC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_rg(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_rg,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrrg'].widget.attrs['required'] = True
        
        self.fields['s2300_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2300RG
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_rne(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_rne,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrrne'].widget.attrs['required'] = True
        
        self.fields['s2300_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2300RNE
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_oc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_oc,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['s2300_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2300OC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_cnh(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_cnh,self ).__init__(*args,**kwargs)
        
        self.fields['categoriacnh'].widget.attrs['required'] = True
        
        self.fields['dtvalid'].widget.attrs['required'] = True
        
        self.fields['ufcnh'].widget.attrs['required'] = True
        
        self.fields['nrregcnh'].widget.attrs['required'] = True
        
        self.fields['s2300_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2300CNH
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_brasil(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_brasil,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300brasil
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['paisresid'].widget.attrs['required'] = True
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300exterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_trabestrangeiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_trabestrangeiro,self ).__init__(*args,**kwargs)
        
        self.fields['filhosbr'].widget.attrs['required'] = True
        
        self.fields['casadobr'].widget.attrs['required'] = True
        
        self.fields['classtrabestrang'].widget.attrs['required'] = True
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300trabEstrangeiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_infodeficiencia(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_infodeficiencia,self ).__init__(*args,**kwargs)
        
        self.fields['reabreadap'].widget.attrs['required'] = True
        
        self.fields['defintelectual'].widget.attrs['required'] = True
        
        self.fields['defmental'].widget.attrs['required'] = True
        
        self.fields['defauditiva'].widget.attrs['required'] = True
        
        self.fields['defvisual'].widget.attrs['required'] = True
        
        self.fields['deffisica'].widget.attrs['required'] = True
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300infoDeficiencia
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_dependente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_dependente,self ).__init__(*args,**kwargs)
        
        self.fields['inctrab'].widget.attrs['required'] = True
        
        self.fields['depsf'].widget.attrs['required'] = True
        
        self.fields['depirrf'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        self.fields['s2300_evttsvinicio'].queryset = s2300evtTSVInicio.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300dependente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_contato(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_contato,self ).__init__(*args,**kwargs)
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300contato
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_infocomplementares(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_infocomplementares,self ).__init__(*args,**kwargs)
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300infoComplementares
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_cargofuncao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_cargofuncao,self ).__init__(*args,**kwargs)
        
        self.fields['codcargo'].widget.attrs['required'] = True
        
        self.fields['s2300_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2300cargoFuncao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_remuneracao(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_remuneracao,self ).__init__(*args,**kwargs)
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['s2300_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2300remuneracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_fgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_fgts,self ).__init__(*args,**kwargs)
        
        self.fields['opcfgts'].widget.attrs['required'] = True
        
        self.fields['s2300_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2300fgts
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_infodirigentesindical(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_infodirigentesindical,self ).__init__(*args,**kwargs)
        
        self.fields['categorig'].widget.attrs['required'] = True
        
        self.fields['s2300_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2300infoDirigenteSindical
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_infotrabcedido(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_infotrabcedido,self ).__init__(*args,**kwargs)
        
        self.fields['infonus'].widget.attrs['required'] = True
        
        self.fields['tpregprev'].widget.attrs['required'] = True
        
        self.fields['tpregtrab'].widget.attrs['required'] = True
        
        self.fields['dtadmced'].widget.attrs['required'] = True
        
        self.fields['matricced'].widget.attrs['required'] = True
        
        self.fields['cnpjcednt'].widget.attrs['required'] = True
        
        self.fields['categorig'].widget.attrs['required'] = True
        
        self.fields['s2300_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2300infoTrabCedido
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_infoestagiario(forms.ModelForm):
    vlrbolsa = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_infoestagiario,self ).__init__(*args,**kwargs)
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['dtprevterm'].widget.attrs['required'] = True
        
        self.fields['nivestagio'].widget.attrs['required'] = True
        
        self.fields['natestagio'].widget.attrs['required'] = True
        
        self.fields['s2300_infocomplementares'].widget.attrs['required'] = True

    class Meta:
        model = s2300infoEstagiario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_ageintegracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_ageintegracao,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
        self.fields['cnpjagntinteg'].widget.attrs['required'] = True
        
        self.fields['s2300_infoestagiario'].widget.attrs['required'] = True

    class Meta:
        model = s2300ageIntegracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_supervisorestagio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_supervisorestagio,self ).__init__(*args,**kwargs)
        
        self.fields['nmsuperv'].widget.attrs['required'] = True
        
        self.fields['cpfsupervisor'].widget.attrs['required'] = True
        
        self.fields['s2300_infoestagiario'].widget.attrs['required'] = True

    class Meta:
        model = s2300supervisorEstagio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_afastamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_afastamento,self ).__init__(*args,**kwargs)
        
        self.fields['codmotafast'].widget.attrs['required'] = True
        
        self.fields['dtiniafast'].widget.attrs['required'] = True
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300afastamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2300_termino(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_termino,self ).__init__(*args,**kwargs)
        
        self.fields['dtterm'].widget.attrs['required'] = True
        
        self.fields['s2300_evttsvinicio'].widget.attrs['required'] = True

    class Meta:
        model = s2300termino
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

