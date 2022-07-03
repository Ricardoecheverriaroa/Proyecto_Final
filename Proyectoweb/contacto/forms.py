from django import forms

class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True,  max_length=10)
    
    email=forms.CharField(label="Email", required=True,  max_length=20)
    
    contenido=forms.CharField(label="Contenido", max_length=100, widget=forms.Textarea)
    