"""crud_fbvs_employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employeelist_view),
    path('create/', views.employeecreate_view),
    re_path('update/(?P<id>\d+)/$', views.employeeupdate_view),
    re_path('delete/(?P<id>\d+)/$', views.employeedelete_view),
]
