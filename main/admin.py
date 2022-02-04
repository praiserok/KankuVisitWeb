from django.contrib import admin
from . import models

admin.site.register(models.Task)
admin.site.register(models.Coach)
admin.site.register(models.School)
admin.site.register(models.Group)
admin.site.register(models.Timetable)
admin.site.register(models.Sportsman)