from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length = 200)
    create_data = models.DateTimeField(default = timezone.now) # 생성날짜

    def __str__(self):
        return str(self.text)