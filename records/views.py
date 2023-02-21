from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from records.forms import ActivityForm
from .models import Activity, Field
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

################ CREATE
class FieldCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('list-field')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['header'] = 'Cadastro de Campos'
        return context
        
    
class ActivityCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Activity
    fields = ['number', 'points', 'details', 'description', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('list-activity')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['header'] = 'Cadastro de Atividades'
        return context
    
################ UPDATE

class FieldUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form_update.html'
    success_url = reverse_lazy('list-field')
    
class ActivityUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Activity
    # fields = ['number', 'points', 'details', 'description',  'field']
    form_class = ActivityForm
    template_name = 'records/form_update.html'
    success_url = reverse_lazy('list-activity')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Activity, pk = self.kwargs['pk'], user = self.request.user)
        return self.object
    

class FieldDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Field
    template_name = 'records/form_delete.html'
    success_url = reverse_lazy('list-field')
    error_url = reverse_lazy('error-message')

    def form_valid(self, form):
        success_url = self.get_success_url()
        error_url = self.error_url.format(**self.object.__dict__)
        field = Field.objects.get(id = self.object.pk)
        activity = Activity.objects.filter(field = field)
        if not activity:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            context = {}
            context['message'] = "Não é possivel deletar esse campo. Existem atividade dependentes dele."
            context['url_path'] = "list-field"
            ErrorMessage.context = context
            return HttpResponseRedirect(error_url)
    
class ActivityDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Activity
    template_name = 'records/form_delete.html'
    success_url = reverse_lazy('index')
    

################ READ
class FieldList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Field
    template_name = 'records/lists/field.html'
    
class ActivityList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Activity
    template_name = 'records/lists/activity.html'
    
    def get_queryset(self):
        self.object_list = Activity.objects.filter(user = self.request.user)
        return self.object_list
    
####################### ERRO

class ErrorMessage(LoginRequiredMixin, TemplateView):
    context = {}
    context['message'] = 'Página de erro.'
    context['url_path'] = 'index'
    login_url = reverse_lazy('login')
    template_name = 'records/error_message.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context = self.context
        return context