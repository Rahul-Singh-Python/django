from django.shortcuts import render
from . forms import StudentRegistartion
from . models import user
# Create your views here.

# def showstudent(request):
# 	if request.method == 'POST':
# 		fm = StudentRegistartion(request.POST)
# 		if fm.is_valid():
# 			nm =fm.cleaned_data['name']
# 			em =fm.cleaned_data['email']
# 			pw =fm.cleaned_data['password']
# 			reg = user(name=nm,email=em,password=pw) #Insert Data
# 			# reg = user(id=1,name=nm,email=em,password=pw) # Update Data
# 			reg.save()
# 			# reg = user(id=1) # Delete Data
# 			# reg.delete()
# 	else:
# 		fm = StudentRegistartion()
# 	return render(request,'enroll/showstudent.html',{'form':fm})






def showstudent(request):
	if request.method == 'POST':
		pi = user.objects.get(pk=3)
		fm = StudentRegistartion(request.POST,instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		fm = StudentRegistartion()
	return render(request,'enroll/showstudent.html',{'form':fm})
