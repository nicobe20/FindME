from operator import index
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InventarioDeBodega
from .models import Tareas
from .forms import InventarioForm, LocalizadorForms
from .forms import TareasForm
import csv






# Create your views here.
#############################################################################
#Home view
def home(request):
   return  render(request, 'paginas/home.html')

####################################################################################################

#Aqui ocurre todo lo que es la gestion de inventario
#part1


def Inventario(request):
    Inventario = InventarioDeBodega.objects.all()
    return render(request,'Inventario/Index.html',{'inventario':Inventario})

def AñadirInventario(request):
    formulario1 = InventarioForm(request.POST or None, request.FILES or None)
    if formulario1.is_valid():
        formulario1.save()
        return redirect('Inventario')
    return render(request,'Inventario/AñadirInventario.html', {'formulario1':formulario1})


#######################################################################################################

#Buscar Paquetes ocurre aqui
def Buscarpaquete(request):
    return render(request,'Inventario/LocateCrate.html')


def LocateAcrate(request):
    formulario2 = LocalizadorForms(request.POST or None, request.FILES or None)
    if formulario2.is_valid():
        formulario2.save()
        return redirect('Buscarp')
    return render(request,'Inventario/Localizador.html', {'formulario2':formulario2})



#################################################################################################


#Part 2 of inventory management

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
   
####################################################################################################

#toda la gestion de tareas ocurre aqui.


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

##########################################################################################################

#Exportar inventario ocurre aqui
def export_to_csv(request):
    inventario_objs =  InventarioDeBodega.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment ; filename=inventario_export.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'columnas','bloque','ContenidosInv'])
    inventario_fields = inventario_objs.values_list('id', 'columnas','bloque','ContenidosInv')
    for inventario in inventario_fields:
        writer.writerow(inventario)
    return response