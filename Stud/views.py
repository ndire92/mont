
from django.db.models import Q
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.http import Http404
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login
from app.models import Post, Ressource, UserProfile
from django.contrib.auth import login
from django.contrib import messages
from app.forms import SignUpForm, UserProfileForm
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
    return render(request, 'pages/login.html', context={"form": form})


def user_logout(request):
    logout(request)
    return redirect('/')


def peche(request):

    return render(request, 'pa/peche.html')
# @login_required


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'pa/detail.html', context)

# @login_required


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        post.delete()
        return redirect('/post/')
    else:
        raise Http404

    return render(request, 'pa/delete.html')


@login_required(login_url='/login/')
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
            return redirect('/ressource/')
    else:
        form = Ressou()
    return render(request, 'pa/ressource.html', {'form': form, 'dataObject': Ressource.objects.all()})


@login_required(login_url='/login/')
def upda_ress(request, id):
    stud = Ressource.objects.get(id=id)

    if request.method == 'POST':
        form = Ressou(request.POST, request.FILES, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('ressource')

    else:
        form = Ressou(instance=stud)

    context = {

        'form': form,

    }

    return render(request, 'pa/update_ress.html', context)


@login_required(login_url='/login/')
def del_ress(request, id):
    stud = Ressource.objects.get(id=id)
    stud.delete()
    return redirect('ressource')

    return render(request, 'pa/delete.html')


@login_required(login_url='/login/')
def user_table(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        description = request.POST.get('description')
        profile_picture = request.FILES.get('profile_picture')

        try:
            user = User.objects.create_user(username, email, password)
            user_profile = UserProfile.objects.create(
                user=user, phone_number=phone_number, address=address, description=description, profile_picture=profile_picture)
            messages.success(request, 'Profile created successfully.')
            return redirect('profile-detail', id=user_profile.id)
        except:
            messages.error(request, 'An error occurred. Please try again.')

    return render(request, 'pages/user_table.html')


@login_required(login_url='/login/')
def user_edit(request, id):
    user_profile = get_object_or_404(UserProfile, id=id)

    # Check if the user is trying to edit his/her own profile
    if request.user != user_profile.user:
        messages.error(request, 'You are not authorized to edit this profile.')
        return redirect('all')

    if request.method == 'POST':
        user = user_profile.user
        new_username = request.POST.get('username')

        # check if the new username already exists
        try:
            User.objects.exclude(id=user.id).get(username=new_username)
            error_message = 'This username is already taken. Please choose a different one.'
            return render(request, 'pages/user_edit.html', {'user_profile': user_profile, 'error_message': error_message})
        except User.DoesNotExist:
            pass

        user.username = new_username
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')

        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')

        if new_password1 and new_password2:
            if new_password1 == new_password2:
                user.set_password(new_password1)
            else:
                error_message = 'Passwords do not match.'
                return render(request, 'pages/user_edit.html', {'user_profile': user_profile, 'error_message': error_message})

        user.save()

        user_profile.phone_number = request.POST.get('phone_number')
        user_profile.address = request.POST.get('address')
        user_profile.description = request.POST.get('description')

        if request.FILES.get('profile_picture'):
            user_profile.profile_picture = request.FILES.get('profile_picture')

        user_profile.save()

        messages.success(request, 'Profile updated successfully.')

        return redirect('profile-detail', id=user_profile.id)

    context = {'user_profile': user_profile}
    if request.user.is_authenticated and request.user == user_profile.user:
        context['success'] = True
    return render(request, 'pages/user_edit.html', context)


@login_required(login_url='/login/')
def delete_user(request, id):
    user_profile = get_object_or_404(UserProfile, id=id)

    # Check if the user is trying to delete his/her own profile
    if request.user != user_profile.user:
        messages.error(
            request, 'You are not authorized to delete this profile.')
        return redirect('user_profile_detail', id=user_profile.id)

    user_profile.delete()
    messages.success(request, 'Profile deleted successfully.')
    return redirect('home')


@login_required(login_url='/login/')
def ajout_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        form = UserProfileForm()

    context = {'form': form}
    return render(request, 'pages/add_profile.html', context)
