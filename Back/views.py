from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .forms import Mascotas,AgregarUsuario, Login
from .models import Mascota, Usuario
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
#importamos lo nenesario para que la aplicacion fuincione a su 100%

#defino acciones posibles para establecer permisos

acciones=[
   {'Mostrar':'Home','url':'inicio'} 
]
# Create your views here.
def index(request):
    return render(request, "index.html")
def salir(request):
    logout(request)
    return redirect('/')
#***************************************************************************************************************************************************
#****************************        gestion de usuarios         ***********************************************************************************
@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("correo") ,data.get("password"))
        regDB.save()
    usuarios=User.objects.all()
    form=AgregarUsuario()
    return render(request,"GestionarUsuarios.html",{'actual':actual,'form':form,'usuarios':usuarios,'acciones':acciones,})


def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('inicio')
    return render(request,"login.html",{'form':form,})
#***************************************************************************************************************************************************
#****************************         Edicion y gestion de mascotas        *************************************************************************

  
@login_required(login_url='login')
def MascotaView(request):
    if request.method == 'POST':
        form = Mascotas(request.POST)
        if form.is_valid():
            form.save()
        return redirect('MostrarMascota')
    else:
        form = Mascotas()
    return render (request,'GestionMascota.html',{'form':form})

@login_required(login_url='login')
def MostrarMascota(request):
    mascota= Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request,'MostrarMascota.html',contexto)

#funcion la cual nos muesta 
@login_required(login_url='login')
def editarMascota(request,idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    if request.method == 'GET':
        form = Mascotas(instance=mascota)
    else:
        form = Mascotas(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('MostrarMascota')
    return render (request, 'GestionMascota.html',{'form':form})
#funcion la cual elimina una mascota 
@login_required(login_url='login')
def MascotaDelete (request,idMascota):
    mascota = Mascota.objects.get(idMascota=idMascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('MostrarMascota')
    return render(request, 'MascotaDelete.html', {'mascota':mascota})
#***************************************************************************************************************************************************
#****************************         paginacion        ********************************************************************************************
#mostramos las mascotas con esta clase
class MascotaList(ListView):
    model = Mascota
    template_name = 'MostrarMascota.html'
    paginate_by = 3

#clase para la paginacion de crear una mascota 
class MascotaCreate(CreateView):
    model = Mascota
    form_class = Mascotas
    template_name = 'GestionMascota.html'
    success_url = reverse_lazy('MostrarMascota')

#clase para la paginacion editar una mascota 
class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = Mascotas
    template_name = 'GestionMascota.html'
    success_url = reverse_lazy('MostrarMascota')

#clase para la paginacion eliminar una mascota 
class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'MascotaDelete.html'
    success_url = reverse_lazy('MostrarMascota')


def formulario(request):
    return render(request, "Formulario.html")
    
def quienessomos(request):
    return render(request, "QuienesSomos.html")
    

#***************************************************************************************************************************************************
#****************************        Mostrnado mascotas con imagenes solo para usuarios normales        ********************************************

@login_required(login_url='login')
def VerMascota(request):
    actual=request.user
    form=Mascotas(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        mascota=Mascota(idMascota=data.get("idMascota"),fotoMascota=data.get("idMascota"),mascotaname=data.get("mascotaname"),raza=data.get("raza"),generomascota=data.get("generomascota"),estado=data.get("estado"))
        mascota.save()
    mascota=Mascota.objects.filter(estado='Disponible')
    form=AgregarUsuario()
    return render(request,"MascotaDisponible.html",{'actual':actual,'form':form,'mascota':mascota,'acciones':acciones,})

#***************************************************************************************************************************************************
#****************************         recuperar la contraseña por correo electronico        *********************************************************
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('se a cambiado exitosamente tu contraseña '))
            return redirect('change_password')
        else:
            messages.error(request, ('Incorrecto revise el error'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {
        'form': form
    })
