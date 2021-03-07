from django.shortcuts import render
from .forms import studentregister
# Create your views here.

def showstudent(request):
	fm = studentregister()
	return render(request,'enroll/showstudent.html',{'form':fm})
