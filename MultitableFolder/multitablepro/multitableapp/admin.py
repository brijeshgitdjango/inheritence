from django.contrib import admin

# Register your models here.
from .models import Course, Student, Teacher


class AdminCourse(admin.ModelAdmin):
	list_display = ['cname', 'cfee']

class AdminStudent(admin.ModelAdmin):
	list_display = ['sname', 'sage', 'cname', 'cfee']

class AdminTeacher(admin.ModelAdmin):
	list_display = ['tname', 'temail', 'sname', 'sage', 'cname', 'cfee']

admin.site.register(Course, AdminCourse)
admin.site.register(Student, AdminStudent)
admin.site.register(Teacher, AdminTeacher)