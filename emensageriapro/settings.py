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
    'rest_framework',

    'emensageriapro.controle_de_acesso',
    'emensageriapro.efdreinf',
    'emensageriapro.esocial',
    'emensageriapro.mensageiro',
    'emensageriapro.tabelas',
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
    'emensageriapro.r5001',
    'emensageriapro.r5011',
    'emensageriapro.r9000',
    'emensageriapro.s1000',
    'emensageriapro.s1005',
    'emensageriapro.s1010',
    'emensageriapro.s1020',
    'emensageriapro.s1030',
    'emensageriapro.s1035',
    'emensageriapro.s1040',
    'emensageriapro.s1050',
    'emensageriapro.s1060',
    # 'emensageriapro.s1065',
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
    'emensageriapro.s5011',
    'emensageriapro.s5012',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


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

#STATIC_ROOT = env('STATIC_ROOT')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configurações de Versão do Aplicativo

VERSAO_EMENSAGERIA = '1.0'
VERSAO_MODELO = "v02_04_02" # apagar
VERSAO_LAYOUT_ESOCIAL = "v02_04_02"
VERSAO_LAYOUT_EFDREINF = "v1_03_02"


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


# Configurações de Certificado

CERT_HOST = env('CERT_HOST')
CERT_PASS = env('CERT_PASS')
CERT_PEM_FILE = env('CERT_PEM_FILE')
KEY_PEM_FILE = env('KEY_PEM_FILE')
CA_CERT_PEM_FILE = env('CA_CERT_PEM_FILE')

LINK_WEBSITE = env('LINK_WEBSITE')
EMAIL_RECUPERACAO_SENHA = env('EMAIL_RECUPERACAO_SENHA')

# Configurações Específicas do eSocial

TP_AMB = env('TP_AMB')
FORCE_PRODUCAO_RESTRITA = env('FORCE_PRODUCAO_RESTRITA')

# Chave para ter acesso a função de enviar e consultar eventos pela URL

PASS_SCRIPT = env('PASS_SCRIPT')

LOGIN_REDIRECT_URL = 'mensageiro/mapa-processamento/eyJpZCI6ICIwIiwgInByaW50IjogIjAifQ==/'