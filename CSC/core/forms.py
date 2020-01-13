from django import forms
from material import Layout
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created',)

layout = Layout('name', 'email', 'phone', 'message')