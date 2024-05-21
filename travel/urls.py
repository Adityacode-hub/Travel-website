from django.urls import path
from travel import views
urlpatterns = [
   path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/ ',views.contact,name='contact'),
    path('news/',views.news,name='news'),
    path('destinations/',views.destinations,name='destinations'),

]
