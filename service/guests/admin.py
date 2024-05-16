
from django.contrib import admin

from .models import Guest
from .models import Teams


class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'cohort')


class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'members')


admin.site.register(Guest, GuestAdmin)
admin.site.register(Teams, TeamsAdmin)
