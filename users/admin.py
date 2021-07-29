from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'category'),
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

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
