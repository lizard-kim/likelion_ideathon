from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    comment_pk = models.AutoField(primary_key = True)
    text = models.CharField(max_length = 200)
    create_data = models.DateTimeField(default = timezone.now) # 생성날짜
    
    def __str__(self):
        return str(self.comment_pk)

class AddComment(models.Model):
    comment_pk = models.ForeignKey(Comment, on_delete=models.CASCADE, default = 1)
    text = models.CharField(max_length = 200, blank = True, null = True)
    create_data = models.DateTimeField(default = timezone.now) # 생성날짜

    def __str__(self):
        return str(self.text)