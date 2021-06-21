from django.contrib import admin

from .models import Utterance

class UtteranceAdmin(admin.ModelAdmin):
    list_display = ('months', 'sex', 'question', 'answer', 'created_at')


admin.site.register(Utterance, UtteranceAdmin)
