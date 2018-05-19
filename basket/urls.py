from django.urls import path
from basket import views


urlpatterns = [
    path('agregar', views.agregar, name="agregar"),
    path('listar', views.listar, name="listar"),
    path(r'player/(?P<pk>\d+)/$', views.editar, name="editar"),
    path(r'eliminar/(?P<pk>\d+)/$', views.eliminar, name="eliminar"),
    path(r'editar/(?P<pk>\d+)/$', views.editar_final, name="editar_final"),




]
