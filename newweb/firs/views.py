from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    print(request)
    return render(request, 'home.html')
def about(request):   #კონტროლერი
    return render(request, 'about.html')

