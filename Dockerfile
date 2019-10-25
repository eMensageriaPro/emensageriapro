# sempre defina uma versao específica
FROM python:2.7-slim-buster

###############################################################################
# DOCKER CONTAINER PTYHON 2.7 - NECTO Systems 15OCT2019
###############################################################################

## Crie uma imagem com nome o "." é o path do Dockerfile.
#$ docker build --build-arg APP_NAME=projetodj -t projetodjango . # inclui o "."
#$ docker run -it -p 0.0.0.0:8080:8080 projetodjango  python manage.py runserver 0.0.0.0:8080

# Para rodar o container ...
#$ docker build -t <image_name> .
#$ docker run -p 0.0.0.0:8080:8080  <image_name>

## limpa objetos não utilizados...  pode gerar lentidao no próximo build
#$ docker image prune
#$ docker system prune

# limpando a casa ... faxina minuciosa
#   - all stopped containers
#   - all networks not used by at least one container
#   - all images without at least one container associated to them
#   - all build cache
#$ docker system prune -a

#para um environment com valor padrão caso setado ARG
#ARG some_variable_name
#ENV env_var_name=$some_variable_name

# ---------------------------------------------------------------------------
# porque nao usar o ALPINE ... ?? veja link abaixo
# https://pythonspeed.com/articles/base-image-python-docker-images/
#----------------------------------------------------------------------------


# set work directory com o nome da APP para manter reutilizável.

ARG APP_NAME
ARG ENVIRONMENT
ARG WORK_DIR

ENV APP_NAME=${APP_NAME}
ENV ENVIRONMENT=${ENVIRONMENT}
ENV REQUIREMENTS_PATH=./requirements
ENV WORK_DIR=/usr/src/app


# copia DIRETORIO de requirements para dentro do workdir
# <requirements> -> /usr/src/app/<minhaapp>/requirements/
COPY ${REQUIREMENTS_PATH} ${WORK_DIR}/requirements/
WORKDIR ${WORK_DIR}

# # psycopg2 deve ser instalado via binary - NAO REMOVER
RUN pip install psycopg2-binary
# # CECL com a linha abaixo é possível instalar o psycopg2 non binary
# # mas image = 443Mb
RUN apt-get clean && apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends


ENV TZ=America/Brasilia
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# REQUIREMENTS
RUN pip install --no-cache-dir -r ${WORK_DIR}/requirements/${ENVIRONMENT}.txt


# copia o projeto pra dentro do workdir
# <minhaapp> -> /usr/src/app/<minhaapp>
COPY ${APP_NAME}/ ${WORK_DIR}

#RUN ls ${WORK_DIR}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=utf-8

# #update pip ... demora - NAO REMOVER
# RUN pip install -U pip setuptools

EXPOSE 8080

#CMD ["uwsgi --ini ${WORK_DIR}/uwsgi/uwsgi.ini"]

#CMD ["python", "${APP_NAME}/manage.py", "runserver", "0.0.0.0:8080"]

# lembrete .. para acessar o bash
# docker exec -it 5dae717c285d /bin/bash

# processos
# docker exec -it $5dae717c285d ls -al /proc

# Docker configuracoes 
#docker inspect --format='{{json .Config}}' $CONTAINER_NAME
