from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/create_account.html'

def logout_view(request):
    logout(request)
    return render(request, 'landing.html')

