from django.contrib import admin

from . import models


@admin.register(models.Call)
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


@admin.register(models.Conditon)
class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    ordering = ('id',)
    search_fields = ('name',)
