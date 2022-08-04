from django.contrib import admin
from . import models

admin.site.register(models.School)
admin.site.register(models.Group)
admin.site.register(models.Timetable),
admin.site.register(models.TimetableDays)
