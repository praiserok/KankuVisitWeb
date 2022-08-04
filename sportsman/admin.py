from django.contrib import admin
from . import models


class SportsmanAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'coach', 'is_active')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'coach')
    list_editable = ('is_active',)
    list_filter = ('coach', 'is_active',)
    prepopulated_fields = {
        'slug': ('first_name', 'last_name', 'surname')}


admin.site.register(models.Sportsman, SportsmanAdmin)
