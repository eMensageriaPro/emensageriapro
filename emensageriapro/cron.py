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


class EsocialSend(CronJobBase):

    RUN_EVERY_MINS = config.ESOCIAL_SEND_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'emensageriapro.esocial_send'

    def do(self):
        pass


class EsocialConsult(CronJobBase):

    RUN_EVERY_MINS = config.ESOCIAL_CONSULT_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'emensageriapro.esocial_consult'

    def do(self):
        pass


class EfdreinfSend(CronJobBase):

    RUN_EVERY_MINS = config.EFDREINF_SEND_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'emensageriapro.efdfreinf_send'

    def do(self):
        pass


class EfdreinfConsult(CronJobBase):

    RUN_EVERY_MINS = config.EFDREINF_CONSULT_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'emensageriapro.efdreinf_consult'

    def do(self):
        pass


class ImportFiles(CronJobBase):

    RUN_EVERY_MINS = config.IMPORT_FILES_RUN_EVERY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'emensageriapro.import_files'

    def do(self):
        pass