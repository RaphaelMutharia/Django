from django.urls import path
from . import views
from registration import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('registration/', views.registration, name='registration')
    path('login/', views.login, name='myloginpage'),
    path('', views.home, name='myhomepage'),
    path('about/', views.about, name='myaboutpage'),
    path('courses/', views.courses, name='mycourses'),
    path('register/', views.register, name='myregister'),
    path('addstudent', views.addstudent, name='addstudent'),

    path('addstudent', views.addstudent, name='addingstudent'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deletestudent/<id>', views.deletestudent, name='deletestudent'),
    path('editstudent/<id>', views.editstudent, name='editingstudent'),
    path('updatestudent/<id>', views.updatestudent, name='updatingstudent'),
    path('create/', views.create_course, name='create_course'),
]
urlpatterns = format_suffix_patterns(urlpatterns)