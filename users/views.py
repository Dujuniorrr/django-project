from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UserForm
from django.shortcuts import get_object_or_404

class UserCreate(CreateView):
    template_name = 'records/form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['header'] = 'Cadastro de Usuário'
        return context
    
    def form_valid(self, form):
        group = get_object_or_404(Group, name='Docente')
        url = super().form_valid(form)
        self.object.groups.add(group)
        self.object.save()
        return url