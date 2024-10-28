from django.shortcuts import render
from django.views.generic import ListView
from .models import blogs
# Create your views here.
class listblog(ListView):
    template_name = "core/blog.html"
    model = blogs
    context_object_name = 'blogs'

    