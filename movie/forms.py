from django import forms
from .models import Tareas
from .models import InventarioDeBodega


class TareasForm(forms.ModelForm):
    class Meta:
        model= Tareas
        fields = '__all__'

class InventarioForm(forms.ModelForm):
    class Meta:
        model = InventarioDeBodega
        fields = '__all__'