
from django.urls import  path
from gsoi import views

urlpatterns = [

    path('', views.home, name='Home' ),
    path('contact/', views.contact, name='contact'),     
    
]
