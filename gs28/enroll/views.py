from django.shortcuts import render
from . forms import Student
from .models import user
# Create your views here.

def showstudent(request):
	if request.method == 'POST':
		fm = Student(request.POST)
		if fm.is_valid():
			nm =fm.cleaned_data['name']
			em =fm.cleaned_data['email']
			pw =fm.cleaned_data['password']
			# reg = user(name=nm,email=em,password=pw) # Insert Data
			# reg = user(id=1,name=nm,email=em,password=pw) # Update Data
			# reg.save()
			reg = user(id=1) # Delete Data
			reg.delete()
	else:
		fm = Student()
	return render(request,'enroll/showstudent.html',{'form':fm})
