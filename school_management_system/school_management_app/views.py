
from django.contrib.auth import login,logout
from django.contrib import  messages
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.urls import reverse
from school_management_app.EmailBackEnd import EmailBackEnd

# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def showLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h1> Method Not Allowed</h1>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == 1:
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == 2:
                return HttpResponseRedirect(reverse("staff_home"))
                #return HttpResponse("Staff login"+str(user.user_type))
            else:
                return HttpResponseRedirect(reverse("staff_home"))
              #  return HttpResponse("Student login"+str(user.user_type))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")
def GetUserdetails(request):
    if request.user!=None:
        return HttpResponse("User :"+request.user.email+"usertype :"+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")