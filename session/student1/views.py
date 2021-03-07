from django.shortcuts import render

# Create your views here.

def setsession(request):
	request.session['name'] = 'Rahul'
	request.session['lname'] = 'Singh'
	return render(request,'student1/setsession.html')


def getsession(request):
	name = request.session.get('name')
	keys = request.session.keys()
	items = request.session.items()
	# age = request.session.setdefault('age','26')
	# return render(request,'student1/getsession.html',{'name':name,'keys':keys,'items':items,'age':age})
	return render(request,'student1/getsession.html',{'name':name,'keys':keys,'items':items})



def delsession(request):
	request.session.flush()
	return render(request,'student1/delsession.html')