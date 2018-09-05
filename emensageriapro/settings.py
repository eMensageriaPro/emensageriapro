#coding:utf-8
"""
Django settings for emensageria project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

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

import psycopg2
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from emensageriapro.versao import versao

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2w0qr9j#u2e=q081@sk)^-t3g9p5+k0+k9-b=yx4*aw!j=dsm$'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

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
    'emensageriapro.s1065',
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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Internacionalização

LANGUAGE_CODE = 'pt-BR'

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'

USE_THOUSAND_SEPARATOR = True

TIME_ZONE = 'Brazil/East'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#STATIC_URL = '/static/'

STATIC_URL = 'http://static.emensageria.com.br/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIR = (
#    os.path.join(BASE_DIR, 'static'),
#)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configurações de Versão do Aplicativo - NÂO ALTERAR

VERSAO_EMENSAGERIA = versao['versao']
VERSAO_MODELO = versao['versao_esocial']

#coding:utf-8


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts permitidos em Produção (obrigatório caso o DEBUG = False)

ALLOWED_HOSTS = [
    'www.emensageria.com.br',
    'www.municipios.adm.br',
]

# Configuração do Banco de Dados



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emensageriapro',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# E-mail Config

EMAIL_HOST = 'smtp.xxx.com.br'
EMAIL_HOST_USER = 'xxxx@xxx.com.br'
EMAIL_HOST_PASSWORD = 'xxxxx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = 'xxx@xxx.com.br'


# Configurações de Certificado

CERT_HOST = 'certificados/xxx.pfx'
CERT_PASS = 'xxx'
CERT_PEM_FILE = 'certificados/cert.pem'
KEY_PEM_FILE = 'certificados/key.pem'
CA_CERT_PEM_FILE = 'certificados/acserproacfv5.crt'

# Configurações Específicas do eSocial

TP_AMB = 2 # 1-Produção; 2-Produção Restrita
FORCE_PRODUCAO_RESTRITA = True

# Chave para ter acesso a função de enviar e consultar eventos pela URL

PASS_SCRIPT = '123456'