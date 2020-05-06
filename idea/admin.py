from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Idea, Image_storage, Comment,AddComment
# Register your models here.

admin.site.register(Idea)
admin.site.register(Image_storage)
admin.site.register(Comment)
admin.site.register(AddComment)
>>>>>>> idea & detail 연결 및 수정
