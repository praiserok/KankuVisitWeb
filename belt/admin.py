from django.contrib import admin
from . import models


admin.site.register(models.Belt)
# prepopulated_fields = {"slug": ("name",)}
