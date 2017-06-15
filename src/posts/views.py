from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

def post_create(request):
    return HttpResponse("Create")

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "object_list": queryset,
    }
    return render(request, "index.html", context)

def post_detail(request, id=None):
    # instance = Post.objects.get(pk=1)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_update(request):
    return HttpResponse("Update")

def post_delete(request):
    return HttpResponse("Delete")