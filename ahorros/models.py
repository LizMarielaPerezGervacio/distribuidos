
from django.db import models
from django.utils import timezone
from admins.models import Socio, Cajera

class Ahorro(models.Model):
    debito = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    credito = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    fecha = models.DateTimeField(default=timezone.now)
    
    socio = models.ForeignKey(Socio, on_delete=models.PROTECT, related_name='ahorros')
    cajera = models.ForeignKey(Cajera, on_delete=models.PROTECT, related_name='ahorros')

    def __str__(self):
        return f"Ahorro - Socio: {self.socio} | Débito: {self.debito} | Crédito: {self.credito}"

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = 'Ahorros'