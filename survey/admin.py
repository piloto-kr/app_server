from django.contrib import admin

from .models import Survey

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('months', 'sex', 'answer', 'created_at')


admin.site.register(Survey, SurveyAdmin)
