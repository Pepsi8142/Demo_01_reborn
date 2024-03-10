from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('user_name')
            messages.success(request, f'Welcome {user_name}! Your account has been created successfully!')
            return redirect('Food:index')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'Users/register.html', context)
