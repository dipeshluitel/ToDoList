from django import forms
from .models import To_do_list

class TaskForm(forms.ModelForm):
    class Meta:
        model = To_do_list
        fields = ['listed']
        widgets = {
            'listed': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Enter Your Task'})
        }