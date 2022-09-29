from operator import index
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InventarioDeBodega
from .models import Tareas
from .forms import InventarioForm
from .forms import TareasForm






# Create your views here.
def home(request):
   return  render(request, 'paginas/home.html')


def about(request):
    return render(request, 'paginas/about.html')

def Findme(request):
    return render(request,'paginas/Findme.html')



def Inventario(request):
    Inventario = InventarioDeBodega.objects.all()
    return render(request,'Inventario/Index.html',{'inventario':Inventario})

def AñadirInventario(request):
    formulario1 = InventarioForm(request.POST or None, request.FILES or None)
    if formulario1.is_valid():
        formulario1.save()
        return redirect('Inventario')
    return render(request,'Inventario/AñadirInventario.html', {'formulario1':formulario1})

def editar(request,id):
    inventario = InventarioDeBodega.objects.get(id=id)
    formulario1 = InventarioForm(request.POST or None, request.FILES or None, instance=inventario)
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('Inventario')
    return render(request,'Inventario/EditarInventario.html',{'formulario1':formulario1})
    
def eliminarInventario(request,id): 
   inventario = InventarioDeBodega.objects.get(id=id)
   inventario.delete()
   return redirect('Inventario')
   


def BuscarPaquete(request):
    return render(request,'Inventario/BuscarPaquete.html')


def TareasInv(request):
    tareas = Tareas.objects.all()
    return render(request,'Tasks/TareasInv.html',{'tareas':tareas})
    


def eliminarTareas(request,id):
    tareas = Tareas.objects.get(id=id)
    tareas.delete()
    return redirect('Tareas')

def Añadirtareas(request):
    formulario = TareasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Tareas')
    return render(request,'Tasks/CrearTarea.html', {'formulario':formulario})

def editartareas(request,id):
    tareas = Tareas.objects.get(id=id)
    formulario = TareasForm(request.POST or None, request.FILES or None, instance=tareas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Tareas')
    return render(request,'Tasks/EditarTarea.html',{'formulario':formulario})
