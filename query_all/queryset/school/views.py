from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
# Create your views here.

def home(request):
	# student_data = Student.objects.all()

	# student_data = Student.objects.filter(marks=85)
	
	# student_data = Student.objects.exclude(marks=85)

	# student_data = Student.objects.order_by('marks')
	# student_data = Student.objects.order_by('-marks')
	# student_data = Student.objects.order_by('?')
	# student_data = Student.objects.order_by('name')


	# student_data = Student.objects.order_by('id').reverse()
	# student_data = Student.objects.order_by('id').reverse()[0:5]


	# student_data = Student.objects.values()
	# student_data = Student.objects.values('name','city')


	# student_data = Student.objects.values_list()
	# student_data = Student.objects.values_list('id','name')
	# student_data = Student.objects.values_list('id','name',named=True)


	# student_data = Student.objects.using('default')

	# student_data = Student.objects.dates('pass_date','month')
	# student_data = Student.objects.dates('pass_date','year')
	# student_data = Student.objects.dates('pass_date','week')
	# student_data = Student.objects.dates('pass_date','day')



############## Second Table "Teacher" Started #############################

	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True)
	# student_data = qs2.union(qs1)


	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True)
	# student_data = qs2.union(qs1,all=True)



	# Agar qs3 bhi table ho aise kar sakte hai

	# student_data = qs2.union(qs1,qs3, all=True)


	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True)
	# student_data = qs2.intersection(qs1)


	# qs1 = Student.objects.values_list('id','name',named=True)
	# qs2 = Teacher.objects.values_list('id','name',named=True)
	# student_data = qs2.difference(qs1)


###################### AND OR operator ################################

	# student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=105)
	# student_data = Student.objects.filter(id=6,roll=105)
	# student_data = Student.objects.filter(Q(id=6) & Q(roll=105))

	student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=106)
	student_data = Student.objects.filter(Q(id=6) | Q(roll=106))




	print("Return",student_data)
	print()
	print("SQL Query :",student_data.query)
	return render(request,'school/home.html',{'students':student_data})