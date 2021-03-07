from django.shortcuts import render
from .models import Student,proxyStudent
# Create your views here.
def home(request):
	# student_data = Student.objects.all()
	student_data = proxyStudent.objects.all()
	# student_data = proxyStudent.students.get_stu_roll_range(101,104)
	return render(request,'school/home.html',{'students':student_data})
