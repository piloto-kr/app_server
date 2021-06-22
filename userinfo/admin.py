from django.contrib import admin

from .models import Userinfo

class UserinfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Userinfo._meta.get_fields()]
    list_filter   = ('uuid', 'parentName', 'childName', 'childMonths')


admin.site.register(Userinfo, UserinfoAdmin)
