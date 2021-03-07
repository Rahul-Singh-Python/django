from django import forms

class sturegister(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	mobile = forms.IntegerField()