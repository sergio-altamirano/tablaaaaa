from django.shortcuts import render,redirect
from .models import Trabajador

# Create your views here.

def inicio_vista(request):
    eltrabajador=Trabajador.objects.all()
    return render(request,'gestionarTrabajador.html',{"mistrabajadores":eltrabajador})

def registrarTrabajador(request):
    id_trabajador=request.POST["txtid_trabajador"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtnombre"]
    curp=request.POST["txtnombre"]
    fecha_nacimiento=request.POST["txtnombre"]
    puesto=request.POST["txtnombre"]
    salario=request.POST["numcreditos"]

    guardarTrabajador=Trabajador.objects.create(id_trabajador=id_trabajador,nombre=nombre,apellido=apellido,curp=curp,fecha_nacimiento=fecha_nacimiento,puesto=puesto,salario=salario) 

    return redirect('/')

def seleccionarTrabajador(request,id_trabajador):
    Trabajador=Trabajador.objects.get(id_trabajador=id_trabajador)
    return render(request,"editarTrabajador.html",{"mitrabajador":Trabajador})

def editarMateria(request):
    id_trabajador=request.POST["txtid_trabajador"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtnombre"]
    curp=request.POST["txtnombre"]
    fecha_nacimiento=request.POST["txtnombre"]
    puesto=request.POST["txtnombre"]
    salario=request.POST["numcreditos"]

    Trabajador=Trabajador.objects.get(id_trabajador=id_trabajador)

    Trabajador.id_trabajador=id_trabajador
    Trabajador.nombre=nombre
    Trabajador.apellido=apellido
    Trabajador.curp=curp
    Trabajador.fecha_nacimiento=fecha_nacimiento
    Trabajador.puesto=puesto
    Trabajador.salario=salario
    Trabajador.save()

    return redirect('/')

def borrarMateria(request,id_trabajador):
    Trabajador=Trabajador.objects.get(id_trabajador=id_trabajador)
    Trabajador.delete()

    return redirect("/")