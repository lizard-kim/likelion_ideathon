# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Idea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    idea_title = models.CharField(max_length=20, null=True, blank=True)
    idea_subtitle = models.TextField(max_length=100, null=True, blank=True)
    idea_image = models.ImageField(
        upload_to="idea/%Y%m%d", null=True, blank=True)
    idea_description = models.TextField(max_length=500, null=True, blank=True)
    idea_hashtag = models.TextField(max_length=100, null=True, blank=True)
    idea_likecount = models.IntegerField(null=True, blank=True)
    idea_create_data = models.DateTimeField(
        default=timezone.now, null=True, blank=True)  # 생성날짜

    def __str__(self):
        return str(self.id)


class Idea_image_storage(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="idea/%Y%m%d", null=True, blank=True)

    def __str__(self):
        return str(self.idea_id)


class Idea_Comments(models.Model):  # (어떤 유저의 어떤 아이디어에) 다른 유저가 다는 댓글들 저장
    idea = models.ForeignKey(
        Idea, on_delete=models.CASCADE, null=True, blank=True)    # 어떤 유저의 어떤 아이디어에
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)    # 다른 유저가
    text = models.CharField(max_length=200, null=True, blank=True)    # 작성하는 댓글
    create_data = models.DateTimeField(default=timezone.now)  # 생성날짜

    def __str__(self):
        return str(self.id)


# (어떤 유저의 어떤 아이디어에 달린 댓글들에) 다른 유저가 작성하는 대댓글들 저장
class Idea_AddComments(models.Model):
    idea_comments = models.ForeignKey(
        Idea_Comments, on_delete=models.CASCADE, null=True, blank=True)  # 어떤 유저의 어떤 아이디어에 달린 댓글들
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)    # 다른 유저가
    text = models.CharField(max_length=200, blank=True,
                            null=True)    # 작성하는 대댓글
    create_data = models.DateTimeField(default=timezone.now)  # 생성날짜

    def __str__(self):
        return str(self.text)
