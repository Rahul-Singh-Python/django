from django.core import validators
from django import forms

def starts_with_s(value):
	if value[0] != 's':
		raise forms.ValidationError('Name should be start with s')

class Student(forms.Form):
	# name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
	name = forms.CharField(validators=[starts_with_s])
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())