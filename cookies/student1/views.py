from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.

def setcookie(request):
	response = render(request,'student1/setcookie.html')
	# response.set_cookie('name','Rahul',max_age=60)
	response.set_signed_cookie('name','Sonam',salt='nm', expires=datetime.utcnow()+timedelta(days=2))
	return response


def getcookie(request):
	# name = request.get_signed_cookie('name',salt='nm')
	name = request.get_signed_cookie('name',salt='nmm',default='Guest')
	return render(request,'student1/getcookie.html',{'name':name})


def delcookie(request):
	response = render(request,'student1/delcookie.html')
	response.delete_cookie('name')
	return response
