from django import forms
from . models import user

class StudentRegistartion(forms.ModelForm):
	class Meta:
		model = user
		fields = ['name','email','password']
	