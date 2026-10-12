from django.db import models
from django.utils import timezone
from admins.models import Socio, Cajera

class Prestamo(models.Model):
    monto = models.IntegerField(default=10000)
    plazo = models.IntegerField(default=24)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    fecha = models.DateField(default=timezone.now)
    vigente = models.BooleanField(default=True)
    socio = models.ForeignKey(Socio, on_delete=models.PROTECT, related_name='prestamos')

    def __str__(self):
        return f"{ self.socio }; Bs. { self.monto }" 

    class Meta: 
            ordering = ['vigente','fecha']

class Amortizacion(models.Model):
    capital = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    interes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha = models.DateTimeField(default=timezone.now)
    prestamo = models.ForeignKey(Prestamo, on_delete=models.PROTECT, related_name='amortizaciones')
    cajera = models.ForeignKey(Cajera, on_delete=models.PROTECT, related_name='amortizaciones')

    def __str__(self):
        return f"{self.prestamo} {self.fecha}: Bs. {self.capital + self.interes}"

    class Meta:
        ordering = ['fecha']
        verbose_name_plural = 'Amortizaciones'