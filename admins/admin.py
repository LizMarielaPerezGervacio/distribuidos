from django.contrib import admin
from .models import Persona,Socio,Cajera
# Register your models here.
admin.site.register([
    Persona,Socio,Cajera
])