from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from records.forms import ActivityForm
from .models import Activity, Field
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin

################ CREATE
class FieldCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('list-field')
    
class ActivityCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Activity
    fields = ['number', 'points', 'details', 'description', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('list-activity')
    
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
    
################ DELETE
@login_required
def FieldDelete(request, pk):
    context = {}
    field = Field.objects.get(id = pk)
    activity = Activity.objects.filter(field = field)
    if not activity:
        field.delete()
        return redirect('/campos/')
    else:
        context['message'] = "Não é possivel deletar esse campo. Existem atividade dependentes dele."
        context['url_path'] = "list-field"
        return render(request, 'records/error_message.html', context)

    
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
    