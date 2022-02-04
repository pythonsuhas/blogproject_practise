from django.contrib import admin
from testapp.models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['ename','eno','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)    
