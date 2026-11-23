from django import forms 
from datetime import datetime
from admins.models import Socio

class FormNewPrestamo(forms.Form):
    monto =forms.IntegerField(min_value=0, required=True, label='Monto: ', initial=1000)
    plazo = forms.IntegerField(max_value=360,min_value=1, required=True, label='Plazo: ', initial=24)
    tasa_interes = forms.DecimalField(min_value=0,max_value=100,decimal_places=2,required=True,label='Tasa de Interés:',initial=5.00)
    fecha = forms.DateField(initial=datetime.now(),label='fehca de prestamo', required=True,widget=forms.DateInput(attrs={'type':'date'}))
    socio=forms.ModelChoiceField(label='nombre del socio',required=True ,querysed=Socio.objects.all())
    