from django.shortcuts import render

# Create your views here.

def fees_django(request):
	return render(request,'fees/fees1.html',{'title':'Learn Django','cname':'Django','charge':3000})

def fees_python(request):
	return render(request,'fees/fees2.html')