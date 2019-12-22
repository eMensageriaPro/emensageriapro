#coding:utf-8
"""
Django settings for emensageria project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

"""

    eMensageria - Sistema de Gerenciamento de Eventos do eSocial <www.emensageria.com.br>
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

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

import psycopg2
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import environ
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.auth.hashers',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'rest_framework',
    'rest_framework.authtoken',
    # 'django_celery_beat',
    'django_cron',
    'constance',
    'constance.backends.database',

    'emensageriapro.controle_de_acesso',
    'emensageriapro.r1000',
    'emensageriapro.r1070',
    'emensageriapro.r2010',
    'emensageriapro.r2020',
    'emensageriapro.r2030',
    'emensageriapro.r2040',
    'emensageriapro.r2050',
    'emensageriapro.r2060',
    'emensageriapro.r2070',
    'emensageriapro.r2098',
    'emensageriapro.r2099',
    'emensageriapro.r3010',
    'emensageriapro.r4010',
    'emensageriapro.r4020',
    'emensageriapro.r4040',
    'emensageriapro.r4098',
    'emensageriapro.r4099',
    'emensageriapro.r5001',
    'emensageriapro.r5011',
    'emensageriapro.r9000',
    'emensageriapro.r9001',
    'emensageriapro.r9002',
    'emensageriapro.r9011',
    'emensageriapro.r9012',
    'emensageriapro.s1000',
    'emensageriapro.s1005',
    'emensageriapro.s1010',
    'emensageriapro.s1020',
    'emensageriapro.s1030',
    'emensageriapro.s1035',
    'emensageriapro.s1040',
    'emensageriapro.s1050',
    'emensageriapro.s1060',
    #'emensageriapro.s1065',
    'emensageriapro.s1070',
    'emensageriapro.s1080',
    'emensageriapro.s1200',
    'emensageriapro.s1202',
    'emensageriapro.s1207',
    'emensageriapro.s1210',
    'emensageriapro.s1250',
    'emensageriapro.s1260',
    'emensageriapro.s1270',
    'emensageriapro.s1280',
    'emensageriapro.s1295',
    'emensageriapro.s1298',
    'emensageriapro.s1299',
    'emensageriapro.s1300',
    'emensageriapro.s2190',
    'emensageriapro.s2200',
    'emensageriapro.s2205',
    'emensageriapro.s2206',
    'emensageriapro.s2210',
    'emensageriapro.s2220',
    'emensageriapro.s2221',
    'emensageriapro.s2230',
    'emensageriapro.s2231',
    'emensageriapro.s2240',
    'emensageriapro.s2241',
    'emensageriapro.s2245',
    'emensageriapro.s2250',
    'emensageriapro.s2260',
    'emensageriapro.s2298',
    'emensageriapro.s2299',
    'emensageriapro.s2300',
    'emensageriapro.s2306',
    'emensageriapro.s2399',
    'emensageriapro.s2400',
    'emensageriapro.s2405',
    'emensageriapro.s2410',
    'emensageriapro.s2416',
    'emensageriapro.s2420',
    'emensageriapro.s3000',
    'emensageriapro.s5001',
    'emensageriapro.s5002',
    'emensageriapro.s5003',
    'emensageriapro.s5011',
    'emensageriapro.s5012',
    'emensageriapro.s5013',
    'emensageriapro.tabelas',
    'emensageriapro.efdreinf',
    'emensageriapro.esocial',
    'emensageriapro.mensageiro',
    'emensageriapro.mapa_processamento',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'emensageriapro.get_username.RequestMiddleware',
)

CRON_CLASSES = [
    'emensageriapro.cron.EsocialValidate',
    'emensageriapro.cron.EsocialSend',
    'emensageriapro.cron.EsocialConsult',
    'emensageriapro.cron.EfdreinfValidate',
    'emensageriapro.cron.EfdreinfSend',
    'emensageriapro.cron.EfdreinfConsult',
    'emensageriapro.cron.ImportFiles',
]


ROOT_URLCONF = 'emensageriapro.urls'

WSGI_APPLICATION = 'emensageriapro.wsgi.application'


TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
      os.path.join(BASE_DIR, 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'constance.context_processors.config',
        'emensageriapro.context_processors.admin_media',
      ],
    },
  },
]

# Internacionalização

LANGUAGE_CODE = 'pt-BR'

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'

USE_THOUSAND_SEPARATOR = True

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Configurações de Versão do Aplicativo

VERSAO_EMENSAGERIA = '1.5'
VERSAO_LAYOUT_ESOCIAL = 'v02_05_00'
VERSAO_LAYOUT_EFDREINF = 'v1_04_00'

VERSOES_ESOCIAL = [
    'v02_04_02',
    'v02_05_00']

VERSOES_EFDREINF = [
    'v1_03_02',
    'v1_04_00',
    'v2_00_00']

# Hosts permitidos em Produção (obrigatório caso o DEBUG = False)

ALLOWED_HOSTS = [
    'localhost',
    env('ALLOWED_HOSTS'),
]

# Configuração do Banco de Dados


DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

# E-mail Config

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
SERVER_EMAIL = env('SERVER_EMAIL')

ADMINS = [x.split(':') for x in env.list('DJANGO_ADMINS')]

SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

# Endereços login e logout

LINK_WEBSITE = env('LINK_WEBSITE')
LOGIN_REDIRECT_URL = LINK_WEBSITE + 'mapa-processamento/visao-geral/'
LOGOUT_REDIRECT_URL = LINK_WEBSITE

# Static files

STATIC_ROOT = env('STATIC_ROOT') or os.path.join(BASE_DIR, 'static')
STATIC_URL = env('STATIC_URL')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

# Media files

MEDIA_ROOT = env('MEDIA_ROOT') or os.path.join(BASE_DIR, 'media')
MEDIA_URL = env('MEDIA_URL')

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    )
}

