from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees_django(request):
	# return HttpResponse("<h1>Fees Dajngo 200</h1>")
	return render(request,'fees1.html')

def fees_python(request):
	return render(request,'fees2.html')