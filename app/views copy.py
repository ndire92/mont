
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm #add this
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login
from app.models import CustomUser, Post, Profile, Ressource
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from app.forms import SignUpForm, UserForm
from app.ressource import Ressou
from app.forms import PostForm

def Base(request):
    return render(request, 'pages/base.html')


def Accueil(request):
    return render(request, 'pages/accueil.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'pages/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'pages/login.html',context={"form":form})

def user_logout(request):
    logout(request)
    return redirect('https://precvadi.sn/')



@login_required(login_url='home')
def PROFILE(request):

    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user,
    }

    return render(request, 'pages/profile.html', context)


@login_required(login_url='home')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic

            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
                customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request, 'Failed To Update Your Profile')

    return render(request, 'pages/profile.html')



def peche(request):
    
    return render(request, 'pa/peche.html')
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
            form.user = request.user
            form.save()
            return redirect('/post/')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'pa/new_post.html', context)


# @login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Vérifiez si l'utilisateur est l'auteur du post
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/post/')
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
    if post.user == request.user:
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

def ress(request):
    
    if request.method == 'POST':
        form = Ressou(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('ressource')
    else:
        form = Ressou()
    return render(request, 'pa/ressource.html', {'form': form, 'dataObject': Ressource.objects.all()})



def upda_ress(request,id):
    stud= Ressource.objects.get(id=id)

    if request.method == 'POST':
            form = Ressou(request.POST, request.FILES,instance=stud)
            if form.is_valid():
                form.save()
                return redirect('ressource')

    else:
            form = Ressou(instance=stud)


    context = {

    'form': form,
    
    }
   
    return render(request,'pa/update_ress.html',context)


def del_ress(request,id):
    stud =Ressource.objects.get(id=id)
    stud.delete()
    return redirect('ressource')


    return render(request,'pa/delete.html')


