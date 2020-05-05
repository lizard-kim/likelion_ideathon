from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Django User Model: 해당 칼럼을 제공해줌
    # username
    # password
    # email
    # first_name
    # last_name

# Django User model과 onoToone으로 연결해준다
# 즉 User model 칼럼에 추가해주고 싶은거 추가하면 됨
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20 )
    user_school = models.CharField(max_length=20)
    user_about = models.TextField(max_length=100)
    user_contact = models.TextField(max_length=200)
    user_image = models.ImageField(upload_to="", null = True, blank = True)# media files 어디에 저장할지 upload to

    def __str__(self):
        return str(str(self.user_id)+ '번 ') + str(self.user_name)