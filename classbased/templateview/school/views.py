from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# class HomeTemplateView(TemplateView):
# 	template_name = 'school/home.html'



class HomeTemplateView(TemplateView):
	template_name = 'school/home.html'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		# context['name'] = 'Rahul'
		# context['roll'] = 101
		
		context = {'name':'Rahul','roll':101}
		print(context)
		print(kwargs)
		
		return context