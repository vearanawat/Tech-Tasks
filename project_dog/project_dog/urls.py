from django.urls import path
from dog_breeds_api import views

urlpatterns = [
    path('breeds/', views.fetch, name='fetch'),
    path('random/<str:breed_name>/', views.random, name='random'),
]
