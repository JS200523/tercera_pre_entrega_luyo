from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('buscar/', views.buscar_libros, name='buscar_libros'),
]