
# Register your models here.
from dataclasses import asdict
from pyexpat import model
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import InventarioDeBodega
from django.contrib import admin
from .models import InventarioDeBodega
from .models import Tareas




class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id','columnas','filas','bloque','ContenidosInv' )
    search_fields =  ["ContenidosInv"]
    


    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'El tipo de archivo que has seleccionado nos es CSV.')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            #me hace un split de cada elemento en el csv para tenerlo como una lista parte cada coma
            for x in csv_data:
                fields = x.split(",")
                created = InventarioDeBodega.objects.update_or_create(
                    id = fields[0],
                    columnas = fields[1],
                    filas = fields[2],
                    bloque = fields[3],
                    ContenidosInv=fields[4]

                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(InventarioDeBodega, InventoryAdmin)
admin.site.register(Tareas)


