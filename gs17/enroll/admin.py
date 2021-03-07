from django.contrib import admin
from . models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display =('id','studid','stuname','stuemail','stupass','comment')

# admin.site.register(Student,StudentAdmin)