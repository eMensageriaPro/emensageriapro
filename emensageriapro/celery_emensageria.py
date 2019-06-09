import os
from celery import Celery
from django.conf import settings

# https://medium.com/luizalabs/executando-processos-em-background-com-django-e-celery-5ade867e1bf3
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.dir') #1

app = Celery('emensageriapro') #2
app.config_from_object('django.conf:settings') #3
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #4