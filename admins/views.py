
from django.shortcuts import redirect, render
from .models import Persona


def index_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {'personas': personas})


def detalle_persona(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalles.html', {'persona': persona})


def nueva_persona(request):
    if request.method == 'GET':
        return render(request, 'personas/nuevo.html')
    else:
        datos = request.POST

        persona = Persona.objects.create(
            ci=datos.get('ci'),
            nombres=datos.get('nombre'),
            apellidos=datos.get('apellido'),
            direccion=datos.get('direccion'),
            telefono=datos.get('telefono'),
            fecha_nacimiento=datos.get('fecha_nacimiento'),
            email=datos.get('email')
        )

        return redirect('index_personas')
