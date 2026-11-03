
from django.shortcuts import render
from .models import Persona

def index_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {'personas': personas})

def detalle_persona(request, id):
    
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalles.html', {'persona': persona})

def nueva_persona(request):
    return render(request, 'personas/nuevo.html')