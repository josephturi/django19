from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
    # if request.method == "POST":
    #     print(request.POST.get("title"))
    #     print(request.POST.get("content"))
    #     Post.object.create(title=title)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "title": instance.title,
        "content": instance.content,
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("Delete")
