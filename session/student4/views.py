from django.shortcuts import render

# Create your views here.

def setsession(request):
	request.session['name'] = 'Rahul'
	return render(request,'student2/setsession.html')


def getsession(request):
	name = request.session['name']
	return render(request,'student2/getsession.html',{'name':name})



def delsession(request):
	request.session.flush()
	request.session.clear_expired()
	return render(request,'student2/delsession.html')