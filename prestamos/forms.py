
from django import forms
from datetime import date
from admins.models import Socio


class FormNewPrestamo(forms.Form):
    monto = forms.IntegerField(
        min_value=1, required=True,
        label='Monto:', initial=50000
    )

    plazo = forms.IntegerField(
        min_value=1, max_value=360,
        required=True, label='Plazo:',
        initial=48
    )

    tasa_interes = forms.DecimalField(
        min_value=0, max_value=100,
        decimal_places=2, required=True,
        label='Tasa de interés anual (%):',
        initial=6.00
    )

    fecha = forms.DateField(
        label='Fecha del préstamo:',
        initial=date.today,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        )
    )

    socio = forms.ModelChoiceField(
        queryset=Socio.objects.all(),
        label='Nombre del socio',
        required=True
    )
