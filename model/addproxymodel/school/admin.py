from django.contrib import admin
from .models import Student,proxyStudent
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id','name','roll']


@admin.register(proxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
	list_display = ['id','name','roll']