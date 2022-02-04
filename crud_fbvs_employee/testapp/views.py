from django.shortcuts import render,redirect
from testapp.models import *
from testapp.forms import *
from django.db.models import *

# Create your views here.
def employeelist_view(request):
    employee=Employee.objects.all().order_by('-esal')[1:]
    return render(request,'testapp/employeelist.html',{'employee':employee})

def employeecreate_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')
    return render(request,'testapp/employeecreate.html',{'form':form})

def employeeupdate_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/employeeupdate.html',{'employee':employee})


def employeedelete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect ('/')
