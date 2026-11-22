
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormNewPrestamo


def index_prestamos(request):
    return HttpResponse('Nuevo prestamos')


def nuevo_prestamo(request):
    if request.method == 'POST':
        form = FormNewPrestamo(request.POST)

        if form.is_valid():
            return HttpResponse(
                'Formulario valido. Falta implementar el guardado.'
            )
    else:
        form = FormNewPrestamo()

    return render(request, 'prestamos/nuevo.html', {
        'form': form
    })
