from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_django(request):
	return HttpResponse("Fees Django 3000")

def fees_python(request):
	return HttpResponse("Fees Python 5000")