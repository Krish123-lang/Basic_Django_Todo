from django.shortcuts import redirect, render
from .forms import BlogForm
from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'blogs': blogs, 'form': form}
    return render(request, 'home.html', context)


def post(request, slug):
    posts = Blog.objects.get(new_slug=slug)
    context = {'posts': posts}
    return render(request, 'post.html', context)


def update(request, slug):
    up_blogs = Blog.objects.get(new_slug=slug)
    form = BlogForm(instance=up_blogs)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=up_blogs)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'up_blogs': up_blogs, 'form': form}
    return render(request, 'home.html', context)


def delete(request, slug):
    del_blog = Blog.objects.get(new_slug=slug)

    if request.method == "POST":
        del_blog.delete()
        return redirect('home')
    context = {'del_blog': del_blog}
    return render(request, 'delete.html', context)
