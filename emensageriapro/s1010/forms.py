# coding: utf-8
from django import forms
from emensageriapro.s1010.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1010evtTabRubrica 


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



class form_s1010_exclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_exclusao,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        
        self.fields['s1010_evttabrubrica'].widget.attrs['required'] = True

    class Meta:
        model = s1010exclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_alteracao_novavalidade(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_alteracao_novavalidade,self ).__init__(*args,**kwargs)
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['s1010_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1010alteracaonovaValidade
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_alteracao_ideprocessosind(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_alteracao_ideprocessosind,self ).__init__(*args,**kwargs)
        
        self.fields['nrproc'].widget.attrs['required'] = True
        self.fields['s1010_alteracao'].queryset = s1010alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1010alteracaoideProcessoSIND
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_alteracao_ideprocessofgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_alteracao_ideprocessofgts,self ).__init__(*args,**kwargs)
        
        self.fields['nrproc'].widget.attrs['required'] = True
        self.fields['s1010_alteracao'].queryset = s1010alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1010alteracaoideProcessoFGTS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_alteracao_ideprocessoirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_alteracao_ideprocessoirrf,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        self.fields['s1010_alteracao'].queryset = s1010alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1010alteracaoideProcessoIRRF
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_alteracao_ideprocessocp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_alteracao_ideprocessocp,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['extdecisao'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['s1010_alteracao'].queryset = s1010alteracao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_alteracao'].widget.attrs['required'] = True

    class Meta:
        model = s1010alteracaoideProcessoCP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_alteracao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_alteracao,self ).__init__(*args,**kwargs)
        
        self.fields['codincsind'].widget.attrs['required'] = True
        
        self.fields['codincfgts'].widget.attrs['required'] = True
        
        self.fields['codincirrf'].widget.attrs['required'] = True
        
        self.fields['codinccp'].widget.attrs['required'] = True
        
        self.fields['tprubr'].widget.attrs['required'] = True
        
        self.fields['natrubr'].widget.attrs['required'] = True
        
        self.fields['dscrubr'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        
        self.fields['s1010_evttabrubrica'].widget.attrs['required'] = True

    class Meta:
        model = s1010alteracao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_inclusao_ideprocessosind(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_inclusao_ideprocessosind,self ).__init__(*args,**kwargs)
        
        self.fields['nrproc'].widget.attrs['required'] = True
        self.fields['s1010_inclusao'].queryset = s1010inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1010inclusaoideProcessoSIND
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_inclusao_ideprocessofgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_inclusao_ideprocessofgts,self ).__init__(*args,**kwargs)
        
        self.fields['nrproc'].widget.attrs['required'] = True
        self.fields['s1010_inclusao'].queryset = s1010inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1010inclusaoideProcessoFGTS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_inclusao_ideprocessoirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_inclusao_ideprocessoirrf,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        self.fields['s1010_inclusao'].queryset = s1010inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1010inclusaoideProcessoIRRF
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_inclusao_ideprocessocp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_inclusao_ideprocessocp,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['extdecisao'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['s1010_inclusao'].queryset = s1010inclusao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1010_inclusao'].widget.attrs['required'] = True

    class Meta:
        model = s1010inclusaoideProcessoCP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1010_inclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_inclusao,self ).__init__(*args,**kwargs)
        
        self.fields['codincsind'].widget.attrs['required'] = True
        
        self.fields['codincfgts'].widget.attrs['required'] = True
        
        self.fields['codincirrf'].widget.attrs['required'] = True
        
        self.fields['codinccp'].widget.attrs['required'] = True
        
        self.fields['tprubr'].widget.attrs['required'] = True
        
        self.fields['natrubr'].widget.attrs['required'] = True
        
        self.fields['dscrubr'].widget.attrs['required'] = True
        
        self.fields['inivalid'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        
        self.fields['s1010_evttabrubrica'].widget.attrs['required'] = True

    class Meta:
        model = s1010inclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

