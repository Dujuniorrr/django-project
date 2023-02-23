from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UserForm
from django.shortcuts import get_object_or_404
from .models import Profile

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
        Profile.objects.create(user=self.object)
        return url
    
class UpdateProfile(UpdateView):
    template_name = "users/update_form.html"
    model = Profile
    fields = ["complet_name", "cpf", "phone"]
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Profile, user = self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['header'] = 'Editar Perfil'
        return context