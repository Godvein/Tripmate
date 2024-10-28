from django.urls import path
from . import views
from .views import listblog
urlpatterns = [
    path('', listblog.as_view(), name="blogs" ),
    path('add_blogs/', views.addBlogs, name = "add_blogs")
]