from django.contrib import admin

# Register your models here.

from .models import Employee, EmpProxy

class AdminEmployee(admin.ModelAdmin):
	list_display = ['ename', 'sal' , 'loc']

class AdminEmpProxy(admin.ModelAdmin):
	list_display = ['ename', 'sal' , 'loc']

admin.site.register(Employee, AdminEmployee)
admin.site.register(EmpProxy, AdminEmpProxy)