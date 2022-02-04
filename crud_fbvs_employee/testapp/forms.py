from django import forms
from testapp.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
