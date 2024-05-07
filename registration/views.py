from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Student
from .forms import CourseForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




from registration.models import Student

"""
def registration(request):
    return HttpResponse("Welcome to registration!")

def mypage(request):
    template = loader.get_template('registration')
    return HttpResponse(template.render())
"""
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())

@csrf_exempt
def addstudent(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

    obj1 = Student(username=username, password=password, email=email)
    obj1.save()


    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'dashboard.html', context)
def editstudent(request,id):
    data = Student.objects.get(id=id)
    context = {'data': data}
    return render(request, 'updatestudent.html', context)
def updatestudent(request, id):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
    editstudent = Student.objects.get(id=id)
    editstudent.username = username
    editstudent.email= email
    editstudent.password= password

    editstudent.save()
    return redirect('/dashboard')

def dashboard(request):
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'dashboard.html', context)

def deletestudent(request, id):
   deletestudent=Student.objects.get(id=id)
   deletestudent.delete()
   return redirect('/dashboard')

def create_course(request):
    if request.method == 'POST':
      form = CourseForm(request.POST)
      if form.is_valid():
        form.save()
        # Redirect to a success page
        return redirect('success')
    else:
      form = CourseForm()
    return render(request, 'create_course.html', {'form': form})