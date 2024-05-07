
from django.contrib import admin

from .models import Cohort
from .models import Host
from .models import Event


class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'strength')


class HostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'workplace')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'start', 'duration', 'host', 'cohort')


admin.site.register(Cohort, CohortAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Event, EventAdmin)
