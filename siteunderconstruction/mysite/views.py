from django.shortcuts import render

# Create your views here.

def home(request):
	print("I am Home Page")
	return render(request,'mysite/home.html')

def about(request):
	print("I am About Page")
	return render(request,'mysite/about.html')