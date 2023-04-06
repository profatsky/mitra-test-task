from django.contrib import admin

from . import models


@admin.register(models.Bargain)
class BargainAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'placement_date', 'source')
    search_fields = ('title', 'source')


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'placement_date', 'source')
    search_fields = ('title', 'source')
