from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserForm
from .models import Profile, ControlNumber


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            
            ctrl_number = request.POST['control_number']
            password1 = request.POST['password1']
            first_name = request.POST['first_name']
            first_last_name = request.POST['first_last_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            birthday = request.POST['birthday']
            gender = request.POST['gender']
            semester = request.POST['semester']
            username = request.POST['username']

            try:
                u = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                )
                
                profile = Profile.objects.create(user_id=u.id)
                profile.phone=phone
                profile.gender=gender
                profile.first_last_name=first_last_name
                profile.control_number_id=ctrl_number
                profile.birthday=birthday
                profile.semester=semester
                profile.control_number_id=ctrl_number
                profile.save()

                ControlNumber.objects.filter(pk=profile.control_number).update(
                    is_active=True
                )
                
                messages.add_message(request, messages.SUCCESS, 'Cuenta creada correctamente.')
                return redirect('account:register')
            except:
                messages.add_message(request, messages.ERROR, 'Error al crear cuenta, intenta nuevamente.')
                return redirect('account:register')
    else:
        user_form = UserForm()
    
    return render(request, 'account/signup.html', {'form': user_form})
