
from django import forms
from .models import Profile,Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Entrez une adresse e-mail valide.', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    username= forms.CharField(label='utilisateur', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    first_name= forms.CharField(label='prénom', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    last_name= forms.CharField(label='nom', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    password1= forms.CharField(label='mot de passe', widget=forms.PasswordInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    password2= forms.CharField(label='confirmer password', widget=forms.PasswordInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
        
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
        
        
class UserForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    phone = forms.CharField(label='Tel', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    addresse = forms.CharField(label='Adresse', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['description', 'phone', 'addresse', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs.update({'class': 'form-control'})

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titre',widget=forms.TextInput(attrs={
        'class':'form-controle',
}))
    content = forms.CharField(label='Content',widget=forms.Textarea(attrs={
    'class':'form-control',
    }))

    class Meta:
        model = Post
        fields = ('title' ,'content', 'image')