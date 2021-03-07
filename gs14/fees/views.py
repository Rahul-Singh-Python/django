from django.shortcuts import render

# Create your views here.

def fees_django(request):
	return render(request,'fees/fees1.html',{'title':'Django','cname':'Learn Django','charge':10000})

def fees_python(request):
	return render(request,'fees/fees2.html',{'title':'Python','cname':'Learn Python','charge':8000})

# Create your views here.
