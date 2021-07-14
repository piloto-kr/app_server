from django.contrib import admin

from .models import Pit

class PitAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'pit_type', 'checklist', 'content', 'checked_at')

admin.site.register(Pit, PitAdmin)