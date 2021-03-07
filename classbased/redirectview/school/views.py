from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.


class GithubRedirectView(RedirectView):
	url = 'https://github.com/Rahul-gvp'



class GeekRedirectView(RedirectView):
	pattern_name = 'mindex'
	permanent = True
	query_string = True


	def get_redirect_url(self,*args,**kwargs):
		print(kwargs)
		kwargs['pk'] = 16
		return super().get_redirect_url(*args,**kwargs)
