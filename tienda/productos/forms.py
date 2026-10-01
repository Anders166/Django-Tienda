from django import forms
from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 3})}

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if not nombre:
            raise forms.ValidationError("El nombre no puede estar vacío.")
        return nombre


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad', 'estado']

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa.")
        return cantidad
