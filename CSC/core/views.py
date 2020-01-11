from django.views.generic import TemplateView
from event.models import Gallery
from django.shortcuts import render

class HomePage(TemplateView):

    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.filter(
                             name__exact="eventos en general").values(
                                                   'photo1', 'photo2', 'photo3',
                                                   'photo4', 'photo5', 'photo6',
                                                   'photo7', 'photo8', 'photo9',
                                                   'photo10', 'photo11', 'photo12')
        return context