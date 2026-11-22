
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index_personas, name='index_personas'),
    path('personas/detalles/<int:id>/', views.detalle_persona, name='detalle_persona'),
    path('personas/nueva/', views.nueva_persona, name='nueva_persona'),
]
