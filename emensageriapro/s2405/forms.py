# coding: utf-8
from django import forms
from emensageriapro.s2405.models import * 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialPaises 
from emensageriapro.tabelas.models import eSocialLogradourosTipos 
from emensageriapro.esocial.models import s2405evtCdBenefAlt 


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




class form_s2405_brasil(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2405_brasil, self).__init__(*args,**kwargs)
        
        self.fields['s2405_evtcdbenefalt'].widget.attrs['required'] = True        
        self.fields['tplograd'].widget.attrs['required'] = True        
        self.fields['dsclograd'].widget.attrs['required'] = True        
        self.fields['nrlograd'].widget.attrs['required'] = True        
        self.fields['cep'].widget.attrs['required'] = True        
        self.fields['codmunic'].widget.attrs['required'] = True        
        self.fields['uf'].widget.attrs['required'] = True
        
    class Meta:
        model = s2405brasil
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2405_dependente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2405_dependente, self).__init__(*args,**kwargs)
        
        self.fields['s2405_evtcdbenefalt'].queryset = s2405evtCdBenefAlt.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2405_evtcdbenefalt'].widget.attrs['required'] = True        
        self.fields['tpdep'].widget.attrs['required'] = True        
        self.fields['nmdep'].widget.attrs['required'] = True        
        self.fields['dtnascto'].widget.attrs['required'] = True        
        self.fields['sexodep'].widget.attrs['required'] = True        
        self.fields['depirrf'].widget.attrs['required'] = True        
        self.fields['incfismen'].widget.attrs['required'] = True        
        self.fields['depfinsprev'].widget.attrs['required'] = True
        
    class Meta:
        model = s2405dependente
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s2405_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s2405_exterior, self).__init__(*args,**kwargs)
        
        self.fields['s2405_evtcdbenefalt'].widget.attrs['required'] = True        
        self.fields['paisresid'].widget.attrs['required'] = True        
        self.fields['dsclograd'].widget.attrs['required'] = True        
        self.fields['nrlograd'].widget.attrs['required'] = True        
        self.fields['nmcid'].widget.attrs['required'] = True
        
    class Meta:
        model = s2405exterior
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

