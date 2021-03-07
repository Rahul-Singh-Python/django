from django.urls import path
from .import views

urlpatterns = [
	path('leandj',views.learn_django),
	path('leanpy',views.learn_python),
]
