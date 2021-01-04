from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#home page of requester app
@login_required(login_url='')
def homeView(request):
    if request.user.groups.filter(name='Lecturer').exists():
        return render(request, 'requester/lecturerhome.html')#if user is a lecturer render lecturer home page
    elif request.user.groups.filter(name='Student').exists():
        return render(request, 'requester/studenthome.html')#if user is a lecturer render lecturer home page

