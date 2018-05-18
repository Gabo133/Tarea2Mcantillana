from django.urls import path
from basket import views


urlpatterns = [
    path('agregar', views.agregar, name="agregar"),
    path('listar', views.listar, name="listar"),
    path(r'detail/(?P<pk>\d+)/$', views.editar, name="editar"),


]
