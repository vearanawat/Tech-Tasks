from django.urls import path
from prime_bin_api import views

urlpatterns=[
	path('',views.Final,name='Final'),
]