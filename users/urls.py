from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('endereço/', view.as_view(), name='nome-da-url'), 
    path('login/', auth_views.LoginView.as_view(
        template_name = "users/form.html"    
    ), name='login'),
    
]