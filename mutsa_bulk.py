import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideathon.settings')
django.setup()

from accounts.models import Profile

f = open('../멋사 - Sheet1.csv', 'r', encoding="utf8")
mutsa = []

rdr = csv.reader(f)
for row in rdr:
    email, user_name, user_school, password = row
    tuple = (email, user_name, user_school, password)
    mutsa.append(tuple)
f.close()

instances = []
for (email, user_name, user_school, password) in mutsa:
    instances.append(Profile(email=email, user_name=user_name, user_school=user_school, password=password))

Profile.objects.bulk_create(instances)