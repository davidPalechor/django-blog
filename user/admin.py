from django.contrib import admin

from .models import PersonUser


@admin.register(PersonUser)
class PersonUserAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = [
        'id',
        'first_name',
        'last_name',
    ]
