from django import forms

class StudentRegistartion(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	first_name=forms.CharField()
