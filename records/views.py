from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from records.forms import ActivityForm
from .models import Activity, Field
from django.shortcuts import redirect

################ CREATE

class FieldCreate(CreateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('list-field')
    
class ActivityCreate(CreateView):
    model = Activity
    fields = ['number', 'points', 'details', 'description', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('list-activity')
    
################ UPDATE

class FieldUpdate(UpdateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form_update.html'
    success_url = reverse_lazy('list-field')
    
class ActivityUpdate(UpdateView):
    model = Activity
    # fields = ['number', 'points', 'details', 'description',  'field']
    form_class = ActivityForm
    template_name = 'records/form_update.html'
    success_url = reverse_lazy('list-activity')
    
################ DELETE
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
        
class ActivityDelete(DeleteView):
    model = Activity
    template_name = 'records/form_delete.html'
    success_url = reverse_lazy('index')

################ READ
class FieldList(ListView):
    model = Field
    template_name = 'records/lists/field.html'
    
class ActivityList(ListView):
    model = Activity
    template_name = 'records/lists/activity.html'
