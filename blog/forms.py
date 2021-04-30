from django import forms
from .import models
from django.forms import ModelForm
from .models import Comment
#from django import forms as formView


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
