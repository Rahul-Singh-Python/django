from django import forms

class studentregister(forms.Form):
	# name = forms.CharField(label='Your Name',label_suffix=' ',initial='sonam')
	# name = forms.CharField(label='Your Name',label_suffix=' ',
	# 	required=False,initial='sonam',disabled=True,help_text='Limit 20 Char')

	# name = forms.CharField(widget=forms.PasswordInput())
	# name = forms.CharField(widget=forms.HiddenInput())
	# name = forms.CharField(widget=forms.Textarea)
	# name = forms.CharField(widget=forms.CheckboxInput)
	# name = forms.CharField(widget=forms.FileInput)
	# name = forms.CharField(widget=forms.TextInput(attrs('class':'somecss1')))
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1','id':'uniqueid'}))
