from django.contrib import admin
from .models import Profile, Idea_Cart
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from . import models
# Register your models here.

#admin.site.register(Profile)
admin.site.register(Idea_Cart)

@admin.register(models.Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'user_name',
        'user_school',
        'user_about',
        'user_contact',
        'user_image',
    )
