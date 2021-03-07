from django import forms
from . models import user

class StudentRegistartion(forms.ModelForm):
	name = forms.CharField(max_length=50,required=False)
	class Meta:
		model = user
		fields = ['name','email','password']
		labels = {'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
		error_messages={
		'name':{'required':'Enter Your Name'},
		'password':{'required':'Enter Your Password'}
		}
		widgets={
		'password':forms.PasswordInput,
		'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name'})
		}