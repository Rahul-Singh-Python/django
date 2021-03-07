from django.shortcuts import render

# Create your views here.

def setsession(request):
	request.session['name'] = 'Rahul'
	request.session.set_expiry(5)
	return render(request,'student2/setsession.html')


def getsession(request):
	name = request.session['name']
	print(request.session.get_session_cookie_age())
	print(request.session.get_expiry_age())
	print(request.session.get_expiry_date())
	print(request.session.get_expire_at_browser_close())
	return render(request,'student2/getsession.html',{'name':name})



def delsession(request):
	request.session.flush()
	request.session.clear_expired()
	return render(request,'student2/delsession.html')