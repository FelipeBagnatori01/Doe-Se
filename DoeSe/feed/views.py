from django.shortcuts import render

# Create your views here.
def feedList(request):
    return render(request, 'frontEnd/test.html')