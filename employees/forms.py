from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Employee

class EmployeeCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Employee
        fields = ('username' , 'email' , 'age',)

class EmployeeChangeForm(UserChangeForm):

    class Meta:
        model = Employee
        fields = ('username' , 'email' , 'age',)