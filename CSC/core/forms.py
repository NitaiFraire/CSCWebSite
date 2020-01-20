from django import forms
from django.forms import ValidationError
from material import Layout
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('created',)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        if not phone.isdigit():
            raise ValidationError("El telefono debe ser únicamente numerico")

        return phone

    layout = Layout('name', 'email', 'phone', 'message')