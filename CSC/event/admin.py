from django.contrib import admin
from .models import EventType, EventDetail, Gallery


class EventDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'hour', 'start_date', 'end_date')
    readonly_fields = ('slug', 'created', 'updated')

class EventTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(EventType, EventTypeAdmin)
admin.site.register(EventDetail, EventDetailAdmin)
admin.site.register(Gallery, GalleryAdmin)