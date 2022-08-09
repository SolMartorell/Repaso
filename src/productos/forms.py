from django.forms import Form, CharField

class FormularioBusqueda(Form):
    nombre_producto = CharField(max_length=30)