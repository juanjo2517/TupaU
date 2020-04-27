from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = [
        'nombre','apellido', 'correo_electronico',
        'username','foto_perfil','fecha_nacimiento']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo_electronico': 'Correo',
            'usermame':'Usuario'
        }

        widgets = {'nombre': forms.TextInput(attrs='input-login')}