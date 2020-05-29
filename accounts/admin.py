from django.contrib import admin
from .models import Profile, Idea_Cart
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .forms import UserChangeForm, UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError
from . import models
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password','password1', 'password2','user_name', 'user_school', 'user_about', 'user_contact', 'user_image', 'is_active', 'is_staff')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_name', 'user_school', 'user_about', 'user_contact', 'user_image', 'is_active', 'is_staff')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Profile, UserAdmin)
admin.site.register(Idea_Cart)
