from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    html="""
        <h1>!HOLA¡</h1>
        <p>el rodrigo es el masca</p>
    """
    return HttpResponse(html)
