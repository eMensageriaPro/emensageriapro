#coding:utf-8

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


from emensageriapro.padrao import executar_sql

def atualizar_status_esocial():
    executar_sql("""
      UPDATE public.s1000_evtinfoempregador AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1000_evtinfoempregador SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1000_evtinfoempregador SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1000_evtinfoempregador SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1005_evttabestab AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1005_evttabestab SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1005_evttabestab SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1005_evttabestab SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1010_evttabrubrica AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1010_evttabrubrica SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1010_evttabrubrica SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1010_evttabrubrica SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1020_evttablotacao AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1020_evttablotacao SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1020_evttablotacao SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1020_evttablotacao SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1030_evttabcargo AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1030_evttabcargo SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1030_evttabcargo SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1030_evttabcargo SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1035_evttabcarreira AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1035_evttabcarreira SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1035_evttabcarreira SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1035_evttabcarreira SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1040_evttabfuncao AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1040_evttabfuncao SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1040_evttabfuncao SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1040_evttabfuncao SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1050_evttabhortur AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1050_evttabhortur SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1050_evttabhortur SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1050_evttabhortur SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1060_evttabambiente AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1060_evttabambiente SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1060_evttabambiente SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1060_evttabambiente SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1070_evttabprocesso AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1070_evttabprocesso SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1070_evttabprocesso SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1070_evttabprocesso SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1080_evttaboperport AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1080_evttaboperport SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1080_evttaboperport SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1080_evttaboperport SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1200_evtremun AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1200_evtremun SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1200_evtremun SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1200_evtremun SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1202_evtrmnrpps AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1202_evtrmnrpps SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1202_evtrmnrpps SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1202_evtrmnrpps SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1207_evtbenprrp AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1207_evtbenprrp SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1207_evtbenprrp SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1207_evtbenprrp SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1210_evtpgtos AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1210_evtpgtos SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1210_evtpgtos SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1210_evtpgtos SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1250_evtaqprod AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1250_evtaqprod SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1250_evtaqprod SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1250_evtaqprod SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1260_evtcomprod AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1260_evtcomprod SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1260_evtcomprod SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1260_evtcomprod SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1270_evtcontratavnp AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1270_evtcontratavnp SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1270_evtcontratavnp SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1270_evtcontratavnp SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1280_evtinfocomplper AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1280_evtinfocomplper SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1280_evtinfocomplper SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1280_evtinfocomplper SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1295_evttotconting AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1295_evttotconting SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1295_evttotconting SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1295_evttotconting SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1298_evtreabreevper AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1298_evtreabreevper SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1298_evtreabreevper SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1298_evtreabreevper SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1299_evtfechaevper AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1299_evtfechaevper SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1299_evtfechaevper SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1299_evtfechaevper SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s1300_evtcontrsindpatr AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s1300_evtcontrsindpatr SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s1300_evtcontrsindpatr SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s1300_evtcontrsindpatr SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2190_evtadmprelim AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2190_evtadmprelim SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2190_evtadmprelim SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2190_evtadmprelim SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2200_evtadmissao AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2200_evtadmissao SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2200_evtadmissao SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2200_evtadmissao SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2205_evtaltcadastral AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2205_evtaltcadastral SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2205_evtaltcadastral SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2205_evtaltcadastral SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2206_evtaltcontratual AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2206_evtaltcontratual SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2206_evtaltcontratual SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2206_evtaltcontratual SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2210_evtcat AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2210_evtcat SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2210_evtcat SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2210_evtcat SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2220_evtmonit AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2220_evtmonit SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2220_evtmonit SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2220_evtmonit SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2230_evtafasttemp AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2230_evtafasttemp SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2230_evtafasttemp SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2230_evtafasttemp SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2240_evtexprisco AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2240_evtexprisco SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2240_evtexprisco SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2240_evtexprisco SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2241_evtinsapo AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2241_evtinsapo SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2241_evtinsapo SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2241_evtinsapo SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2250_evtavprevio AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2250_evtavprevio SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2250_evtavprevio SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2250_evtavprevio SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2260_evtconvinterm AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2260_evtconvinterm SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2260_evtconvinterm SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2260_evtconvinterm SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2298_evtreintegr AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2298_evtreintegr SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2298_evtreintegr SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2298_evtreintegr SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2299_evtdeslig AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2299_evtdeslig SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2299_evtdeslig SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2299_evtdeslig SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2300_evttsvinicio AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2300_evttsvinicio SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2300_evttsvinicio SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2300_evttsvinicio SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2306_evttsvaltcontr AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2306_evttsvaltcontr SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2306_evttsvaltcontr SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2306_evttsvaltcontr SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2399_evttsvtermino AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2399_evttsvtermino SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2399_evttsvtermino SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2399_evttsvtermino SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s2400_evtcdbenefin AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s2400_evtcdbenefin SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s2400_evtcdbenefin SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s2400_evtcdbenefin SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
      UPDATE public.s3000_evtexclusao AS a
         SET recepcao_tp_amb=b.recepcao_tp_amb, recepcao_data_hora=b.recepcao_data_hora, recepcao_versao_app=b.recepcao_versao_app, 
             recepcao_protocolo_envio_lote=b.recepcao_protocolo_envio_lote, processamento_codigo_resposta=b.processamento_codigo_resposta, 
             processamento_descricao_resposta=b.processamento_descricao_resposta, processamento_versao_app_processamento=b.processamento_versao_app_processamento, 
             processamento_data_hora=b.processamento_data_hora, recibo_numero=b.recibo_numero, recibo_hash=b.recibo_hash
        FROM public.retornos_eventos AS b WHERE a.retornos_eventos_id = b.id;UPDATE public.s3000_evtexclusao SET status=5 WHERE processamento_codigo_resposta IN (301,401,402,403,404,405,501,502,503,504,505);
      UPDATE public.s3000_evtexclusao SET status=14 WHERE processamento_codigo_resposta IN (201,202);
      UPDATE public.s3000_evtexclusao SET ocorrencias=Null WHERE retornos_eventos_id NOT IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);
    """, False)
    lista_ocorrencias = executar_sql("""SELECT DISTINCT retornos_eventos_id FROM retornos_eventos_ocorrencias 
                                          WHERE retornos_eventos_id IN (SELECT retornos_eventos_id FROM retornos_eventos_ocorrencias);""", True)
    update = ''
    import json
    from django.forms.models import model_to_dict
    #json.dumps(model_to_dict(s1000_evtinfoempregador), indent=4, sort_keys=True, default=str)
    for a in lista_ocorrencias:
        retornos_eventos_id =  a[0]
        from emensageriapro.mensageiro.models import RetornosEventosOcorrencias
        ocorrencias = RetornosEventosOcorrencias.objects.using( 'default' ).filter(excluido = False, retornos_eventos_id=retornos_eventos_id).all()
        lista_ocor = []
        for o in ocorrencias:
            lista_ocor.append(json.dumps(model_to_dict(o), indent=4, sort_keys=True, default=str))
        txt_str = '|'.join(lista_ocor)
        txt_str = txt_str.replace("'", "''")
        c = executar_sql("""
            SELECT tabela
              FROM transmissor_eventos_esocial 
             WHERE retornos_eventos_id=%s;""" % a[0], True)
        if c:
            update += """UPDATE public.%s SET ocorrencias = '%s' 
                          WHERE retornos_eventos_id='%s';""" % (c[0][0], str(txt_str).replace("'", "''"), a[0])

    if update: executar_sql(update, False)


