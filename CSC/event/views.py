from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import reverse, get_object_or_404, render
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import FormMixin
# from django.http import FileResponse

from event.models import Detail, Gallery
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

    if request.method == 'POST':
        form = RegisterUserInEventForm(data=request.POST, slug=slug)
        if form.is_valid():

            inscription = form.cleaned_data['inscription']

            one_day = datetime.timedelta(days=1)
            date_limit = event.start_date - one_day

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

            env = Environment(loader=FileSystemLoader('event/templates/event'))
            template = env.get_template('ticketTemplate.html')
            html = template.render(data)

            if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'pdfs/')):
                os.mkdir(os.path.join(settings.MEDIA_ROOT, 'pdfs/'))

            options = {
                'margin-top': '0',
                'margin-right': '0',
                'margin-bottom': '0',
                'margin-left': '0',
            }

            pdfkit.from_string(html, os.path.join(
                                        settings.MEDIA_ROOT,
                                        f"pdfs/{request.user}-{event.slug}.pdf"),
                                        options=options)  

            msg = EmailMessage(f'Registro {event.name}',
                                '',
                                'nfraire07@gmail.com',
                                ['nfraire07@gmail.com'])

            pdf = os.path.join(settings.MEDIA_ROOT,
                              f"pdfs/{request.user}-{event.slug}.pdf")

            msg.attach_file(pdf, 'application/pdf')

            try:
                msg.send()
                os.remove(os.path.join(settings.MEDIA_ROOT,
                                       f"pdfs/{request.user}-{event.slug}.pdf"))
                print("sent")
            except:
                print("error")

            # buffer = io.BytesIO()
            # p = canvas.Canvas(buffer)
            # p.drawInlineImage(image, 150, 650, 150, 150)
            # p.drawString(100, 100, 'Hellow')
            # p.showPage()
            # p.save()
            # buffer.seek(0)
            # return FileResponse(pdf, as_attachment=True, filename='hellow.pdf')

    else:
        form = RegisterUserInEventForm(slug=slug)    

    context = {
        'event': event,
        'form': form
    }
    
    return render(request, 'event/event_detail.html', context=context)
