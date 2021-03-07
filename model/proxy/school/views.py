from django.shortcuts import render
from .models import ExamCenter,myExamCenter
# Create your views here.

def home(request):
	exam_center = ExamCenter.objects.all()
	my_exam_center = myExamCenter.objects.all()
	return render(request,'school/home.html',{'exams':exam_center,'myexams':my_exam_center})