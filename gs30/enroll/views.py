from django.shortcuts import render

# Create your views here.

def home(request,check):
	return render(request,'enroll/home.html',{'ch':check})

# def show_details(request,my_id):
# 	student = {'id':my_id}
# 	return render(request,'enroll/show.html',student)


def show_details(request,my_id):
	if my_id == 1:
		student = {'id':my_id,'name':'Rohan'}
	if my_id == 2:
		student = {'id':my_id,'name':'Sonam'}
	if my_id == 3:
		student = {'id':my_id,'name':'Rahul'}
	if my_id == 4:
		student = {'id':my_id,'name':'Sandhya'}
	return render(request,'enroll/show.html',student)

def show_subdetails(request,my_id,my_subid):
	if my_id == 1 and my_subid == 5:
		student = {'id':my_id,'name':'Rohan','info':'sub Details'}
	if my_id == 2 and my_subid == 6:
		student = {'id':my_id,'name':'Sonam','info':'sub Details'}
	if my_id == 3 and my_subid == 7:
		student = {'id':my_id,'name':'Rahul','info':'sub Details'}
	if my_id == 4 and my_subid == 8:
		student = {'id':my_id,'name':'Sandhya','info':'sub Details'}
	return render(request,'enroll/show.html',student)