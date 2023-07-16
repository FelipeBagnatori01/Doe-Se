from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .models import Institute
from .models import Post, Follows
from .forms import UploadForm
from django.db import models
from django.contrib.auth import get_user_model
import json

# Create your views here.


@login_required
def show_feed(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'show_feed.html', {'posts':posts})
    elif request.method == "POST":
        return HttpResponse("Resposta ao post")


@login_required
def show_feed_org(request):
    posts = Post.objects.all()
    return render(request, 'show_feed_org.html', {'posts':posts})


@login_required
def create_post(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
        return redirect(show_feed_org)
    return render(request, 'create_post.html', {'form' : UploadForm})

@login_required
def like_postSF(request, post_id):
    Post.objects.filter(pk=post_id).update(likes = Post.objects.get(pk=post_id).likes+1)
    return redirect(show_feed)

@login_required
def like_postSFO(request, post_id):
    Post.objects.filter(pk=post_id).update(likes = Post.objects.get(pk=post_id).likes+1)
    return redirect(show_feed_org)

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
def profile(request, user_id):
    posts = Post.objects.filter(user=get_user_model().objects.get(username=user_id))
    follow = False
    return render(request, 'profile.html', {'posts':posts, 'user_id':user_id, 'follow':follow})

@login_required
def profile_org(request, user_id):
    posts = Post.objects.filter(user=get_user_model().objects.get(username=user_id))
    follow = True
    return render(request, 'profile_org.html', {'posts':posts, 'user_id':user_id, 'follow':follow})

@login_required
def follow(request, user_id):
    # adicionar follow
    return redirect(profile)

@login_required
def follow_org(request, user_id):
    # adicionar follow
    return redirect(profile_org)

@login_required
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
    return redirect(show_feed)

@login_required
def institution_login(request):
    return render(request, 'profile_org.html')

@login_required
def upload(request):
    form = UploadForm(request.POST, request.FILES)
    return render(request, 'make_post.html')

@login_required
def search(request):
    profiles = get_user_model().objects.all()
    return render(request, 'search.html', {'profiles':profiles})

@login_required
def search_org(request):
    profiles = get_user_model().objects.all()
    return render(request, 'search_org.html', {'profiles':profiles})
