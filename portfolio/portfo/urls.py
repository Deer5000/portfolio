from django.urls import path

from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name ='contact'),
    path('greet/<str:name>/', views.greet_by_name)
]