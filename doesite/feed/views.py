from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User
from .models import Institute

# Create your views here.

@login_required
def show_feed(request):
    if request.method == "GET":
        return render(request, 'show_feed.html')
    elif request.method == "POST":
        return HttpResponse("Resposta ao post")

@login_required
def show_feed_org(request):
    return render(request, 'show_feed_org.html')

@login_required
def create_post(request):
    return render(request, 'create_post.html')

@login_required
def config(request):
    return render(request, 'config.html')

def login(request):
    return render(request, 'login.html')

def login_org(request):
    return render(request, 'login_org.html')

def landing(request):
    return render(request, 'landing.html')

def create_account(request):
    return render(request, 'create_account.html')

def create_institution(request):
    return render(request, 'create_institution.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def profile_org(request):
    return render(request, 'profile_org.html')


def users(request):
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.email = request.POST.get('email')
    new_user.psw = request.POST.get('psw')
    new_user.save()
    return render(request, 'landing.html')

def institutes(request):
    new_institute = Institute()
    new_institute.name = request.POST.get('name')
    new_institute.email = request.POST.get('email')
    new_institute.phone = request.POST.get('phone')
    new_institute.cep = request.POST.get('cep')
    new_institute.uf = request.POST.get('uf')
    new_institute.adress = request.POST.get('adress')
    new_institute.number = request.POST.get('number')
    new_institute.psw = request.POST.get('psw')
    new_institute.description = request.POST.get('description')
    new_institute.save()
    return render(request, 'landing.html')

@login_required    
def user_login(request):
    return render(request, 'profile.html')

@login_required
def institution_login(request):
    return render(request, 'profile_org.html')
