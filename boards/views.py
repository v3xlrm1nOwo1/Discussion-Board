from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from . import models
# import .models
# import models

# Create your views here.

def test(request):

    lev = random.randint(0, 1000)
    name = "Blacke-Heart"

    HTML_RESPONSE = f"""<h1>Name: {name}</h1>
                        <p>Lev: {lev}</p>"""

    return HttpResponse(HTML_RESPONSE)


# Home Page
def home(request):

    boards = models.Board.objects.all()
    context = {'boards': boards}
    return render(request, 'home.html', context)


# board topics
def board_topics(request, board_name):

    board = get_object_or_404(models.Board, name=board_name)
    context = {'board': board}
    return render(request, 'topics.html', context)