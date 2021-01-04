from django.shortcuts import render
from django.http import HttpResponse

#home page of requester app
def homeView(request):
    return render(request, 'requester/studenthome.html')#

