from django.urls import path
from .import views

urlpatterns = [
	path('register/',views.showstudent),
	path('success/',views.thankyou),
]