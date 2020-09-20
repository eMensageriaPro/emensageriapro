# Dockerfile by Marcos Roberto
# Variaveis de ambiente iniciais
FROM centos:centos7
LABEL author="marcosroberto1808@gmail.com"

COPY ./compose_setup/files/uwsgi.ini \
requirements.txt /requirements/

# Dependencias basicas do S.O
RUN yum -y install epel-release ; \
yum -y install gcc python-devel postgresql-devel python-pip ; \
pip install --upgrade pip ; \

# Dependencias iniciais da aplicacao
yum install -y fontconfig freetype libX11 libXext libXrender libjpeg libpng openssl xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 
RUN rpm -i https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox-0.12.5-1.centos7.x86_64.rpm

# Ajustar timezone e locales
RUN export TZ="America/Fortaleza" ; \
export LANG="pt_BR.UTF-8" ; \
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone ; \
localedef -i pt_BR -f UTF-8 pt_BR.UTF-8

# Dependencias PYTHON 
RUN pip install --no-cache-dir -r /requirements/requirements.txt ; \
pip install --no-cache-dir uwsgi ; yum clean all

## Iniciar Tudo
WORKDIR /app
CMD ["uwsgi --ini /requirements/uwsgi.ini"]