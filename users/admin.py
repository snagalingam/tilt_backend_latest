from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import UserDetail

User = get_user_model()


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'category'),
        }),
    )
    fieldsets = (
        (('User Information'), {'fields': (
            'email',
            'category',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_test',
        )}),
    )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }
    list_display = [
        'email',
        'category',
        'is_active',
        'is_staff',
        'is_superuser',
        'is_test',
    ]
    model = User
    readonly_fields = ('created', 'updated',)
    search_fields = (
        'email',
        'category',
        'is_active',
        'is_staff',
        'is_superuser',
        'is_test',
    )
    ordering = ('email', 'category')


class UserDetailAdmin(admin.ModelAdmin):
    fieldsets = ((('Information'), {'fields': (
        'user',
        'customer',
        'unique_id',
        'preferred_name',
        'program',
        'created',
        'updated',
    )}),)
    list_display = ['user', 'customer']
    model = UserDetail
    readonly_fields = ('created', 'updated',)
    search_fields = ('user', 'customer')
    ordering = ('user', 'customer',)


admin.site.register(User, UserAdmin)
admin.site.register(UserDetail, UserDetailAdmin)
admin.site.unregister(Group)
