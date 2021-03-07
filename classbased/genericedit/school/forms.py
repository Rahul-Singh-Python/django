from django import forms

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	msg = forms.CharField(widget=forms.Textarea)


class FeedBackForm(forms.Form):
	your_name = forms.CharField()
	your_email = forms.EmailField()
	your_msg = forms.CharField(widget=forms.Textarea)