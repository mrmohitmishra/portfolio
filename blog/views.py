from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog(request):
    blogposts = Blog.objects
    return render(request,'blog/blog.html',{'blogposts':blogposts})