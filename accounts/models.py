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

# 현재 접속한 유저가 @다른 사람이 등록한 @아이디어를 @저장
class Idea_Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, null = True, blank = True)
    add_cart = models.NullBooleanField()

    def __str__(self):
        return str(self.id)

