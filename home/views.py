
from django.http import Http404
from django.shortcuts import render, redirect
# from .formulaires import DimAgroAssurancef


from home.models import Post, Slider
from .forms import PostForm
# from .models import Attendance, Course, DimAgroAssurance, FactAgriculture, Post, Slider, Student, Students, Studenttt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
# import pandas as pd

# Create your views here.


# @login_required
def ho(request):
    posts = Post.objects.order_by('-id').all()
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    posts_number = posts.count()
    message = f'{posts_number} posts:'
    if posts_number == 1:
        message = f'{posts_number} post:'

    context = {
        'posts': page_object,
        # 'post_number':post_number,
        'message': message
    }

    return render(request, 'pa/index.html', context)


# @login_required
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'pa/detail.html', context)

# @login_required


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.admin = request.admin
            form.save()
            return redirect('/post/')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'pa/new_post.html', context)


# @login_required
def update_post(request, id):
    post = Post.objects.get(id=id)
    if post== request.admin:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/post/')
            9

        else:
            form = PostForm(instance=post)
    else:
        raise Http404

    context = {

        'form': form,
        'post': post
    }
    return render(request, 'pa/update_post.html', context)


# @login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.admin == request.admin:
        post.delete()
        return redirect('/post/')
    else:
        raise Http404

    return render(request, 'pa/delete.html')


# @login_required
def search(request):
    search = request.GET.get('search')
    posts = Post.objects.filter(Q(title__icontains=search) |
                                Q(content__icontains=search) |
                                Q(image__icontains=search)
                                )

    posts_number = posts.count()
    message = f'{posts_number} results:'
    if posts_number == 1:
        message = f'{posts_number} results:'

    context = {
        'posts': posts,
        'message': message,
    }
    return render(request, 'pa/search.html', context)


def all(request):

    posts = Post.objects.order_by('-id').all()
    context = {
        'posts': posts,
        # 'post_number':post_number,

    }

    return render(request, 'pa/blog.html', context)


def commun(request):

    return render(request, 'pa/commun.html',)


def domaine(request):

    return render(request, 'pa/domaine.html',)


def peche(request):

    return render(request, 'pa/peche.html')


def foncier(request):

    return render(request, 'pa/foncier.html')


def agriculture(request):

    return render(request, 'pa/agriculture.html')


def sante(request):

    return render(request, 'pa/sante.html')


def education(request):

    return render(request, 'pa/education.html')


def tabview(request):
    # daga = DimAgroAssurancef()

    return render(request, 'pa/tab.html')


def LOGIN(request):
    return render(request, 'pa/login.html')


def Sin(request):
    # daga = DimAgroAssurancef()

    return render(request, 'pa/in.html')
