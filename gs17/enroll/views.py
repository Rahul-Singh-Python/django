from django.shortcuts import render
from enroll.models import Student
from . forms import StudentRegistartion
# Create your views here.

def studentinfo(request):
	stud = Student.objects.all()
	print('myoutput',stud)
	return render(request,'enroll/studentinfo.html',{'stu':stud})

# def showformdata(request):
# 	fm = StudentRegistartion()
# 	return render(request,'enroll/userregister.html',{'form':fm})

def showformdata(request):
	# fm = StudentRegistartion()
	# fm = StudentRegistartion(auto_id='some_%s')
	# fm = StudentRegistartion(auto_id=True)
	# fm = StudentRegistartion(auto_id=False)
	fm = StudentRegistartion(auto_id=True,label_suffix=' -',initial={'name':'Rahul','email':'rahul@gmail.com'})
	return render(request,'enroll/userregister.html',{'form':fm})