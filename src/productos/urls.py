from django.urls import path
from productos.views import *

urlpatterns = [
    path('inicio/', index, name="productos_inicio"),
]