from django.views.generic import (ListView, DetailView)
from event.models import Detail, Gallery

import datetime

class EventListView(ListView):
    model = Detail
    paginate_by = 6
    template_name = 'event/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Detail
    template_name = 'event/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['current_time'] = datetime.date.today()
        data['gallery'] = Gallery.objects.filter(event_id__slug=self.kwargs['slug']
                                        ).values('photo1', 'photo2', 'photo3',
                                                'photo4', 'photo5', 'photo6',
                                                'photo7', 'photo8', 'photo9',
                                                'photo10', 'photo11', 'photo12')
        return data
    