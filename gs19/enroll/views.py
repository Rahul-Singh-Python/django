from django.shortcuts import render
from .forms import sturegister
# Create your views here.

def showStudent(request):
	fm = sturegister()
	return render(request,'enroll/register.html',{'form':fm})