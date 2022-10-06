from logging import PlaceHolder
from django import forms
from . import models


class NewTopicForm(forms.ModelForm):
    
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'placeholder':'What is on your mind?...'}), max_length=5000, help_text="The max length is 5000")
    class Meta:
        
        model = models.Topic
        fields = ['subject', 'comment']