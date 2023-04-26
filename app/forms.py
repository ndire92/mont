
from django import forms
from .models import Post, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Entrez une adresse e-mail valide.', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    username = forms.CharField(label='utilisateur', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    first_name = forms.CharField(label='prénom', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    last_name = forms.CharField(label='nom', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    password1 = forms.CharField(label='mot de passe', widget=forms.PasswordInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    password2 = forms.CharField(label='confirmer password', widget=forms.PasswordInput(
        attrs={'placeholder': '', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={
        'class': 'form-controle',
    }))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class UserProfileForm(forms.ModelForm):
    description = forms.CharField(label='Code Commune', widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    phone_number = forms.CharField(label='Code Commune', widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    address = forms.CharField(label='Code Commune', widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['description', 'phone_number', 'address', 'profile_picture']

    def save(self, commit=True, user=None):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user = user
        if commit:
            profile.save()
        return profile
