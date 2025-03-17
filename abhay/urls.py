from django.urls import path
from . import views
# from .views import UploadView
urlpatterns = [
    path('',views.base,name='base'),
    # path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('skill/',views.skill,name='skill'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('comment/',views.comment,name='comment'),
    # path('<int:comment>/',views.comment,name='comment')
    path('upload/',views.upload,name='upload'),
    path('login/',views.login,name="login"),
]
