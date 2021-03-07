from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def home(request):
	# student_data = Student.objects.get(pk=5)
	# student_data = Student.objects.get(id=5)

	# student_data = Student.objects.first()
	# student_data = Student.objects.order_by('name').first()
	
	# student_data = Student.objects.last()
	# student_data = Student.objects.order_by('name').last()

	# student_data = Student.objects.latest('pass_date')

	# student_data = Student.objects.earliest('pass_date')
	

	# student_data = Student.objects.all()
	# print(student_data.exists())


	# student_data = Student.objects.all()
	# one_data = Student.objects.get(pk=1)
	# print(student_data.filter(pk=one_data.pk).exists())




################## CREATE , DELETE, UPDATE Method ################################

	# student_data = Student.objects.create(name='Aachal',roll=113,city='Surat',marks=60,pass_date='2020-5-4')
	

	# student_data,created = Student.objects.get_or_create(name='Archna',roll=114,city='Surat',marks=60,pass_date='2020-5-4')
	# print(created)


	# student_data = Student.objects.filter(id=12).update(name='Sonam',marks=35)
	# student_data = Student.objects.filter(marks=60).update(city='Pass')


	# student_data,created = Student.objects.update_or_create(id=14,name='Archna',defaults={'name':'Sameer'})
	# print(created)


	# objs = [
	# Student(name='Sunny',roll=115,city='Ahmedabad',marks=70,pass_date='2020-3-5'),
	# Student(name='Anash',roll=116,city='Surat',marks=85,pass_date='2020-4-25'),
	# Student(name='Rohit',roll=117,city='Modasa',marks=70,pass_date='2020-1-1'),
	# Student(name='Bhavin',roll=118,city='Patna',marks=65,pass_date='2020-3-15'),
	# ]
	# student_data = Student.objects.bulk_create(objs)

	
	# all_student_data = Student.objects.all()
	# for stu in all_student_data:
	# 	stu.city = 'Dhanbad'
	# student_data = Student.objects.bulk_update(all_student_data,['city'])


	# student_data = Student.objects.in_bulk([2,3])
	# print(student_data[3].name)

	# student_data = Student.objects.in_bulk([])
	
	# student_data = Student.objects.in_bulk()
	


	# student_data = Student.objects.get(pk=15).delete()
	# student_data = Student.objects.filter(marks=35).delete()
	# student_data = Teacher.objects.all().delete()


	# student_data = Student.objects.all()
	# print(student_data.count())


	student_data =Student.objects.all()
	print(student_data.explain())





	print("Return :",student_data)
	return render(request,'school/home.html',{'students':student_data})