from django.contrib import admin

from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('months', 'sex', 'feedback', 'created_at')


admin.site.register(Feedback, FeedbackAdmin)
