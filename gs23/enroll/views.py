from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import Student
# Create your views here.
def thankyou(request):
	return render(request,'enroll/success.html')

def showstudent(request):
	if request.method == 'POST':
		fm = Student(request.POST)
		if fm.is_valid():
			print('Form Validated')
			name = fm.cleaned_data['name']
			email = fm.cleaned_data['email']
			password = fm.cleaned_data['password']
			print('Name : ',name)
			print('Email : ',email)
			print('Password :',password)
			return HttpResponseRedirect('/regi/success/')
			# return render(request,'enroll/success.html',{'nm':name})

			# OR

			# print('Name : ',fm.cleaned_data['name'])
			# print('Email :',fm.cleaned_data['email'])
			# print('Password :',fm.cleaned_data['password'])

	else:

		fm = Student()
	return render(request,'enroll/showstudent.html',{'form':fm})