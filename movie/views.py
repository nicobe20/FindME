from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
   return  render(request, 'paginas/home.html')


def about(request):
    return render(request, 'paginas/about.html')

def Findme(request):
    return render(request,'paginas/Findme.html')

def Inventario(request):
    return render(request,'Inventario/Index.html')

def ingresarInventario(request):
    return render(request,'Inventario/Ingresar.html')

def EditarInventario(request):
    return render(request,'Inventario/Editar.html')