from django.urls import path
from . import views

urlpatterns = [
    #path('registration/', views.registration, name='registration')
    path('login/', views.login, name='myloginpage'),
    path('home/', views.home, name='myhomepage'),
    path('about/', views.about, name='myaboutpage'),
    path('courses/', views.courses, name='mycourses'),
    path('register/', views.register, name='myregister')

]