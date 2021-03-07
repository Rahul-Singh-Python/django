from django.urls import path
from .import views
urlpatterns = [
    path('student/',views.Student_form),
    path('teacher/',views.Teacher_form),
]