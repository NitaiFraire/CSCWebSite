from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('eventos/', include('event.urls', namespace="events")),
]
