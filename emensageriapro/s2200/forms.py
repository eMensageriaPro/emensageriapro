# coding: utf-8
from django import forms
from emensageriapro.s2200.models import * 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialPaises 
from emensageriapro.tabelas.models import eSocialLogradourosTipos 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2200evtAdmissao 


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



class form_s2200_filiacaosindical(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_filiacaosindical,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjsindtrab'].widget.attrs['required'] = True
        self.fields['s2200_evtadmissao'].queryset = s2200evtAdmissao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200filiacaoSindical
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_alvarajudicial(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_alvarajudicial,self ).__init__(*args,**kwargs)
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200alvaraJudicial
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_observacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_observacoes,self ).__init__(*args,**kwargs)
        
        self.fields['observacao'].widget.attrs['required'] = True
        self.fields['s2200_evtadmissao'].queryset = s2200evtAdmissao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200observacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_sucessaovinc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_sucessaovinc,self ).__init__(*args,**kwargs)
        
        self.fields['dttransf'].widget.attrs['required'] = True
        
        self.fields['cnpjempregant'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200sucessaoVinc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_transfdom(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_transfdom,self ).__init__(*args,**kwargs)
        
        self.fields['dttransf'].widget.attrs['required'] = True
        
        self.fields['cpfsubstituido'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200transfDom
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_afastamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_afastamento,self ).__init__(*args,**kwargs)
        
        self.fields['codmotafast'].widget.attrs['required'] = True
        
        self.fields['dtiniafast'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200afastamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_desligamento(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_desligamento,self ).__init__(*args,**kwargs)
        
        self.fields['dtdeslig'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200desligamento
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_cessao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_cessao,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicessao'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200cessao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_infodecjud(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_infodecjud,self ).__init__(*args,**kwargs)
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['s2200_infoestatutario'].widget.attrs['required'] = True

    class Meta:
        model = s2200infoDecJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_documentos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_documentos,self ).__init__(*args,**kwargs)
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200documentos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_ctps(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_ctps,self ).__init__(*args,**kwargs)
        
        self.fields['ufctps'].widget.attrs['required'] = True
        
        self.fields['seriectps'].widget.attrs['required'] = True
        
        self.fields['nrctps'].widget.attrs['required'] = True
        
        self.fields['s2200_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2200CTPS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_ric(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_ric,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrric'].widget.attrs['required'] = True
        
        self.fields['s2200_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2200RIC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_rg(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_rg,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrrg'].widget.attrs['required'] = True
        
        self.fields['s2200_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2200RG
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_rne(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_rne,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nrrne'].widget.attrs['required'] = True
        
        self.fields['s2200_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2200RNE
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_oc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_oc,self ).__init__(*args,**kwargs)
        
        self.fields['orgaoemissor'].widget.attrs['required'] = True
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['s2200_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2200OC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_cnh(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_cnh,self ).__init__(*args,**kwargs)
        
        self.fields['categoriacnh'].widget.attrs['required'] = True
        
        self.fields['dtvalid'].widget.attrs['required'] = True
        
        self.fields['ufcnh'].widget.attrs['required'] = True
        
        self.fields['nrregcnh'].widget.attrs['required'] = True
        
        self.fields['s2200_documentos'].widget.attrs['required'] = True

    class Meta:
        model = s2200CNH
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_brasil(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_brasil,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200brasil
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['paisresid'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200exterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_trabestrangeiro(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_trabestrangeiro,self ).__init__(*args,**kwargs)
        
        self.fields['filhosbr'].widget.attrs['required'] = True
        
        self.fields['casadobr'].widget.attrs['required'] = True
        
        self.fields['classtrabestrang'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200trabEstrangeiro
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_infodeficiencia(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_infodeficiencia,self ).__init__(*args,**kwargs)
        
        self.fields['infocota'].widget.attrs['required'] = True
        
        self.fields['reabreadap'].widget.attrs['required'] = True
        
        self.fields['defintelectual'].widget.attrs['required'] = True
        
        self.fields['defmental'].widget.attrs['required'] = True
        
        self.fields['defauditiva'].widget.attrs['required'] = True
        
        self.fields['defvisual'].widget.attrs['required'] = True
        
        self.fields['deffisica'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200infoDeficiencia
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_dependente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_dependente,self ).__init__(*args,**kwargs)
        
        self.fields['inctrab'].widget.attrs['required'] = True
        
        self.fields['depsf'].widget.attrs['required'] = True
        
        self.fields['depirrf'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        self.fields['s2200_evtadmissao'].queryset = s2200evtAdmissao.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200dependente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_aposentadoria(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_aposentadoria,self ).__init__(*args,**kwargs)
        
        self.fields['trabaposent'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200aposentadoria
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_contato(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_contato,self ).__init__(*args,**kwargs)
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200contato
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_infoceletista(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_infoceletista,self ).__init__(*args,**kwargs)
        
        self.fields['opcfgts'].widget.attrs['required'] = True
        
        self.fields['cnpjsindcategprof'].widget.attrs['required'] = True
        
        self.fields['natatividade'].widget.attrs['required'] = True
        
        self.fields['tpregjor'].widget.attrs['required'] = True
        
        self.fields['indadmissao'].widget.attrs['required'] = True
        
        self.fields['tpadmissao'].widget.attrs['required'] = True
        
        self.fields['dtadm'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200infoCeletista
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_trabtemporario(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_trabtemporario,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['tpinclcontr'].widget.attrs['required'] = True
        
        self.fields['justcontr'].widget.attrs['required'] = True
        
        self.fields['hipleg'].widget.attrs['required'] = True
        
        self.fields['s2200_infoceletista'].widget.attrs['required'] = True

    class Meta:
        model = s2200trabTemporario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_ideestabvinc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_ideestabvinc,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s2200_trabtemporario'].widget.attrs['required'] = True

    class Meta:
        model = s2200ideEstabVinc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_idetrabsubstituido(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_idetrabsubstituido,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrabsubst'].widget.attrs['required'] = True
        self.fields['s2200_trabtemporario'].queryset = s2200trabTemporario.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2200_trabtemporario'].widget.attrs['required'] = True

    class Meta:
        model = s2200ideTrabSubstituido
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_aprend(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_aprend,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s2200_infoceletista'].widget.attrs['required'] = True

    class Meta:
        model = s2200aprend
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_infoestatutario(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_infoestatutario,self ).__init__(*args,**kwargs)
        
        self.fields['dtingsvpub'].widget.attrs['required'] = True
        
        self.fields['dtexercicio'].widget.attrs['required'] = True
        
        self.fields['dtposse'].widget.attrs['required'] = True
        
        self.fields['dtnomeacao'].widget.attrs['required'] = True
        
        self.fields['tpprov'].widget.attrs['required'] = True
        
        self.fields['indprovim'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200infoEstatutario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_localtrabgeral(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_localtrabgeral,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200localTrabGeral
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_localtrabdom(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_localtrabdom,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200localTrabDom
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_horcontratual(forms.ModelForm):
    qtdhrssem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_horcontratual,self ).__init__(*args,**kwargs)
        
        self.fields['tmpparc'].widget.attrs['required'] = True
        
        self.fields['tpjornada'].widget.attrs['required'] = True
        
        self.fields['s2200_evtadmissao'].widget.attrs['required'] = True

    class Meta:
        model = s2200horContratual
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2200_horario(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_horario,self ).__init__(*args,**kwargs)
        
        self.fields['codhorcontrat'].widget.attrs['required'] = True
        
        self.fields['dia'].widget.attrs['required'] = True
        self.fields['s2200_horcontratual'].queryset = s2200horContratual.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2200_horcontratual'].widget.attrs['required'] = True

    class Meta:
        model = s2200horario
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

