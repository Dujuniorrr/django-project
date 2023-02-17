from django import forms
from .models import Field, Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['field'] = forms.ModelChoiceField(
            queryset=Field.objects.all())