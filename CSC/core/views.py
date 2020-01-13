from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse

from event.models import Gallery
from .forms import ContactForm
from .models import Contact


def index(request):
    gallery = Gallery.objects.filter(name__exact="eventos en general").values(
                                                   'photo1', 'photo2', 'photo3',
                                                   'photo4', 'photo5', 'photo6',
                                                   'photo7', 'photo8', 'photo9',
                                                   'photo10', 'photo11', 'photo12')
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            sendMail = EmailMessage(
                'CSC: Nuevo mensaje de contacto',
                f'De: {name} <{email}>\nTelefono:{phone}\n\nMensaje:\n\n{message}',
                "no-contestar@inbox.mailtrap.io",
                ['fernandezfrairenitai@hotmail.com'],
                reply_to=[email]
            )

            try:
                sendMail.send()
                c = Contact(name=name, email=email, phone=phone, message=message)
                c.save()
                return redirect(reverse('index')+'?ok&#main-header')
            except:
                return redirect(reverse('index')+'?error&#main-header')

    else:
        contact_form = ContactForm()
    
    return render(request, 'core/index.html', {'form': contact_form, 'gallery': gallery})