from django.contrib import admin
from .models import Comment, AddComment
# Register your models here.

admin.site.register(Comment)
admin.site.register(AddComment)