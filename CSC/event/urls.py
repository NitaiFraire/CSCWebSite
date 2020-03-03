from django.urls import path
from .views import EventListView, event_detail

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name="list"),
    path('<slug:slug>', event_detail, name="detail")
]
