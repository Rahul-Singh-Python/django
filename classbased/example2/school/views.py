from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.base import TemplateView
# Create your views here.

class StudentCreateView(CreateView):
	model = Student
	fields = ['name','email','password']
	success_url = '/thanks/'

class ThankTemplteView(TemplateView):
	template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
	model = Student
	fields = ['name','email','password']
	success_url = '/thanksupdate/'

class ThankUpdateTemplteView(TemplateView):
	template_name = 'school/thanksupdate.html'