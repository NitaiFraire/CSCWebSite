from django.contrib import admin
from event.models import Type, Detail, Gallery, UserEvent


class EventDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'hour', 'start_date', 'end_date')
    readonly_fields = ('slug', 'created', 'updated')


class EventTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class UserEventAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento','payment_date', 'payment_status', 'assistance')
    list_filter = ('event_id__name',)
    readonly_fields = ('user_id', 'event_id', 'price', 
                        'day_assistance', 'created', 'updated',)

    def evento(self, obj):
        return obj.event_id.name

    def usuario(self, obj):
        return obj.user_id.email


admin.site.register(Type, EventTypeAdmin)
admin.site.register(Detail, EventDetailAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(UserEvent, UserEventAdmin)