from django.contrib import admin
from .models import Idea, Idea_image_storage, Idea_Comments, Idea_AddComments
# Register your models here.

admin.site.register(Idea)
admin.site.register(Idea_image_storage)
admin.site.register(Idea_Comments)
admin.site.register(Idea_AddComments)
