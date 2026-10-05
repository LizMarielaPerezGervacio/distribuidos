from django.utils import timezone
from django.db import models

# Create your models here.
class Persona(models.Model):
    ci=models.CharField(max_length=8, unique=True, blank=False)
    nombres=models.CharField(max_length=30, blank=False)
    apellidos=models.CharField(max_length=30, blank=False)
    direccion=models.CharField(max_length=50, blank=False)
    telefono=models.CharField(max_length=8, blank=False)
    fecha_nacimiento=models.DateField()
    fecha_registro=models.DateTimeField(null=True, blank=True, default=timezone.now)
    email=models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.apellidos + ' ' + self.nombres
    class Meta:
        ordering = ['apellidos','nombres']

class Socio(models.Model):
    numero=models.CharField(max_length=10)
    fecha_registro=models.DateTimeField(default=timezone.now)
    persona=models.OneToOneField(Persona, on_delete=models.PROTECT, related_name='socio')

    def __str__(self):
        return f"{self.persona.nombres} {self.persona.apellidos} - Nro: {self.numero}"    
    class Meta:
        ordering=['numero']
class Cajera(models.Model):
    item = models.CharField(max_length=10, unique=True, blank=False)
    # Relación 1 a 1 con Persona según el diagrama
    persona = models.OneToOneField(
        Persona, on_delete=models.PROTECT, related_name="cajera"
    )

    def __str__(self):
        return f"Item: {self.item} - {self.persona.nombres} {self.persona.apellidos}"

    class Meta:
        ordering = ["item"]