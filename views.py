from django.shortcuts import render
from datetime import datetime

def mostrar_fecha_hora_actual(request):
    fecha_hora_actual = datetime.now()
    return render(request, 'fecha_hora_actual.html', {'fecha_hora_actual': fecha_hora_actual})
