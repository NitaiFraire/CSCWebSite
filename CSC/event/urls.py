from django.urls import path
from .views import EventListView, EventDetailView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name="list"),
    path('<slug:slug>' , EventDetailView.as_view(), name="detail")
]
