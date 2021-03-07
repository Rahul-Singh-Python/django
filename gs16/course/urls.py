from django.urls import path
from . import views

urlpatterns = [
    path('django/',views.course_info,name='course1'),
]