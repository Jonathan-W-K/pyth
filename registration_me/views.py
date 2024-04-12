from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        # Logic to process registration form data
        return HttpResponse("Registration successful!")
    else:
        # Render registration form template
        return render(request, 'registration/register.html')

def login(request):
    if request.method == 'POST':
        username = request
        password =""
        return HttpResponse("Login successful!")
    else:
        return render(request, 'login/login.html')

def home(request):
    if request.method == 'POST':
        return "click here" <a href="home.html">here</a>
