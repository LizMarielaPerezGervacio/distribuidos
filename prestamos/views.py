
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormNewPrestamo
from .models import Prestamo


def index_prestamos(request):
    return HttpResponse('Nuevo prestamos')


def nuevo_prestamo(request):
    if request.method == 'GET':
        form = FormNewPrestamo(request.POST)
       
    else:
        form = FormNewPrestamo(request.POST)
        if form.is_valid():
            datos=form.cloned_data
            Prestamo =Prestamo.objects.create(){
                monto=datos['monto'],
                plazo=datos['plazo'],
                tasa_interes=datos['tasa_interes'],
                socio=datos['socio'],
            }
            return HttpResponse(datos['socio'])

    return render(request, 'prestamos/nuevo.html', {'form': form})

