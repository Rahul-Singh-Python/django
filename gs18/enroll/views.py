from django.shortcuts import render
from . forms import StudentRegistration
# Create your views here.

def showregister(request):
	fm = StudentRegistration()
	# fm.order_fields(field_order=['First_name','email','name'])
	return render(request,'enroll/studentregister.html',{'form':fm})
