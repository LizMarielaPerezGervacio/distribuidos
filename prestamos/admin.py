from django.contrib import admin
from .models import Prestamo, Amortizacion
# Register your models here.

admin.site.register([
    Prestamo,
    Amortizacion,
])