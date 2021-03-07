from django.shortcuts import render
# Create your views here.

def home(request):
	return render(request,'student/course.html')


def contact(request):
	return render(request,'student/contact.html')

