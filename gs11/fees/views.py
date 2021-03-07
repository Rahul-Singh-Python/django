from django.shortcuts import render

# Create your views here.

def fees_django(request):
	return render(request,'fees/fees1.html',{'p1':56.24312,'p2':50.000,'p3':56.37000})

def fees_python(request):
	return render(request,'fees/fees2.html',{'nm':'Django','age':False,'aa':True,'st':5})
	# return render(request,'fees/fees2.html',{'nm':'Django'})
	# return render(request,'fees/fees2.html',{'st':5})
	# return render(request,'fees/fees2.html')

def loop_python(request):
	student = {'names':['Rahul','Sonam','Raj','Anu']}
	return render(request,'fees/looppython.html',student)

# def loop_python2(request):
# 	stu = {'stu1':{'name':'Rahul','roll':101},
# 			'stu2':{'name':'Sonam','roll':102},
# 			'stu3':{'name':'Raj','roll':103},
# 			'stu4':{'name':'Anu','roll':104},
# 	}
# 	students = {'student':stu}
# 	return render(request,'fees/loop_python2.html',students)

# def loop_python2(request):
# 	data = {'name':'Rahul','roll':101}
# 	return render(request,'fees/loop_python2.html',{'data':data})


def loop_python2(request):
	data = {'stu1':{'name':'Rahul','roll':101},
			'stu2':{'name':'Sonam','roll':102},
			'stu3':{'name':'Raj','roll':103},
			'stu4':{'name':'Anu','roll':104},
	}
	return render(request,'fees/loop_python2.html',{'data':data})