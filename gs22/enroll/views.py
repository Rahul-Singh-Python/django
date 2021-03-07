from django.shortcuts import render
from .forms import Student
# Create your views here.

def showstudent(request):
	fm = Student()
	return render(request,'enroll/showstudent.html',{'form':fm})
