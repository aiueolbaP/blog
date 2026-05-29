
from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'), #nombre de la clase.asview para convertir en vista
    path('add/', views.SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
