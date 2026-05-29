from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from user.forms import SignUpForm, LoginForm

#La vista se crea heredando de una plantilla, indicando el formulario y el html que usará
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'login/register.html'


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'
