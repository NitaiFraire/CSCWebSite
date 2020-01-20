from django.contrib import admin
from event.models import Type, Detail, Gallery


class EventDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'hour', 'start_date', 'end_date')
    readonly_fields = ('slug', 'created', 'updated')

class EventTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Type, EventTypeAdmin)
admin.site.register(Detail, EventDetailAdmin)
admin.site.register(Gallery, GalleryAdmin)