from django.contrib import admin
from django.contrib.auth.models import User
from account.models import ControlNumber, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    readonly_fields = ('control_number', 'phone', 'first_last_name', 'semester', 'gender',
                       'facebook', 'github', 'gitlab', 'instagram', 'birthday',
                       'photo',)

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,]
    fields = ('last_login', 'first_name',
              'last_name', 'email', 'date_joined',)
    readonly_fields = ('last_login', 'first_name',
                       'last_name', 'email', 'date_joined',)


class ControlNumberAdmin(admin.ModelAdmin):
    list_display = ('control_number', 'is_active')
    readonly_fields = ('is_active',)




admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
admin.site.register(ControlNumber, ControlNumberAdmin)
