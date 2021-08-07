from django.contrib import admin

from .models import PreferCharacter

class PreferCharacterAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'prefer_character')

admin.site.register(PreferCharacter, PreferCharacterAdmin)
