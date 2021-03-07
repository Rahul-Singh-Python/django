from django.shortcuts import render
from .models import Student
from django.db.models import Q
# Create your views here.

def home(request):
	# student_data = Student.objects.filter(Q(id=6) & Q(roll=106))
	# student_data = Student.objects.filter(Q(id=6) | Q(roll=107))
	student_data = Student.objects.filter(~Q(id=6))


	print("Student Data",student_data)
	print()
	print("Sql Query:",student_data.query)
	return render(request,'school/home.html',{'students':student_data})
