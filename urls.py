from django.urls import path
from . import views

urlpatterns = [
    path('fecha-hora-actual/', views.mostrar_fecha_hora_actual, name='fecha_hora_actual'),
]
