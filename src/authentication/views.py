from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def login_view(request):
    
    if request.method == "GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }

        return render(request, "authentication/login.html", context)

    else:
        formulario  = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("productos_inicio")
            
        
        context = {
            "errores": "Formulario NO valido",
            "form": formulario
        }
        return render(request, "authentication/login.html", context)


def register_view(request):

    if request.method == "GET":
        formulario = UserCreationForm()
        return render(request, "authentication/register.html", {"form": formulario})
    else:
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("productos_inicio")
        else:
            return render(request, "authentication/register.html", {"form": formulario, "error": "Formulario NO valido"})



def logout_view(request):
    logout(request)
    return redirect("productos_inicio")