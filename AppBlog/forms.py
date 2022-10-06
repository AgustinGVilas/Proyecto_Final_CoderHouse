from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class FormuAutos(forms.Form):    #formulario para crear autos

    marca = forms.CharField()
    modelo = forms.CharField()
    año_fab = forms.IntegerField()
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()


class FormuRegisitro(UserCreationForm):   #formulario para el registro

    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class EditarUsuario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class FormuAvatar(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ['imagen']




