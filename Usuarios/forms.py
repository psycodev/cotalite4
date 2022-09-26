import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    direccion=forms.CharField(max_length=120)
    password1: forms.CharField(label='Contraeña',widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirma Contraeña',widget=forms.PasswordInput)
    class Meta: 
        model= User
        fields=[
            'username',
            'first_name',
            'last_name',
            'direccion',
            'email',
            'is_superuser',   
            'is_staff',
        ]
        labels ={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'E-mail',
            'is_superuser':"Rol",
            'is_staff':'staff',
        }

