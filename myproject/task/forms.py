from django import forms
from .models import User, Task


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'task_detail', 'task_type']