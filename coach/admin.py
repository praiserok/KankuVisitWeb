from django.contrib import admin
from . import models


class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


admin.site.register(models.Coach, CoachAdmin)
