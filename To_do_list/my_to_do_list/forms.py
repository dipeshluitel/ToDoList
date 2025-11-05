from django import forms
from .models import To_do_list, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = To_do_list
        fields = ['listed']
        widgets = {
            'listed': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Enter Your Task'})
        }

class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email','password']