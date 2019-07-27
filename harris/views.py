from django.shortcuts import render, redirect
from harris.models import Blog
from django.http import JsonResponse
from datetime import datetime, date


def home(request):
    return render(request, template_name="harris/index.html")


def get_info(request):
    return JsonResponse({
        "name": "Harris Beg",
        "role": "Developer",
        "github": "https://www.github.com/harrisbegca",
        "levels": [
            ("Python", 10),
            ("HTML", 10),
            ("Java", 9),
            ("CSS", 8),
            ("Javascript", 7),
            ("PHP", 7),
            ("Go", 6),
            ("C#", 5)
        ]
    })


def blog(request):
    blog_posts = Blog.objects.order_by('-timestamp')
    ctx = {"blog_posts": blog_posts, "navbar": True}
    return render(request, template_name="harris/blog.html", context=ctx)


def get_blog(request, id):
    blog_post = Blog.objects.get(pk=id)
    return render(request, template_name="harris/detailed_blog.html", context={"blog_post": blog_post, "navbar": True})
