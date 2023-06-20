from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def admin(request):
    return render(request,'admin_log.html')

def login_admin(request):

    return render(request,'index.html')
              
            #   if request.method=='POST':
            #         username = request.POST['username']
            #         password = request.POST['password']
                    
            #         user  = auth.authenticate(username=username,password=password)

            #         if user is not None:
            #               auth.login(request,user)
            #               return HttpResponseRedirect(request,"admin_log.html")
            #   else:
                #    return HttpResponseRedirect('index.html')
def dashboard(request):
    return render(request,'index.html')


def driverspage(request):
    return render(request,'pages/tables.html')

def requests(request):
    return render(request,'pages/billing.html')

def notification(request):
    return render(request,'pages/notifications.html')

