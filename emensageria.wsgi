import os, sys
sys.path.append('/home/municipios/apps_wsgi')
sys.path.append('/home/municipios/apps_wsgi/emensageriapro')
os.environ['PYTHON_EGG_CACHE'] = '/home/municipios/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'emensageriapro.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
