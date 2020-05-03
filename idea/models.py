from django.db import models
from datetime import datetime

class Idea (models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 100)
    sub_title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
