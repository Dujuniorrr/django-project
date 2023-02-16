from django.urls import path
from .views import IndexView

urlpatterns = [
    # path('endereço/', view.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='index'),
]