from django.contrib import admin

from .models import Harmful

class HarmfulAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'date', 'wordSet', 'created_at')


admin.site.register(Harmful, HarmfulAdmin)
