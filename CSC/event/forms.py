from django import forms
from event.models import Detail


class RegisterUserInEventForm(forms.Form):

    def __init__(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        obj = Detail.objects.filter(slug=slug).values('days', 'price_per_day', 'offer')
        days = obj[0]['days']
        super().__init__(*args, **kwargs)

        if days > 1:
            price_per_day = obj[0]['price_per_day']
            offer = obj[0]['offer']
            DAYS_CHOICES = [('day_0', f'Acceso completo: ${offer}')]

            for day in range(1, days + 1):
                day = (f'day_{day}', f'Día {day}: ${price_per_day}')
                DAYS_CHOICES.append(day)

            self.fields['inscription'] = forms.ChoiceField(choices=DAYS_CHOICES, label="Insripción")
