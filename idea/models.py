from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import User
from django.utils import timezone

class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_school = models.CharField(max_length = 50, null=True)
    idea_title = models.CharField(max_length=20, null=True)
    idea_subtitle = models.TextField(max_length=100, null=True)
    idea_image = models.ImageField(upload_to="", null = True, blank = True, default = ".png")
    idea_description = models.TextField(max_length=500, null=True)
    idea_hashtag = models.TextField(max_length=100, null=True)
    idea_likecount = models.IntegerField(null = True, blank = True)
    idea_create_date = models.DateTimeField(default = timezone.now, null = True, blank = True) # 생성날짜

    def __str__(self):
        return self.idea_title

class Image_storage(models.Model):
    idea_title = models.ForeignKey(Idea, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null = True, blank = True)

    def __str__(self):
        return self.idea_title

class Comment(models.Model):
    # user = models.ManyToManyField(User)
    comments = models.ForeignKey(Idea, on_delete = models.CASCADE, null = True, related_name = "comments")
    text = models.CharField(max_length = 200, null=True)
    create_date = models.DateTimeField(default = timezone.now) # 생성날짜

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.text

class AddComment(models.Model):
    comments_pk = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length = 200, blank = True, null = True)
    create_date = models.DateTimeField(default = timezone.now) # 생성날짜

    def __str__(self):
        return self.text
>>>>>>> idea & detail 연결 및 수정
