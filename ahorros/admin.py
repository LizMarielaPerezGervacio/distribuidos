from django.contrib import admin
from .models import Ahorro

@admin.register(Ahorro)
class AhorroAdmin(admin.ModelAdmin):
    list_display = ('id', 'socio', 'cajera', 'debito', 'credito', 'fecha')
    search_fields = ('socio__persona__nombres', 'socio__persona__apellidos', 'socio__numero')
    list_filter = ('fecha',)