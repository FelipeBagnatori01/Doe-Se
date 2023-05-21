from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_feed(request):
    if request.method == "GET":
        return render(request, 'show_feed.html')
    elif request.method == "POST":
        return HttpResponse("Resposta ao post")

def show_feed_org(request):
    return render(request, 'config.html')

def create_post(request):
    return HttpResponse('A')

def config(request):
    return render(request, 'config.html')

def login(request):
    return render(request, 'login.html')

def landing(request):
    return render(request, 'landing.html')

def create_account(request):
    return render(request, 'create_account.html')

def create_institution(request):
    return render(request, 'create_institution.html')