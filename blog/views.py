from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def blog(request):
    blogposts = Blog.objects
    return render(request,'blog/blog.html',{'blogposts':blogposts})

def detail(request,blog_id):
    detailblog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html',{'blog':detailblog})