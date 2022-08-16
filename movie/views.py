from django.shortcuts import render
from django.http import HttpResponse
from .models import InventarioDeBodega 




# Create your views here.
def home(request):
   return  render(request, 'paginas/home.html')


def about(request):
    return render(request, 'paginas/about.html')

def Findme(request):
    return render(request,'paginas/Findme.html')

def Inventario(request):
    Inventario = InventarioDeBodega.objects.all()
    return render(request,'Usuarios/user.html',{'inventario':Inventario})

def ingresarInventario(request):
    return render(request,'Inventario/Ingresar.html')

def EditarInventario(request):
    return render(request,'Inventario/Editar.html')

def BuscarPaquete(request):
    return render(request,'Inventario/BuscarPaquete.html')

def Usuario(request):
   return render(request, 'Usuarios/user.html')