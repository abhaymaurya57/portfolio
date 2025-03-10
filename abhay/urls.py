from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    # path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('skill/',views.skill,name='skill'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    

]
