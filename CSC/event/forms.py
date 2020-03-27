from django import forms
from event.models import Detail


class RegisterUserInEventForm(forms.Form):

    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        obj = Detail.objects.filter(slug=slug).values('days', 'price_per_day', 'price')
        days = obj[0]['days']
        super().__init__(*args, **kwargs)

        if days > 1:
            price_per_day = obj[0]['price_per_day']
            price = obj[0]['price']
            DAYS_CHOICES = [('day_0', f'Acceso completo: ${price}')]

            for day in range(1, days + 1):
                day = (f'day_{day}', f'Día {day}: ${price_per_day}')
                DAYS_CHOICES.append(day)

            self.fields['inscription'] = forms.ChoiceField(choices=DAYS_CHOICES, label="Insripción")
