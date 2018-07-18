from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm

from .forms import UserChangeForm
from .forms import SignupForm
from .models import PersonUser

@admin.register(PersonUser)
class PersonUserAdmin(UserAdmin):
    add_form = SignupForm
    change_password_form = AdminPasswordChangeForm
    empty_value_display = '-empty-'
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('id_type', 'id', 'password', 'last_login')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_type', 'id', 'password', 'confirm_password')
        }),
    )
    limited_fieldsets = (
        (None, {'fields': ('id')})
    )
    list_display = [
        'id',
        'first_name',
        'last_name',
        'is_active',
    ]
    ordering = (
        'id',
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'last_login',
    )
