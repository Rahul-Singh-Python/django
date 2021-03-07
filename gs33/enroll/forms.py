from django import forms
from .models import user

class Student(forms.ModelForm):
	class Meta:
		model=user
		fields=['student_name','email','password']


class Teacher(Student):
	class Meta(Student.Meta):
		fields=['teacher_name','email','password']
