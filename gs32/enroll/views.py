from django.shortcuts import render
from .forms import Student
# Create your views here.

def showformsdata(request):
	fm = Student()
	return render(request,'enroll/userregister.html',{'form':fm})