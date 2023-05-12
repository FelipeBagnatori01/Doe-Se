from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_feed(request):
    if request.method == "GET":
        return render(request, 'show_feed.html')
    elif request.method == "POST":
        return HttpResponse("Resposta ao post")

def create_post(request):
    return HttpResponse('A')