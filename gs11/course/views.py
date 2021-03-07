from django.shortcuts import render
from datetime import datetime

# Create your views here.

def learn_django(request):
	return render(request,'course/course1.html',{'nm':'django is awesome','age':False,'cap':'ABC'})	

def learn_python(request):
	d = datetime.now()
	return render(request,'course/course2.html',{'dt':d})