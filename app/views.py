from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Libro
from .forms import AgregarLibroForm
from app import models

def base(request):
    return render(request, 'base.html')

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
    if 'q' in request.GET:
        q = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=q)
        return render(request, 'buscar_libros.html', {'libros': libros, 'query': q})
    else:
        return render(request, 'buscar_libros.html')
    

 