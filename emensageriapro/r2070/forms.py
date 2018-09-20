# coding: utf-8
from django import forms
from emensageriapro.r2070.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import EFDReinfPaises 
from emensageriapro.efdreinf.models import r2070evtPgtosDivs 


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



class form_r2070_inforesidext(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_inforesidext,self ).__init__(*args,**kwargs)
        
        self.fields['indnif'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['paisresid'].widget.attrs['required'] = True
        
        self.fields['r2070_evtpgtosdivs'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoResidExt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_infomolestia(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_infomolestia,self ).__init__(*args,**kwargs)
        
        self.fields['dtlaudo'].widget.attrs['required'] = True
        
        self.fields['r2070_evtpgtosdivs'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoMolestia
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_ideestab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_ideestab,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['r2070_evtpgtosdivs'].queryset = r2070evtPgtosDivs.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_evtpgtosdivs'].widget.attrs['required'] = True

    class Meta:
        model = r2070ideEstab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtoresidbr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtoresidbr,self ).__init__(*args,**kwargs)
        
        self.fields['r2070_ideestab'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoResidBR
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtopf(forms.ModelForm):
    vlrirrf = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrrendtributavel = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtopf,self ).__init__(*args,**kwargs)
        
        self.fields['vlrirrf'].widget.attrs['required'] = True
        
        self.fields['vlrrendtributavel'].widget.attrs['required'] = True
        
        self.fields['inddecterceiro'].widget.attrs['required'] = True
        
        self.fields['indsuspexig'].widget.attrs['required'] = True
        
        self.fields['dtpgto'].widget.attrs['required'] = True
        self.fields['r2070_pgtoresidbr'].queryset = r2070pgtoResidBR.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtoresidbr'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoPF
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_detdeducao(forms.ModelForm):
    vlrdeducao = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_detdeducao,self ).__init__(*args,**kwargs)
        
        self.fields['vlrdeducao'].widget.attrs['required'] = True
        
        self.fields['indtpdeducao'].widget.attrs['required'] = True
        self.fields['r2070_pgtopf'].queryset = r2070pgtoPF.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070detDeducao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_rendisento(forms.ModelForm):
    vlrisento = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_rendisento,self ).__init__(*args,**kwargs)
        
        self.fields['vlrisento'].widget.attrs['required'] = True
        
        self.fields['tpisencao'].widget.attrs['required'] = True
        self.fields['r2070_pgtopf'].queryset = r2070pgtoPF.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070rendIsento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_detcompet(forms.ModelForm):
    vlrrendtributavel = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_detcompet,self ).__init__(*args,**kwargs)
        
        self.fields['vlrrendtributavel'].widget.attrs['required'] = True
        
        self.fields['perrefpagto'].widget.attrs['required'] = True
        
        self.fields['indperreferencia'].widget.attrs['required'] = True
        self.fields['r2070_pgtopf'].queryset = r2070pgtoPF.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070detCompet
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_compjud(forms.ModelForm):
    vlrcompanoant = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcompanocalend = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_compjud,self ).__init__(*args,**kwargs)
        
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070compJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_inforra(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_inforra,self ).__init__(*args,**kwargs)
        self.fields['r2070_pgtopf'].queryset = r2070pgtoPF.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoRRA
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_inforra_despprocjud(forms.ModelForm):
    vlrdespadvogados = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdespcustas = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_inforra_despprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['vlrdespadvogados'].widget.attrs['required'] = True
        
        self.fields['vlrdespcustas'].widget.attrs['required'] = True
        
        self.fields['r2070_inforra'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoRRAdespProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_inforra_ideadvogado(forms.ModelForm):
    vlradvogado = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_inforra_ideadvogado,self ).__init__(*args,**kwargs)
        
        self.fields['vlradvogado'].widget.attrs['required'] = True
        
        self.fields['nrinscadvogado'].widget.attrs['required'] = True
        
        self.fields['tpinscadvogado'].widget.attrs['required'] = True
        self.fields['r2070_inforra_despprocjud'].queryset = r2070infoRRAdespProcJud.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_inforra_despprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoRRAideAdvogado
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_infoprocjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_infoprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['indorigemrecursos'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        self.fields['r2070_pgtopf'].queryset = r2070pgtoPF.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_infoprocjud_despprocjud(forms.ModelForm):
    vlrdespadvogados = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdespcustas = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_infoprocjud_despprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['vlrdespadvogados'].widget.attrs['required'] = True
        
        self.fields['vlrdespcustas'].widget.attrs['required'] = True
        
        self.fields['r2070_infoprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoProcJuddespProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_infoprocjud_ideadvogado(forms.ModelForm):
    vlradvogado = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_infoprocjud_ideadvogado,self ).__init__(*args,**kwargs)
        
        self.fields['vlradvogado'].widget.attrs['required'] = True
        
        self.fields['nrinscadvogado'].widget.attrs['required'] = True
        
        self.fields['tpinscadvogado'].widget.attrs['required'] = True
        self.fields['r2070_infoprocjud_despprocjud'].queryset = r2070infoProcJuddespProcJud.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_infoprocjud_despprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoProcJudideAdvogado
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_infoprocjud_origemrecursos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_infoprocjud_origemrecursos,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjorigemrecursos'].widget.attrs['required'] = True
        
        self.fields['r2070_infoprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070infoProcJudorigemRecursos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_depjudicial(forms.ModelForm):
    vlrdepjudicial = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_depjudicial,self ).__init__(*args,**kwargs)
        
        self.fields['r2070_pgtopf'].widget.attrs['required'] = True

    class Meta:
        model = r2070depJudicial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtopj(forms.ModelForm):
    vlrret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrrendtributavel = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtopj,self ).__init__(*args,**kwargs)
        
        self.fields['vlrret'].widget.attrs['required'] = True
        
        self.fields['vlrrendtributavel'].widget.attrs['required'] = True
        
        self.fields['dtpagto'].widget.attrs['required'] = True
        self.fields['r2070_pgtoresidbr'].queryset = r2070pgtoResidBR.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtoresidbr'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoPJ
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtopj_infoprocjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtopj_infoprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['indorigemrecursos'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        self.fields['r2070_pgtopj'].queryset = r2070pgtoPJ.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopj'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoPJinfoProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtopj_despprocjud(forms.ModelForm):
    vlrdespadvogados = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrdespcustas = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtopj_despprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['vlrdespadvogados'].widget.attrs['required'] = True
        
        self.fields['vlrdespcustas'].widget.attrs['required'] = True
        
        self.fields['r2070_pgtopj_infoprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoPJdespProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtopj_ideadvogado(forms.ModelForm):
    vlradvogado = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtopj_ideadvogado,self ).__init__(*args,**kwargs)
        
        self.fields['vlradvogado'].widget.attrs['required'] = True
        
        self.fields['nrinscadvogado'].widget.attrs['required'] = True
        
        self.fields['tpinscadvogado'].widget.attrs['required'] = True
        self.fields['r2070_pgtopj_despprocjud'].queryset = r2070pgtoPJdespProcJud.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2070_pgtopj_despprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoPJideAdvogado
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtopj_origemrecursos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtopj_origemrecursos,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjorigemrecursos'].widget.attrs['required'] = True
        
        self.fields['r2070_pgtopj_infoprocjud'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoPJorigemRecursos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2070_pgtoresidext(forms.ModelForm):
    vlrret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrpgto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_pgtoresidext,self ).__init__(*args,**kwargs)
        
        self.fields['vlrret'].widget.attrs['required'] = True
        
        self.fields['vlrpgto'].widget.attrs['required'] = True
        
        self.fields['formatributacao'].widget.attrs['required'] = True
        
        self.fields['tprendimento'].widget.attrs['required'] = True
        
        self.fields['dtpagto'].widget.attrs['required'] = True
        
        self.fields['r2070_ideestab'].widget.attrs['required'] = True

    class Meta:
        model = r2070pgtoResidExt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

