from django.urls import path
from . import views

urlpatterns=[
	path('',views.add_show,name='addandshow'),
	path('<int:id>/',views.update_data,name='updatedata'),
	path('delete/<int:id>/',views.deletedata,name='deletedata'),
]