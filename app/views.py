from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Libro
from .forms import AgregarLibroForm
from app import models

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = AgregarLibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = AgregarLibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def buscar_libros(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        resultados = Libro.objects.filter(
            models.Q(titulo__icontains=query) |
            models.Q(autor__nombre__icontains=query) |
            models.Q(editorial__nombre__icontains=query)
        )
        return render(request, 'resultado_busqueda.html', {'resultados': resultados})
    else:
        return render(request, 'buscar_libros.html')