# coding: utf-8
from django import forms
from emensageriapro.s2306.models import * 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.esocial.models import s2306evtTSVAltContr 


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




class form_s2306_ageintegracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2306_ageintegracao, self).__init__(*args,**kwargs)
        
        self.fields['s2306_infoestagiario'].widget.attrs['required'] = True        
        self.fields['cnpjagntinteg'].widget.attrs['required'] = True        
        self.fields['nmrazao'].widget.attrs['required'] = True        
        self.fields['dsclograd'].widget.attrs['required'] = True        
        self.fields['nrlograd'].widget.attrs['required'] = True        
        self.fields['cep'].widget.attrs['required'] = True        
        self.fields['uf'].widget.attrs['required'] = True
        
    class Meta:
        model = s2306ageIntegracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2306_cargofuncao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2306_cargofuncao, self).__init__(*args,**kwargs)
        
        self.fields['s2306_evttsvaltcontr'].widget.attrs['required'] = True        
        self.fields['codcargo'].widget.attrs['required'] = True
        
    class Meta:
        model = s2306cargoFuncao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2306_infoestagiario(forms.ModelForm):
    vlrbolsa = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2306_infoestagiario, self).__init__(*args,**kwargs)
        
        self.fields['s2306_evttsvaltcontr'].widget.attrs['required'] = True        
        self.fields['natestagio'].widget.attrs['required'] = True        
        self.fields['nivestagio'].widget.attrs['required'] = True        
        self.fields['dtprevterm'].widget.attrs['required'] = True        
        self.fields['nmrazao'].widget.attrs['required'] = True
        
    class Meta:
        model = s2306infoEstagiario
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2306_infotrabcedido(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2306_infotrabcedido, self).__init__(*args,**kwargs)
        
        self.fields['s2306_evttsvaltcontr'].widget.attrs['required'] = True        
        self.fields['indremuncargo'].widget.attrs['required'] = True
        
    class Meta:
        model = s2306infoTrabCedido
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2306_remuneracao(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2306_remuneracao, self).__init__(*args,**kwargs)
        
        self.fields['s2306_evttsvaltcontr'].widget.attrs['required'] = True        
        self.fields['vrsalfx'].widget.attrs['required'] = True        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
    class Meta:
        model = s2306remuneracao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2306_supervisorestagio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2306_supervisorestagio, self).__init__(*args,**kwargs)
        
        self.fields['s2306_infoestagiario'].widget.attrs['required'] = True        
        self.fields['cpfsupervisor'].widget.attrs['required'] = True        
        self.fields['nmsuperv'].widget.attrs['required'] = True
        
    class Meta:
        model = s2306supervisorEstagio
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

