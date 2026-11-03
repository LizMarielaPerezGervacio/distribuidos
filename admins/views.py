
from django.shortcuts import render
from .models import Persona
def index_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html',{'personas':personas})