def atualizar_status_efdreinf():
    executar_sql("""
      UPDATE public.r1000_evtinfocontri AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r1000_evtinfocontri SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r1000_evtinfocontri SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r1000_evtinfocontri SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r1070_evttabprocesso AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r1070_evttabprocesso SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r1070_evttabprocesso SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r1070_evttabprocesso SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2010_evtservtom AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2010_evtservtom SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2010_evtservtom SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2010_evtservtom SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2020_evtservprest AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2020_evtservprest SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2020_evtservprest SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2020_evtservprest SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2030_evtassocdesprec AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2030_evtassocdesprec SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2030_evtassocdesprec SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2030_evtassocdesprec SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2040_evtassocdesprep AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2040_evtassocdesprep SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2040_evtassocdesprep SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2040_evtassocdesprep SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2050_evtcomprod AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2050_evtcomprod SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2050_evtcomprod SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2050_evtcomprod SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2060_evtcprb AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2060_evtcprb SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2060_evtcprb SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2060_evtcprb SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2070_evtpgtosdivs AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2070_evtpgtosdivs SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2070_evtpgtosdivs SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2070_evtpgtosdivs SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2098_evtreabreevper AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2098_evtreabreevper SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2098_evtreabreevper SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2098_evtreabreevper SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r2099_evtfechaevper AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r2099_evtfechaevper SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r2099_evtfechaevper SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r2099_evtfechaevper SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
UPDATE public.r3010_evtespdesportivo AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r3010_evtespdesportivo SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r3010_evtespdesportivo SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r3010_evtespdesportivo SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);
--
--
UPDATE public.r9000_evtexclusao AS a
   SET cdretorno=b.cdretorno, descretorno=b.descretorno, dhprocess=b.dhprocess
  FROM public.r5001_evttotal AS b WHERE a.retornos_evttotal_id = b.id;UPDATE public.r9000_evtexclusao SET status=5 WHERE cdretorno IN ('1');
UPDATE public.r9000_evtexclusao SET status=14 WHERE cdretorno IN ('0','2');
UPDATE public.r9000_evtexclusao SET ocorrencias=Null WHERE retornos_evttotal_id NOT IN (SELECT r5001_evttotal_id FROM r5001_regocorrs);

--
UPDATE public.r5001_evttotal SET retornos_evttotal_id=id, retornos_evttotalcontrib_id=Null ;
UPDATE public.r5011_evttotalcontrib SET retornos_evttotal_id=Null, retornos_evttotalcontrib_id=id;


    """, False)

    lista_ocorrencias = executar_sql("""SELECT DISTINCT r5001_evttotal_id FROM public.r5001_regocorrs 
                                              WHERE r5001_evttotal_id IN (SELECT r5001_evttotal_id FROM transmissor_eventos_efdreinf);""",
                                     True)
    update = ''
    import json
    from django.forms.models import model_to_dict
    for a in lista_ocorrencias:
        r5001_evttotal_id = a[0]
        from emensageriapro.r5001.models import r5001regOcorrs
        ocorrencias = r5001regOcorrs.objects.using('default').filter(excluido=False,
                                                                     r5001_evttotal_id=r5001_evttotal_id).all()
        lista_ocor = []
        for o in ocorrencias:
            lista_ocor.append(json.dumps(model_to_dict(o), indent=4, sort_keys=True, default=str))
        txt_str = '|'.join(lista_ocor)
        txt_str = txt_str.replace("'", "''")
        c = executar_sql("""
                SELECT tabela
                  FROM transmissor_eventos_efdreinf
                 WHERE retornos_evttotal_id=%s;""" % r5001_evttotal_id, True)
        if c:
            update += """UPDATE public.%s SET ocorrencias = '%s' 
                              WHERE retornos_evttotal_id='%s';""" % (c[0][0], str(txt_str).replace("'", "''"), a[0])

    if update: executar_sql(update, False)




