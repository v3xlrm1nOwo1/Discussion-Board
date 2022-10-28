from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random
from . import models
# import .models
# import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views import generic
from django.utils import timezone
from django.utils.decorators import method_decorator
# Create your views here.

def test(request):

    lev = random.randint(0, 1000)
    name = "Blacke-Heart"

    HTML_RESPONSE = f"""<h1>Name: {name}</h1>
                        <p>Lev: {lev}</p>"""

    return HttpResponse(HTML_RESPONSE)


# Home Page
# def home(request):

#     boards = models.Board.objects.all()
#     context = {'boards': boards}
#     return render(request, 'home.html', context)

class BoardListView(generic.ListView):
    
    model = models.Board
    context_object_name = 'boards'
    template_name = 'home.html'


# board topics
def board_topics(request, board_name):

    board = get_object_or_404(models.Board, name=board_name)
    topics = board.topics.order_by("-created_dt").annotate(count_post=Count('posts'))
    context = {'board': board, 'topics': topics}
    return render(request, 'topics.html', context)


# New Topic
@login_required
def new_topic(request, board_name):
    
    board = get_object_or_404(models.Board, name=board_name)
    if request.method == "POST":
        form = forms.NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()
            
            post = models.Post.objects.create(
                comment=form.cleaned_data.get('comment'),
                topic=topic,
                created_by=request.user
            )
            
            return redirect('board_topics', board_name=board.name)
    else:
        form = forms.NewTopicForm()

    context = {'board': board, 'form': form}
    return render(request, 'new_topic.html', context)


def topic_posts(request, board_name, topic_id):
    topic = get_object_or_404(models.Topic, board__name=board_name, pk=topic_id)
    topic.views += 1
    topic.save()
    
    context = {'topic': topic}
    return render(request, 'topic_posts.html', context)


@login_required
def reply_topic(request, board_name, topic_id):
    topic = get_object_or_404(models.Topic, board__name=board_name, pk=topic_id)
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', board_name=topic.board.name, topic_id=topic.pk)
    else:
        form = forms.PostForm()
    context = {'topic': topic, 'form': form}
    return render(request, 'reply_topic.html', context)


# GCBV
@method_decorator(login_required, name='dispatch')
class EditPostView(generic.UpdateView):
    
    model = models.Post 
    fields = ['comment', ] # field name
    template_name = 'edit_post.html' # name the template
    pk_url_kwarg = 'post_id' # post_id is name of var in url
    context_object_name = 'post' # post is name of object to move 
    
    def form_valid(self, form):
        
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_dt = timezone.now()
        post.save()
        return redirect('topic_posts', board_name=post.topic.board.name, topic_id=post.topic.pk)
    
    