from django import forms 

class FormNewPrestamo(forms.Form):
    monto =forms.IntegerField(min_value=0, required=True, label='Monto: ', initial=1000)
    plaxo = forms.IntegerField(max_value=360,min_value=1, required=True, label='Plazo: ', initial=24)

tasa_interes = forms.DecimalField(
    min_value=0,
    max_value=100,
    decimal_places=2,
    required=True,
    label='Tasa de Interés:',
    initial=5.00
)
    