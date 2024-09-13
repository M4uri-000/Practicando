from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ramanacho(request):
    html="""
        <h1>!HOLA¡</h1>
        <p>RAMANACHOCREADAHASSIDOHACKEADOXDDDDDD</p>
    """
    return HttpResponse(html)