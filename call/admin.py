from django.contrib import admin

from .models import Call


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = (
        'year',
        'period',
        'start_date',
        'end_date',
        'created_at',
        'updated_at',
    )
    ordering = (
        'year',
        'period',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    search_fields = (
        'year',
        'start_date',
    )
