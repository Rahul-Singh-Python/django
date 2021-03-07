from django.shortcuts import render,HttpResponse

# Create your views here.

def setsession(request):
	request.session['name'] = 'Rahul'
	return render(request,'expire/setsession.html')


def getsession(request):
	if 'name' in request.session:
		name = request.session['name']
		request.session.modified = True
		return render(request,'expire/getsession.html',{'name':name})
	else:
		return HttpResponse('Your Session has Expire....')



def delsession(request):
	request.session.flush()
	request.session.clear_expired()
	return render(request,'expire/delsession.html')