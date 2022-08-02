from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Nicolás Betancur'})
    #return HttpResponse('<h1>Welcome to the Home Page!')