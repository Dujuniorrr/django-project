from django.urls import path

from .views import FieldCreate, ActivityCreate
from .views import  FieldUpdate, ActivityUpdate
from .views import FieldDelete, ActivityDelete
from .views import FieldList, ActivityList

urlpatterns = [
    # path('endereço/', view.as_view(), name='nome-da-url'),
    path('campo/cadastrar', FieldCreate.as_view(), name='add-field'),
    path('atividades/cadastrar', ActivityCreate.as_view(), name='add-activity'),
    
    path('campos/editar/<int:pk>', FieldUpdate.as_view(), name='edit-field'),
    path('atividades/editar/<int:pk>', ActivityUpdate.as_view(), name='edit-activity'),
    
    path('campos/deletar/<int:pk>', FieldDelete, name='delete-field'),
    path('atividades/deletar/<int:pk>', ActivityDelete.as_view(), name='delete-activity'),
    
    path('campos/', FieldList.as_view(), name='list-field'),
    path('atividades/', ActivityList.as_view(), name='list-activity'),
    
]