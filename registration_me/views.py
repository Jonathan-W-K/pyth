from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        # Logic to process registration form data
        return HttpResponse("Registration successful!")
    else:
        # Render registration form template
        return render(request, 'registration/register.html')

