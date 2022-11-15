import csv
from operator import index
from django.forms import FilePathField
from django.db import connection
from django.http import StreamingHttpResponse as st
from django.http import HttpResponse
from django.shortcuts import redirect, render



from .forms import InventarioForm, LocalizadorForms, TareasForm
from .models import InventarioDeBodega, Tareas
import os 
from wsgiref.util import FileWrapper
import mimetypes
# Create your views here.
#############################################################################
#Home view y cargar 
def home(request):
   return  render(request, 'paginas/home.html')

def CyD(request):
   return  render(request, 'paginas/cyd1.html')

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

#Exportar inventario ocurre aqui
def export_to_csv(request):
    inventario_objs =  InventarioDeBodega.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment ; filename=inventario_export.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'columnas','bloque','ContenidosInv','created','updated'])
    inventario_fields = inventario_objs.values_list('id', 'columnas','bloque','ContenidosInv','created','updated')
    for inventario in inventario_fields:
        writer.writerow(inventario)
    return response
    

# toda la gestion de descarga de archivos 

def Descargar_Archivos(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = '\\Finder.zip'
    FilePathField = base_dir  + filename
    thefile = FilePathField
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = st(FileWrapper(open(thefile,'rb'),chunk_size),
        content_type = mimetypes.guess_type(thefile)[0] )
    response['Content-length']  = os.path.getsize(thefile)
    response['Content-Disposition'] = "Atachment;filename%s" % filename
    return response

