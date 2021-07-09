from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def redirHome(request):
    return redirect('/courses')

def homePage(request):
    context = {
        "courses": Course.objects.all(),
        "descriptions": Description.objects.all(),
    }
    return render(request, "homePage.html", context)

def createCourse(request):
    errors = Course.objects.courseValidator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/courses')
    desc = Description.objects.create(
        body = request.POST['description'],
        )
    Course.objects.create(
        name = request.POST['course_name'],
        description = desc
        )
    return redirect('/courses')

def destroyConfirmation(request, id):
    context = {
        "course":Course.objects.get(id=id),
        "description": Description.objects.get(id=id)
    }
    return render(request, 'destroyCourse.html', context)

def destroyCourse(request, id):
    felicia = Course.objects.get(id=id)
    felicia.delete()
    return redirect('/courses')