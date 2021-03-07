from django.shortcuts import render
from .forms import Student,Teacher
# Create your views here.

def Student_form(request):
	if request.method == 'POST':
		fm=Student(request.POST)
		if fm.is_valid():
			fm.save()
	else:
		fm=Student()
	return render(request,'enroll/student.html',{'form':fm})


def Teacher_form(request):
	if request.method == 'POST':
		fm = Teacher(request.POST)
		if fm.is_valid():
			fm.save()
	else:
		fm = Teacher()
	return render(request,'enroll/teacher.html',{'form':fm})
