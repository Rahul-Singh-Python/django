from django import forms

class Student(forms.Form):
	name = forms.CharField(error_messages={'required':'Enter Your Name'})
	email = forms.EmailField(error_messages={'required':'Enter Your Email'})
	password = forms.CharField(widget=forms.PasswordInput(),error_messages={'required':'Enter Your Password'})

	# def clean_name(self):
	# 	valname = self.cleaned_data['name']
	# 	if len(valname) < 4:
	# 		raise forms.ValidationError('Enter More then or equal 4 char')
	# 	return valname


	def clean(self):
		cleaned_data = super().clean()
		valname = self.cleaned_data['name']
		valemail = self.cleaned_data['email']

		if len(valname) < 4 :
			raise forms.ValidationError('Name should be more than or equal 4')
		if len(valemail) < 10:
			raise forms.ValidationError('Email shuld be more than of equal 10')
