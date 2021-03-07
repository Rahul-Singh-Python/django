from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django import forms
from .forms import StudentForm
# Create your views here.

# class StudentCreateView(CreateView):
# 	model = Student
# 	fields = ['name','email','password']
# 	success_url = '/thanks/'

# 	def get_form(self):
# 		form = super().get_form()
# 		form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
# 		form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
# 		return form


# class StudentUpdateView(UpdateView):
# 	model = Student
# 	fields = ['name','email','password']
# 	success_url = '/thanksupdate/'


# 	def get_form(self):
# 		form = super().get_form()
# 		form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
# 		form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
# 		return form


class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = '/thanks/'


class StudentUpdateView(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'school/student_form.html'
	success_url = '/thanksupdate/'

# class StudentDeleteView(DeleteView):
# 	model = Student
# 	success_url = '/create/'

class StudentDeleteView(DeleteView):
	model = Student
	success_url = '/thanksdelete/'
	template_name = 'school/confirm_del.html'


class ThankTemplteView(TemplateView):
	template_name = 'school/thanks.html'

class ThankUpdateTemplteView(TemplateView):
	template_name = 'school/thanksupdate.html'


class ThankdeleteTemplteView(TemplateView):
	template_name = 'school/thanksdelete.html'