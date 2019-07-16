from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeCreationForm, EmployeeChangeForm
from .models import Employee

class EmployeeAdmin(UserAdmin):
    add_form    = EmployeeCreationForm
    form        = EmployeeChangeForm
    model       = Employee
    list_display = ['email' , 'username', 'age', 'is_staff',]

admin.site.register(Employee,EmployeeAdmin)