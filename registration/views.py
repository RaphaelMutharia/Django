from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


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
    template = loader.get_template('courses')
    return HttpResponse(template.render())

@csrf_exempt
def addstudent(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

    obj1 = Student(username=username, password=password, email=email)
    obj1.save()
    return render(request, 'register.html')
