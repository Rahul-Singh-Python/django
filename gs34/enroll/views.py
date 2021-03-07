from django.shortcuts import render
from .forms import Student
from django.contrib import messages
# Create your views here.

# def regi(request):
# 	if request.method == 'POST':
# 		fm = Student(request.POST)
# 		if fm.is_valid():
# 			fm.save()
# 			# messages.add_message(request,messages.SUCCESS,'Your Account Has Been Created !!!')
# 			# messages.add_message(request,messages.INFO,'Your Account Has Been Created !!!')
# 			messages.info(request,'Now You Can login !!!')
# 			print(messages.get_level(request))
# 			messages.debug(request,'This is Debug !!!')
# 			messages.set_level(request,messages.DEBUG)
# 			messages.debug(request,'This is New Debug !!!')
# 			print(messages.get_level(request))

# 	else:
# 		fm=Student()
# 	return render(request,'enroll/userregistration.html',{'form':fm})




def regi(request):
	messages.info(request,'Now You Can Login !!!')
	messages.success(request,'Update Success !!!')
	messages.warning(request,'This is warning !!!')
	messages.error(request,'This is Error !!!')
	fm=Student()
	return render(request,'enroll/userregistration.html',{'form':fm})