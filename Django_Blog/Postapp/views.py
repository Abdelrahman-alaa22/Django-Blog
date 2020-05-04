from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.models import User
# Create your views here.


class Home(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'Postapp/home.html'



