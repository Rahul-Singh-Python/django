from django.shortcuts import render
from .models import Student
from datetime import date,time
# Create your views here.

def home(request):
	student_data = Student.objects.all()

	# student_data = Student.objects.filter(name__exact='Rahul')
	# student_data = Student.objects.filter(name__iexact='rahul')


	# student_data = Student.objects.filter(name__contains='u')
	# student_data = Student.objects.filter(name__icontains='U')
	

	# student_data = Student.objects.filter(id__in=[1,5,7])
	# student_data = Student.objects.filter(marks__in=[75])
	# student_data = Student.objects.filter(marks__in=[85,75])
	# student_data = Student.objects.filter(marks__gt=70)
	# student_data = Student.objects.filter(marks__gte=75)
	# student_data = Student.objects.filter(marks__lt=75)
	# student_data = Student.objects.filter(marks__lte=75)

	# student_data = Student.objects.filter(name__startswith='s')
	# student_data = Student.objects.filter(name__istartswith='S')
	# student_data = Student.objects.filter(name__endswith='a')
	# student_data = Student.objects.filter(name__iendswith='A')

	# student_data = Student.objects.filter(passdate__range=('2020-02-15','2020-09-08'))
	# student_data = Student.objects.filter(admdatetime__date=date(2020,9,1))
	# student_data = Student.objects.filter(admdatetime__date__gt=date(2020,9,5))
	# student_data = Student.objects.filter(passdate__year=2019)
	# student_data = Student.objects.filter(passdate__year__gt=2019)
	# student_data = Student.objects.filter(passdate__year__gte=2019)


	# student_data = Student.objects.filter(passdate__month=9)
	# student_data = Student.objects.filter(passdate__month__gt=5)
	# student_data = Student.objects.filter(passdate__month__gte=6)


	# student_data = Student.objects.filter(passdate__day=7)
	# student_data = Student.objects.filter(passdate__day__gt=7)
	# student_data = Student.objects.filter(passdate__day__gte=7)



	# student_data = Student.objects.filter(passdate__week=14)
	# student_data = Student.objects.filter(passdate__week__gt=14)


	# student_data = Student.objects.filter(passdate__week_day=1) # sunday
	# student_data = Student.objects.filter(passdate__week_day=2) # monday
	# student_data = Student.objects.filter(passdate__week_day=3) # tuesday
	# student_data = Student.objects.filter(passdate__week_day=4) # wednesday
	# student_data = Student.objects.filter(passdate__week_day=5) # thrusday
	# student_data = Student.objects.filter(passdate__week_day=6) # friday
	# student_data = Student.objects.filter(passdate__week_day=7) # saturday


	# student_data = Student.objects.filter(passdate__week_day__gt=3) 
	# student_data = Student.objects.filter(passdate__week_day__gte=3) 

	
	# student_data = Student.objects.filter(passdate__quarter=1) # jan,feb,mar 
	# student_data = Student.objects.filter(passdate__quarter=2) # apr,may,jun
	# student_data = Student.objects.filter(passdate__quarter=3) # jul,aug,sep
	# student_data = Student.objects.filter(passdate__quarter=4) # oct,nov,dec


	# student_data = Student.objects.filter(admdatetime__time__gt=time(6,00))
	# student_data = Student.objects.filter(admdatetime__time__gt=time(10,25))
	# student_data = Student.objects.filter(admdatetime__hour__gt=1)
	# student_data = Student.objects.filter(admdatetime__minute__gt=26)
	# student_data = Student.objects.filter(admdatetime__second__gt=10)
	# student_data = Student.objects.filter(admdatetime__second__lt=10)


	# student_data = Student.objects.filter(roll__isnull=True)
	# student_data = Student.objects.filter(roll__isnull=False)









	print("Student Data",student_data)
	print()
	print("Sql Query:",student_data.query)
	return render(request,'school/home.html',{'students':student_data})
