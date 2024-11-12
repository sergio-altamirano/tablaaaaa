from django.urls import path
from Taqueriawero_app import views

urlpatterns = [
    path('',views.inicio_vista,name="inicio_vista"),
    path("registrarTrabajador/",views.registrarTrabajador,name="registrarTrabajador"),
    path("seleccionarTrabjador/<id_trabajador>",views.seleccionarTrabjador,name="seleccionarTrabjador"),
    path("borrarTrabajador/<id_trabajador>",views.borrarTrabajador,name="borrarTrabajador"),
    path("editarTrabajador/",views.editarTrabajador,name="editarTrabajador")
]