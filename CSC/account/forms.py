from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from material import Layout, Row
from .models import Profile, ControlNumber


class UserForm(UserCreationForm):

    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]

    SEMESTER_CHOICES = [
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        ('6', 'Sexto'),
        ('7', 'Séptimo'),
        ('8', 'Octavo'),
        ('9', 'Noveno'),
        ('10', 'Décimo'),
        ('11', 'Onceavo'),
        ('12', 'Doceavo'),
    ]

    first_name = forms.CharField(max_length=30, label="Nombre(s)")
    control_number = forms.CharField(max_length=10, label="Número de control")
    first_last_name = forms.CharField(max_length=20, label="Apellido paterno")
    last_name = forms.CharField(max_length=20, label="Apellido materno")
    phone = forms.CharField(max_length=10, label="Telefono")
    semester = forms.ChoiceField(choices=SEMESTER_CHOICES, label="Semestre")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Género")
    birthday = forms.DateField(label="Fecha de nacimiento",
                               input_formats=('%Y-%m-%d',))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo ya esta registrado, prueba con otro.")

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone.isnumeric() == False:
            raise ValidationError("El telefono debe ser únicamente numerico")

    def clean_control_number(self):
        ctrl_number = self.cleaned_data.get('control_number')

        if (
            ControlNumber.objects.filter(pk=ctrl_number     # not exists
                                ).exists() == False     
        ):
            raise ValidationError("Número de control invalido")


        if (
            ControlNumber.objects.filter(pk=ctrl_number
                                ).filter(is_active=True     # exists and is_active
                                ).exists() 
                
        ):
            raise ValidationError("Número de control invalido") 

        return ctrl_number


    layout = Layout(Row('first_name', 'first_last_name', 'last_name'),
                    'control_number', 'email',
                    Row('password1', 'password2'),
                    'phone',
                    'birthday', 
                    'gender', 'semester',)