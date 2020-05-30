from accounts.models import Profile
import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideathon.settings')
django.setup()


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
    instances.append(Profile(email=email, user_name=user_name, user_school=user_school, password=password  user_about="자기소개를 변경해주세요.",  user_contact="연락처를 적어주세요."))

Profile.objects.bulk_create(instances)
