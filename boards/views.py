from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def test(request):

    lev = random.randint(0, 1000)
    name = "Blacke-Heart"

    HTML_RESPONSE = f"""<h1>Name: {name}</h1>
                        <p>Lev: {lev}</p>"""

    return HttpResponse(HTML_RESPONSE)