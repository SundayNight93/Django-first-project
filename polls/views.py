from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime


def index(request):
    message = """
        <html>
            <body>
                <h2>¡Hola a todos!</h2>
            </body>
        </html>
        """
    return HttpResponse(message)

def adios(request):
    message = """
        <html>
            <body>
                <h2>¡Adios a todos!</h2>
            </body>
        </html>
        """
    return HttpResponse(message)

def fecha(request):
    fecha_actual = datetime.datetime.now()

    message = """
        <html>
            <body>
                <h2>Fecha y Hora actuales %s</h2>
            </body>
        </html>
        """ % fecha_actual

    return HttpResponse(message)