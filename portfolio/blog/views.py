from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects
    blogDict = {'blogs':blogs}
    return render(request, 'blog/blog.html', blogDict)

def detail(request, blog_id):
    detailBlog = get_object_or_404(Blog, pk=blog_id)
    detailBlogDict = {'blog':detailBlog}
    return render(request, 'blog/detail.html', detailBlogDict)