from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('registro/', views.register_user, name="register"),
    path('identificar/',
         auth_views.LoginView.as_view(template_name="account/login.html"),
         name="login"),
    path('salir/',
         auth_views.LogoutView.as_view(), name="logout")
]
