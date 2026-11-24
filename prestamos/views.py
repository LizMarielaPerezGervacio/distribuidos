
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormNewPrestamo
from .models import Prestamo
from dateutil.relativedelta import relativedelta


def index_prestamos(request):
    return HttpResponse('Nuevo prestamos')


def nuevo_prestamo(request):
    if request.method == 'GET':
        form = FormNewPrestamo()

    else:
        form = FormNewPrestamo(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            prestamo = Prestamo.objects.create(
                monto=datos['monto'],
                plazo=datos['plazo'],
                tasa_interes=datos['tasa_interes'],
                socio=datos['socio']
            )

            return HttpResponse(str(plan_pagos(datos)))

    return render(
        request,
        'prestamos/nuevo.html',
        {'form': form}
    )


def plan_pagos(datos):
    saldo = float(datos['monto'])
    plazo = int(datos['plazo'])
    capital = saldo / plazo
    fecha = datos['fecha']
    tasa = float(datos['tasa_interes'])

    plan = [[0, 0, 0, saldo, fecha]]

    for p in range(1, plazo + 1):
        fila = []

        interes = saldo * (tasa / 12 / 100)
        capital_cuota = capital if p < plazo else saldo
        amortizacion = capital_cuota + interes

        saldo = saldo - capital_cuota
        fecha = fecha + relativedelta(months=1)

        fila.append(p)
        fila.append(capital_cuota)
        fila.append(interes)
        fila.append(amortizacion)
        fila.append(saldo)
        fila.append(fecha)

        plan.append(fila)

    return plan
