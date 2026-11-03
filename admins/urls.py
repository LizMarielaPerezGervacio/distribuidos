from django.urls import path
from . import views

urlpatterns=[
    path('index',views.index_personas, name='index_personas')
]


#localhost:800/admin/index