from django.contrib import admin
from django import forms

from finance.models import Total, Entry, Egress

####################################
###########[ VALIDATORS ]###########
####################################

class FinanceAdminForm(forms.ModelForm):

    class Meta:
        model = Egress
        fields = ('amount',)

    def clean_amount(self):
        total = Total.objects.filter(pk=1).values('total')

        if not total:
            raise forms.ValidationError("Cuenta vacia")
        else:
            total = total[0]['total']
            total = float(total)
            egress = self.cleaned_data.get('amount')
            egress = float(egress)

            if total - egress < 0:
                raise forms.ValidationError("La cuenta no puede quedar vacia")

        return egress


####################################
#############[ MODELS ]#############
####################################

class EntryAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'created',)
    fields = ('amount', 'description',)
    readonly_fields = ('created',)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class EgressAdmin(admin.ModelAdmin):
    form = FinanceAdminForm
    list_display = ('amount', 'created',)
    fields = ('amount', 'description',)
    readonly_fields = ('created',)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class TotalAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request):
        return False


admin.site.register(Total, TotalAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Egress, EgressAdmin)