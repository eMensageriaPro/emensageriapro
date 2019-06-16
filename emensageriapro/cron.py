#coding: utf-8
import datetime


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

"""

from django_cron import CronJobBase, Schedule
from constance import config
from django.urls import reverse
from emensageriapro.settings import LINK_WEBSITE
import requests


class EsocialValidate(CronJobBase):

    RUN_EVERY_MINS = config.ESOCIAL_SEND_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Validação - eSocial'


    def do(self):

        if config.ESOCIAL_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('esocial_validar_api', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'


class EsocialSend(CronJobBase):

    RUN_EVERY_MINS = config.ESOCIAL_SEND_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Envio - eSocial'

    def do(self):

        if config.ESOCIAL_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('esocial_enviar_api', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'


class EsocialConsult(CronJobBase):

    RUN_EVERY_MINS = config.ESOCIAL_CONSULT_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Consulta - eSocial'

    def do(self):

        if config.ESOCIAL_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('esocial_consultar_api', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'


class EfdreinfValidate(CronJobBase):

    RUN_EVERY_MINS = config.EFDREINF_SEND_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Validação - EFD-Reinf'

    def do(self):

        if config.EFDREINF_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('efdreinf_validar_api', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'


class EfdreinfSend(CronJobBase):

    RUN_EVERY_MINS = config.EFDREINF_SEND_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Envio - EFD-Reinf'

    def do(self):

        if config.EFDREINF_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('efdreinf_enviar_api', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'


class EfdreinfConsult(CronJobBase):

    RUN_EVERY_MINS = config.EFDREINF_CONSULT_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Consulta - EFD-Reinf'

    def do(self):

        if config.EFDREINF_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('efdreinf_consultar_api', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'


class ImportFiles(CronJobBase):

    RUN_EVERY_MINS = config.IMPORT_FILES_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = u'Importação de Arquivos'

    def do(self):

        if config.IMPORT_AUTOMATIC_FUNCTIONS_ENABLED:

            token = config.SYSTEM_TOKEN_SCHEDULE
            url = LINK_WEBSITE + reverse('scripts_processar_arquivos', kwargs={'tab': 'json'})[1:]
            return requests.get(url, headers={'Authorization': 'Token %s' % token}).text

        else:

            return u'Envio automático desativado.'