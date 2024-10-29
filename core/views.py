from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Blogs
# Create your views here.
class listblog(ListView):
    template_name = "core/blog.html"
    model = Blogs
    context_object_name = 'blogs'

def addBlogs(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        creator = request.user
        blog = Blogs(title = title, content = content, creator = creator)
        blog.save()
        return redirect("blogs")
    return render(request, "core/addblog.html")

def home(request):
    return render(request, "core/home.html")
    