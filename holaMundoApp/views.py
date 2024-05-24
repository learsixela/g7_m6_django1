from django.shortcuts import render
from django.http import HttpResponse
# Create your views here controladores.

def hola(request):
    return HttpResponse("""
                        <h1>Hola desde otro metodo</h1>
                        <p>Esto es un parrafo desde django</p>
                        """)
def index(request):
    return HttpResponse("""
        <h1>Hola Mundo!!!</h1>
    """)