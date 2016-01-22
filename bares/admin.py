from django.contrib import admin
from .models import *

class BarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Bar, BarAdmin)
admin.site.register(Tapa)
