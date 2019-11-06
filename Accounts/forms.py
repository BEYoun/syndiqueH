from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,PasswordInput,EmailInput


class SignUpForm(UserCreationForm):
    # role = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=TextInput(
        attrs={
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Nom'
        }))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=TextInput(
        attrs={
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Prénom'
        }))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=EmailInput(
        attrs={
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Email'
        }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'class':'form-control','id':'inputName','placeholder':'Nom d\'utilisateur'}),
            'password1': PasswordInput(attrs={'class':'form-control','id':'inputConfPassword','placeholder':'Confirm Password'}),
            'password2': PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
        }

class SyndiqueForm(UserCreationForm):
    # role = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=TextInput(
        attrs={
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Nom'
        }))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=TextInput(
        attrs={
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Prenom'
        }))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=EmailInput(
        attrs={
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Email'
        }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'class':'form-control','id':'inputName','placeholder':'Nom d\'utilisateur'}),
            'password1': PasswordInput(attrs={'class':'form-control','id':'inputConfPassword','placeholder':'mot de pass'}),
            'password2': PasswordInput(attrs={'class':'form-control','placeholder':'Confirmation mot de pass'}),
        }