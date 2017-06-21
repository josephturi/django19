from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, 'Successful Create', extra_tags='html_safe')
        return redirect('posts:list')
        # return HttpResponseRedirect(instance.get_absolute_url())
    if not form.is_valid:
        messages.error(request, 'Save failed Create', extra_tags='html_safe')
    # if request.method == "POST":
    #     print(request.POST.get("title"))
    #     print(request.POST.get("content"))
    #     Post.object.create(title=title)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_list(request):
    queryset_list = Post.objects.all()#.order_by("-timestamp")
    paginator = Paginator(queryset_list, 7) # Show 7 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    context = {
        "title": "List",
        "object_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "post_list.html", context)

def post_detail(request, slug=None):
    # instance = Post.objects.get(pk=1)
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successful Update', extra_tags='html_safe')
        return redirect('posts:list')
        # return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, 'Save failed Update', extra_tags='html_safe')
    context = {
        "title": instance.title,
        "content": instance.content,
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Successfuly deleted', extra_tags='html_safe')
    return redirect('posts:list')


