from django.shortcuts import render, redirect
from harris.models import Blog

def home(request):
    return render(request, template_name="harris/index.html")

def blog(request):
    blog_posts = Blog.objects.all()
    ctx = {"blog_posts": blog_posts}
    return render(request, template_name="harris/blog.html", context=ctx)

def get_blog(request, id):
    blog_post = Blog.objects.get(pk=id)
    return render(request, template_name="harris/detailed_blog.html", context={"blog_post": blog_post})