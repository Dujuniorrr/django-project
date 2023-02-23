from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreate, UpdateProfile

urlpatterns = [
    # path('endereço/', view.as_view(), name='nome-da-url'), 
    path('login/', auth_views.LoginView.as_view(
        template_name = "users/login.html"    
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar/', UserCreate.as_view(), name='add-user'),
    path('editarDados/', UpdateProfile.as_view(), name='edit-profile'),
]