from django.shortcuts import render
from . forms import Student
# Create your views here.

def showstudent(request):
	if request.method == 'POST':
		fm = Student(request.POST)
		if fm.is_valid():
			print('Form Validat')
			print('Name :',fm.cleaned_data['name'])
			print('Email :',fm.cleaned_data['email'])
			print('Password :',fm.cleaned_data['password'])
			print('Rpassword :',fm.cleaned_data['rpassword'])
	else:
		fm = Student()
	return render(request,'enroll/showstudent.html',{'form':fm})
