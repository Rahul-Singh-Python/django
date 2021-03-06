from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
# Create your views here.

class StudentCreateView(CreateView):
	model = Student
	# template_name = 'school/student.html'
	fields = ['name','email','password']
	# success_url = '/thanks/'

class ThanksTemplate(TemplateView):
	template_name = 'school/thanks.html'


class StudentDetailView(DetailView):
	model = Student