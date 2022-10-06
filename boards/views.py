from multiprocessing import context
from pydoc_data.topics import topics
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random
from . import models
# import .models
# import models
from . import forms
from django.contrib.auth.models import User

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


# New Topic
def new_topic(request, board_name):
    
    board = get_object_or_404(models.Board, name=board_name)
    user = User.objects.first()
    if request.method == "POST":
        form = forms.NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()
            
            post = models.Post.objects.create(
                comment=form.cleaned_data.get('comment'),
                topic=topic,
                created_by=user
            )
            
            return redirect('board_topics', board_name=board.name)
    else:
        form = forms.NewTopicForm()

    context = {'board': board, 'form': form}
    return render(request, 'new_topic.html', context)