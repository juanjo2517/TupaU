from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    """Esta clase tendrá dos funciones: Una para crear un usuario normal
    y otra para crear un superusuario"""

    def create_user(self, correo_electronico, username, nombre, apellido, password = None):
        #Crea un usuario normal
        if not correo_electronico:
            raise ValueError('El usuario debe tener un Correo Electrónico')

        usuario = self.model(
            username = username, 
            email = self.normalize_email(correo_electronico), 
            nombre = nombre,
            apellido = apellido
            )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, correo_electronico, username, nombre, apellido, password):
        #Crea un superUsuario

        usuario = self.create_user(
            correo_electronico, 
            username = username, 
            nombre = nombre,
            apellido = apellido 
            )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=150, blank=False, null=False)
    correo_electronico = models.EmailField('Correo Electrónico', max_length=254, unique=True, blank=False, null=False)
    username = models.CharField('Nombre de Usuario', max_length=50, unique=True, blank=False, null=False)
    foto_perfil = models.ImageField('Foto de Perfil',upload_to='perfil/', 
                                height_field=None,width_field=None, 
                                max_length=200,blank=False, 
                                null=False
                                )
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', auto_now=True, auto_now_add=False)
    activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()
    
    #Campo que diferencia al usuario de los demás
    USERNAME_FIELD = 'email'

    #Campos requeridos
    REQUIRED_FIELDS = ['username','nombre','apellido']

    def __str__(self):
        return f'Usuario {self.nombre},{self.apellido}'

    def has_perm(self, perm, obj = None):
        """Este metodo es llamado por el administrador de Django, 
        para otorgar el permiso de entrar al administrador de Django"""
        return True
    
    def has_module_perms(self, app_label):
        """Tambien es para el administrador de Django, recibe app_label
        que basicamente dice en que aplicacion esta situado nuestro modelo Usuario"""
        return True
    
    @property
    def is_staff(self):
        #Verifica si el usuario es administrador o no
        return self.usuario_administrador
