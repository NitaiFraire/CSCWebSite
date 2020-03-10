from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib import messages
from django.shortcuts import reverse, get_object_or_404, render, redirect
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import FormMixin
# from django.http import FileResponse

from event.models import Detail, Gallery, UserEvent
from event.forms import RegisterUserInEventForm

from jinja2 import Environment, FileSystemLoader

import datetime
import os
import pdfkit


class EventListView(ListView):
    model = Detail
    paginate_by = 6
    template_name = 'event/event_list.html'
    context_object_name = 'events'


# class EventDetailView(DetailView):
#     model = Detail
#     template_name = 'event/event_detail.html'
#     context_object_name = 'event'

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['current_time'] = datetime.date.today()
#         data['gallery'] = Gallery.objects.filter(event_id__slug=self.kwargs['slug']
#                                         ).values('photo1', 'photo2', 'photo3',
#                                                 'photo4', 'photo5', 'photo6',
#                                                 'photo7', 'photo8', 'photo9',
#                                                 'photo10', 'photo11', 'photo12')
#         return data

def event_detail(request, slug):

    event = get_object_or_404(Detail, slug=slug)
    try:
        current_user = get_user_model().objects.get(pk=request.user.id)
        user_id = current_user.id
        already_registered = UserEvent.objects.filter(user_id=user_id, event_id=event.id).exists()
    except:
        already_registered = False

    if request.method == 'POST':
        form = RegisterUserInEventForm(data=request.POST, slug=slug)
        if form.is_valid():

            inscription = form.cleaned_data['inscription']
            one_day = datetime.timedelta(days=1)
            date_limit = event.start_date - one_day

            # parameters for the html template
            data = {
                'date_limit': date_limit,
                'start_date': event.start_date,
                'hour': event.hour,
                'event_description': event.description,
                'user': request.user,
                'total': event.price
            }

            if 'day_0' not in inscription:
                data['total'] = event.price_per_day

            # generate html template
            env = Environment(loader=FileSystemLoader('event/templates/event'))
            template = env.get_template('ticketTemplate.html')
            html = template.render(data)

            # create folder for pdfs
            if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'pdfs/')):
                os.mkdir(os.path.join(settings.MEDIA_ROOT, 'pdfs/'))

            # generate pdf
            options = {
                'margin-top': '0',
                'margin-right': '0',
                'margin-bottom': '0',
                'margin-left': '0',
            }
            pdf_path = os.path.join(settings.MEDIA_ROOT, f"pdfs/{request.user}-{slug}.pdf") 
            pdfkit.from_string(html, pdf_path, options)  

            # send email

            # Develpment
            msg = EmailMessage(f'Registro {event.name}',
                                '',
                                'nfraire07@gmail.com',
                                ['nfraire07@gmail.com'])

            #production

            msg.attach_file(pdf_path, 'application/pdf')

            
            try:
                register = UserEvent.objects.create(user_id=current_user, event_id=event, price=data['total'])
                register.day_assistance = inscription
                register.save()
                msg.send()

                # remove pdf file
                os.remove(pdf_path)

                message = '''Registro exitoso!. Revisa tu bandeja de entrada,
                             se ha enviado un correo con las instrucciones de pago.'''
                messages.add_message(request, messages.SUCCESS, message)
                return redirect('events:detail', slug=slug)
            except:
                messages.add_message(request, messages.ERROR, 'Error la registrar, intenta nuevamente.')
                return redirect('events:detail', slug=slug)
    else:
        form = RegisterUserInEventForm(slug=slug)    

        context = {
            'event': event,
            'form': form,
            'already_registered': already_registered
        }

    return render(request, 'event/event_detail.html', context=context)
