from django.shortcuts import render
from django.http import HttpResponse
from register.html import recordForm
from .models import Record


def add_record(request):
    if request.method == 'POST':
        studentname = request.POST.get('studentname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        age = request.POST.get('age')

        obj = Record(studentname=studentname, email=email, password=password, phone=phone, age=age)
        obj.save()
        data = recordForm()
        context = {'data': data}
        return HttpResponse('Record added successfully!')

def edit_record(request,id):
    data = Record.objects.get(id=id)
    context = {'data': data}
    return render(request, 'register.html',context)

    records = Record.objects.all()  # Retrieve all records
    return render(request, 'register.html', {'form': form, 'records': records})
