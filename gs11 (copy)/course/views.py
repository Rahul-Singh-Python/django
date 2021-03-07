from django.shortcuts import render

# Create your views here.

def learn_django(request):
	cname = 'Django'
	duration = '4 Months'
	seats = 10
	django_deatails = {'nm':cname,'du':duration,'st':seats}
	return render(request,'course/course1.html',django_deatails)

def learn_python(request):
	return render(request,'course/course2.html')