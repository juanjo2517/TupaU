from django.urls import path
from .views import Registro, Login

urlpatterns = [
    path('', Registro.as_view(), name='registro'),
    path('login/', Login.as_view(), name='login'),
]
