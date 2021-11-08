from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Girl)
class GirlAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age']
    list_editable = ['age']
