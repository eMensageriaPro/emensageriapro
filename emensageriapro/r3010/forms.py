# coding: utf-8
from django import forms
from emensageriapro.r3010.models import * 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.efdreinf.models import r3010evtEspDesportivo 


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



class form_r3010_receitaingressos(forms.ModelForm):
    vlrtotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    precoindiv = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_receitaingressos,self ).__init__(*args,**kwargs)
        
        self.fields['vlrtotal'].widget.attrs['required'] = True
        
        self.fields['precoindiv'].widget.attrs['required'] = True
        
        self.fields['qtdeingrdev'].widget.attrs['required'] = True
        
        self.fields['qtdeingrvendidos'].widget.attrs['required'] = True
        
        self.fields['qtdeingrvenda'].widget.attrs['required'] = True
        
        self.fields['descingr'].widget.attrs['required'] = True
        
        self.fields['tpingresso'].widget.attrs['required'] = True
        self.fields['r3010_boletim'].queryset = r3010boletim.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_boletim'].widget.attrs['required'] = True

    class Meta:
        model = r3010receitaIngressos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_r3010_outrasreceitas(forms.ModelForm):
    vlrreceita = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_outrasreceitas,self ).__init__(*args,**kwargs)
        
        self.fields['descreceita'].widget.attrs['required'] = True
        
        self.fields['vlrreceita'].widget.attrs['required'] = True
        
        self.fields['tpreceita'].widget.attrs['required'] = True
        self.fields['r3010_boletim'].queryset = r3010boletim.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_boletim'].widget.attrs['required'] = True

    class Meta:
        model = r3010outrasReceitas
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_r3010_infoproc(forms.ModelForm):
    vlrcpsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_infoproc,self ).__init__(*args,**kwargs)
        
        self.fields['vlrcpsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['r3010_evtespdesportivo'].queryset = r3010evtEspDesportivo.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_evtespdesportivo'].widget.attrs['required'] = True

    class Meta:
        model = r3010infoProc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_r3010_boletim(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_boletim,self ).__init__(*args,**kwargs)
        
        self.fields['qtdenaopagantes'].widget.attrs['required'] = True
        
        self.fields['qtdepagantes'].widget.attrs['required'] = True
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['pracadesportiva'].widget.attrs['required'] = True
        
        self.fields['cnpjmandante'].widget.attrs['required'] = True
        
        self.fields['nomecompeticao'].widget.attrs['required'] = True
        
        self.fields['moddesportiva'].widget.attrs['required'] = True
        
        self.fields['categevento'].widget.attrs['required'] = True
        
        self.fields['tpcompeticao'].widget.attrs['required'] = True
        
        self.fields['nrboletim'].widget.attrs['required'] = True
        self.fields['r3010_evtespdesportivo'].queryset = r3010evtEspDesportivo.objects.using( slug ).filter(excluido=False).all()
        self.fields['r3010_evtespdesportivo'].widget.attrs['required'] = True

    class Meta:
        model = r3010boletim
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

