
from django.core.handlers import wsgi
import django
import os

import sys

sys.path.append('/home/c/co00847/newsite/public_html/kankuvisit')

sys.path.append('/home/c/co00847/newsite/myenv/lib/python3.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'kankuvisit.settings'


django.setup()


application = wsgi.WSGIHandler()
