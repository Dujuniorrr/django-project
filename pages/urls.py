from django.urls import path
from .views import IndexView, AboutView

urlpatterns = [
    # path('endereço/', view.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='index'),
    path('sobre/', AboutView.as_view(), name='about'),
]