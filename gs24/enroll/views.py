from django.shortcuts import render
from . forms import Student
# Create your views here.

def Showdata(request):
	if request.method == 'POST':
		fm = Student(request.POST)
		if fm.is_valid():
			print('is Valid')
			print('Name : ',fm.cleaned_data['name'])
			print('Roll : ',fm.cleaned_data['roll'])
			print('Price : ',fm.cleaned_data['price'])
			print('Rate : ',fm.cleaned_data['rate'])
			print('Comment : ',fm.cleaned_data['comment'])
			print('email : ',fm.cleaned_data['email'])
			print('website : ',fm.cleaned_data['website'])
			print('password : ',fm.cleaned_data['password'])
			print('description : ',fm.cleaned_data['description'])
			print('feedback : ',fm.cleaned_data['feedback'])
			print('notes : ',fm.cleaned_data['notes'])
			print('Agree : ',fm.cleaned_data['agree'])
	else:
		fm = Student()
	return render(request,'enroll/showdata.html',{'form':fm})
