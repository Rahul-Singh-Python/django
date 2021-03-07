from django.shortcuts import render
from .models import ExamCenter,Student
# Create your views here.

def home(request):
	exam_center = ExamCenter.objects.all()
	student_data = Student.objects.all()

	print(exam_center)
	print(student_data)
	return render(request,'school/home.html',{'exams':exam_center,'students':student_data})