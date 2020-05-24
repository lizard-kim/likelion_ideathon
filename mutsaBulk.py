import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideathon.settings')
django.setup()

from account.models import Profile