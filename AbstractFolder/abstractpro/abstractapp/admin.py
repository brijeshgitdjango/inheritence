from django.contrib import admin

# Register your models here.

from .models import Student, Employee

class AdminStudent(admin.ModelAdmin):
	list_display = ['name', 'loc', 'fee']

class AdminEmployee(admin.ModelAdmin):
	list_display = ['name' ,'loc', 'sal']

admin.site.register(Student, AdminStudent)
admin.site.register(Employee, AdminEmployee)