from django.shortcuts import render

# Create your views here.

def learn_django(request):
	return render(request,'course/course1.html',{'title':'Django','cname':'Learn Django'})

def learn_python(request):
	return render(request,'course/course2.html',{'title':'Python','cname':'Learn Python'})