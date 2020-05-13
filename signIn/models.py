from django.db import models
from django.conf import settings
from idea.models import Idea
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)

class MyUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, user_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name
        )


        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, user_name, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            user_name = user_name
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Profile(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=20 , null = True, blank = True)
    user_school = models.CharField(max_length=20, null = True, blank = True)
    user_about = models.TextField(max_length=100, null = True, blank = True)
    user_contact = models.TextField(max_length=200, null = True, blank = True)
    user_image = models.ImageField(upload_to="", null = True, blank = True)# media files 어디에 저장할지 upload to

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name

# Django User Model: 해당 칼럼을 제공해줌
    # username
    # password
    # email
    # first_name
    # last_name

# Django User model과 onoToone으로 연결해준다
# 즉 User model 칼럼에 추가해주고 싶은거 추가하면 됨
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    # related_name을 설정해주면 model.obejects.all() 할때처럼 DB에 접근할때 manager 이름을 지정할 수 있는 것
    # db_column = 내가 FK 어떤 칼럼 지정할껀지 정하는 것
    # user_name = models.CharField(max_length=20 , null = True, blank = True)
    # user_school = models.CharField(max_length=20, null = True, blank = True)
    # user_about = models.TextField(max_length=100, null = True, blank = True)
    # user_contact = models.TextField(max_length=200, null = True, blank = True)
    # user_image = models.ImageField(upload_to="", null = True, blank = True)# media files 어디에 저장할지 upload to

    # def __str__(self):
    #     return str('유저' + str(self.user_id)+ '번 :') + (str(self.id) + '번 프로필')

class Idea_Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return str(user.id) + '번 유저의 카트'

