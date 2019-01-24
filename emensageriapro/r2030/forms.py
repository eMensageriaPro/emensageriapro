# coding: utf-8
from django import forms
from emensageriapro.r2030.models import * 
from emensageriapro.efdreinf.models import r2030evtAssocDespRec 


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




class form_r2030_infoproc(forms.ModelForm):
    vlrnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r2030_infoproc, self).__init__(*args,**kwargs)
        
        self.fields['r2030_recursosrec'].queryset = r2030recursosRec.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2030_recursosrec'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['vlrnret'].widget.attrs['required'] = True
        
    class Meta:
        model = r2030infoProc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r2030_inforecurso(forms.ModelForm):
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r2030_inforecurso, self).__init__(*args,**kwargs)
        
        self.fields['r2030_recursosrec'].queryset = r2030recursosRec.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2030_recursosrec'].widget.attrs['required'] = True        
        self.fields['tprepasse'].widget.attrs['required'] = True        
        self.fields['descrecurso'].widget.attrs['required'] = True        
        self.fields['vlrbruto'].widget.attrs['required'] = True        
        self.fields['vlrretapur'].widget.attrs['required'] = True
        
    class Meta:
        model = r2030infoRecurso
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r2030_recursosrec(forms.ModelForm):
    vlrtotalrec = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r2030_recursosrec, self).__init__(*args,**kwargs)
        
        self.fields['r2030_evtassocdesprec'].queryset = r2030evtAssocDespRec.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2030_evtassocdesprec'].widget.attrs['required'] = True        
        self.fields['cnpjorigrecurso'].widget.attrs['required'] = True        
        self.fields['vlrtotalrec'].widget.attrs['required'] = True        
        self.fields['vlrtotalret'].widget.attrs['required'] = True
        
    class Meta:
        model = r2030recursosRec
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

