from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'message')

admin.site.register(Contact, ContactAdmin)
