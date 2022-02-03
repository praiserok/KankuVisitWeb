import os
import sys

sys.path.append('/home/c/co00847/newsite/public_html/taskmanager')
sys.path.append('/home/c/co00847/newsite/myenv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'taskmanager.settings'
import django

django.setup()

from django.core.handlers import wsgi

application = wsgi.WSGIHandler()