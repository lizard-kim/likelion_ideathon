from django.db import models
from signIn.models import Profile
from ideaDetail.models import Comment
from django.contrib.auth.models import User

# Create your models here.

class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea_title = models.CharField(max_length=20 )
    idea_subtitle = models.TextField(max_length=100)
    idea_image = models.ImageField(upload_to="", null = True, blank = True)
    idea_description = models.TextField(max_length=500)
    idea_hashtag = models.TextField(max_length=100)
    # idea_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    idea_likecount = models.IntegerField()

    def __str__(self):
        return str(self.idea_title)

class Image_storage(models.Model):
    idea_title = models.ForeignKey(Idea, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null = True, blank = True)

    def __str__(self):
        return str(self.idea_title)
