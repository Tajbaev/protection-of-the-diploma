from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


# Create your views here.

class MainView(ListView):
    template_name = 'index.html'
    model = CommentModel
    context_object_name = 'comment'
