from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', aboutinfo, name='about'),
    
    path('formulario/', formularioAutos, name='formulario'),
    
    path('busqueda/', busquedaAutos, name='busqueda'),
    path('resultadobusqueda/', resultadoBusqueda),
    
    path('error/', error),

    path('listaAutos/', ListarAutos.as_view(), name='listaAutos'),
    path('detalleAuto/<int:pk>', DetalleAutos.as_view(), name='detalleAuto'),
    path('editarAuto/<int:pk>', EditarAutos.as_view(), name='editarAuto'),
    path('eliminarAuto/<int:pk>', EliminarAutos.as_view(), name='eliminarAuto'),

    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('registro/', register, name='registro'),
    path('editarusuario/', editarUsuario, name='editarusuario'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),


]
