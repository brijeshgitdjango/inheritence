from django.contrib import admin

# Register your models here.
from .models import ModelFirst, ModelSecond, ModelMain

class AdminModelFirst(admin.ModelAdmin):
	list_display = ['mf_id','mf_name']

class AdminModelSecond(admin.ModelAdmin):
	list_display = ['ms_id','ms_name']

class AdminModelMain(admin.ModelAdmin):
	list_display = ['mm_name','ms_name','mf_name']


admin.site.register(ModelFirst, AdminModelFirst)
admin.site.register(ModelSecond, AdminModelSecond)
admin.site.register(ModelMain, AdminModelMain)