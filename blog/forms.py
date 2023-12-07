from .models import BlogPost_table
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User


class BlogPost_form(forms.ModelForm):
    class Meta:
        model = BlogPost_table
        fields = ['title','description']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}) ,'description': forms.Textarea(attrs={'class':'form-control'})}


class LoginIn_form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':"current-password"}))


class SignUp_form(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'}),'email': forms.EmailInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'})} 