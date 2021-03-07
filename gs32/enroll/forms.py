from django import forms
from .models import user

class Student(forms.ModelForm):
	class Meta:
		model = user
		# fields=['name','email','password']
		# fields = '__all__'
		exclude=['name']