CONSTANCE_ADDITIONAL_FIELDS = {
    'choices_tp_amb': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (("1", u"Produção"), ("2", u"Produção Restrita"))
    }],
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {

    'SYSTEM_MANUAL_SHOW_IN_MENU': (False,
        u'Visualiza manual do sistema no menu.',
        bool),

    'SYSTEM_MANUAL_LINK': ('http://',
         u'Link do manual do sistema.',
         str),

    'LOGO_IMAGE_IN_LOGIN': (False,
        u'Visualiza imagem do logotipo na tela de Login.',
        bool),

    'LOGO_IMAGE': ('', 'Logotipo da empresa', 'image_field'),

    'SYSTEM_TOKEN_SCHEDULE': ('9944b09199c62bcf9418ad846dd0123e4bbdfc6ee4b',
         u'Token de autenticação do sistema para acesso aos webservices',
         str),

    'ESOCIAL_VALIDATE_RUN_EVERY_MINS': (10,
        u'Tempo entre validações (em minutos) dos eventos do eSocial.',
        int),

    'ESOCIAL_SEND_RUN_EVERY_MINS': (10,
        u'Tempo entre envios (em minutos) dos eventos do eSocial.',
        int),

    'ESOCIAL_CONSULT_RUN_EVERY_MINS': (10,
        u'Tempo entre consultas (em minutos) dos eventos do eSocial.',
        int),

    'ESOCIAL_LOTE_MIN': (1,
        u'Quantidade do mínima do lote do eSocial.',
        int),

    'ESOCIAL_LOTE_MAX': (60,
        u'Quantidade do máxima do lote do eSocial.',
        int),

    'ESOCIAL_TIMEOUT': (3600,
        u'Timeout do eSocial.',
        int),

    'ESOCIAL_AUTOMATIC_FUNCTIONS_ENABLED': (False,
        u'Envio automático do eSocial.',
        bool),

    'ESOCIAL_CA_CERT_PEM_FILE': ('certificado/webservicesproducaorestritaesocialgovbr.crt',
        u'Caminho completo do Certificado do SERPRO para o eSocial',
        str),

    'ESOCIAL_TP_AMB': (
        '2',
        u'Tipo de ambiente padrão do sistema do eSocial.',
        'choices_tp_amb'),

    'ESOCIAL_FORCE_PRODUCAO_RESTRITA': (True,
        u'Força o sistema para envio pelo ambiente produção restrita do eSocial.',
        bool),

    'ESOCIAL_VERIFICAR_PREDECESSAO_ANTES_ENVIO': (False,
        u'Ativa a função de verificar predecessão antes dos envios dos eventos do eSocial.',
        bool),

    'IMPORT_FILES_RUN_EVERY_MINS': (10,
        u'Tempo de leitura de arquivos importados (em minutos).',
        int),

    'IMPORT_LEN_EVENTS': (10,
        u'Quantidade do lote de arquivos de eventos para importação.',
        int),

    'IMPORT_AUTOMATIC_FUNCTIONS_ENABLED': (False,
        u'Funções de importação automáticas ativadas.',
        bool),

    'EFDREINF_VALIDADE_RUN_EVERY_MINS': (10,
        u'Tempo entre validações (em minutos) dos eventos do EFD-Reinf.',
        int),

    'EFDREINF_SEND_RUN_EVERY_MINS': (10,
        u'Tempo entre envios (em minutos) dos eventos do EFD-Reinf.',
        int),

    'EFDREINF_CONSULT_RUN_EVERY_MINS': (10,
        u'Tempo entre consultas (em minutos) dos eventos do EFD-Reinf.',
        int),

    'EFDREINF_CA_CERT_PEM_FILE': ('certificados/acserproacfv5.crt',
        u'Caminho completo do Certificado do SERPRO para o EFD-Reinf',
        str),

    'EFDREINF_LOTE_MIN': (1,
        u'Quantidade do mínima do lote do EFD-Reinf.',
        int),

    'EFDREINF_LOTE_MAX': (60,
        u'Quantidade do máxima do lote do EFD-Reinf.',
        int),

    'EFDREINF_TIMEOUT': (3600,
        u'Timeout do EFD-Reinf.',
        int),

    'EFDREINF_AUTOMATIC_FUNCTIONS_ENABLED': (False,
        u'Envio automático do EFD-Reinf.',
        bool),

    'EFDREINF_TP_AMB': (
        '2',
        u'Tipo de ambiente padrão do sistema do EFD-Reinf.',
        'choices_tp_amb'),

    'EFDREINF_FORCE_PRODUCAO_RESTRITA': (True,
        u'Força o sistema para envio pelo ambiente produção restrita do EFD-Reinf.',
        bool),

    'EFDREINF_VERIFICAR_PREDECESSAO_ANTES_ENVIO': (False,
        u'Ativa a função de verificar predecessão antes dos envios dos eventos do EFD-Reinf.',
        bool),

    'EMAIL_RECUPERACAO_SENHA': ('emensageria@emensageria.com.br',
        u'E-mail de recuperação de senha.',
        str),

    'EMAIL_RECUPERACAO_SENHA_ASSUNTO': (u'Criação/Recuperação de senha | eMensageria',
        u'Assunto padrão do e-mail de recuperação de senha.',
        unicode),

    'EMAIL_RECUPERACAO_SENHA_MENSAGEM': (u'<p>Prezado %(nome)s,<br>Acesse o sistema pelo link <a href="%(endereco)s">eMensageriaPro</a><br>Utilizando o usuário: <strong>%(usuario)s</strong><br>Senha: <strong>%(senha)s</strong><br>E-mail gerado automaticamente pelo sistema eMensageria</p>',
        u'Mensagem padrão do e-mail de recuperação de senha.',
        unicode),

}


if not DEBUG:

    DJANGO_LOG_DIR = env('DJANGO_LOG_DIR', default='/var/log/django')
    LOG_FILENAME = env('LOG_FILENAME', default='emensageria.log')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }

        },
        'handlers': {
            'applogfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(DJANGO_LOG_DIR, LOG_FILENAME),
                'maxBytes': 1024*1024*15,  # 15MB
                'backupCount': 10,
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['applogfile', 'mail_admins'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['applogfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'APPNAME': {
                'handlers': ['applogfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'messageria': {
                # mail_admins will only accept ERROR and higher
                'handlers': ['applogfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }
