from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

#El formulario se pasa a la vista para mostrarse
class SignUpForm(UserCreationForm):
    username = forms.CharField(help_text=None, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    full_name = forms.CharField(help_text=None, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    email = forms.EmailField(label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    password1 = forms.CharField(label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}))


    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'password1', #ingreso
            'password2', #confirmacion
        ]

class LoginForm(AuthenticationForm):

    username = forms.CharField(label=False, help_text=None,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label=False, help_text=None,
                               widget=forms.PasswordInput({'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'password',]