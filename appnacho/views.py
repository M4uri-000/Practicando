from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ooo(request):
    html="""
        <h1>!HOLA¡</h1>
        <p>soy un subtitulo XDDDDD</p>
    """
    return HttpResponse(html)