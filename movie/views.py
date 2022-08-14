from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Nicolás Betancur Ochoa'})
    #return HttpResponse('<h1>Welcome to the Home Page!')
def about(request):
    return render(request, 'about.html',{'name':'Nicolás Betancur Ochoa'})