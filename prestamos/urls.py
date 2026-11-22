
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_prestamos, name='index_prestamos'),
    path('nuevo/', views.nuevo_prestamo, name='nuevo_prestamos'),
]
