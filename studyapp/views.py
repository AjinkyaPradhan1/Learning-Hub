from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.conf import settings
from .import models
from .import emailAPI

from myadmin import models as myadmin_models

import time
dt=time.asctime()

def sessioncheck_middleware(get_response):
     def middleware(request):
          if request.path=='/login/':
               request.session['sunm']=None
               request.session['srole']=None
               response=get_response(request)
          else:
               response=get_response(request)
          return response
     return middleware


def home(request):
    return render(request,"home.html",{}) 

def about(request):
    return render(request,"about.html",{}) 

def service(request):
    return render(request,"service.html",{}) 

def contact(request):
    if request.method=="GET":
        return render(request,"contact.html",{}) 
    else:
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        message=request.POST.get("message")

        contactUserDetails=models.Contact.objects.filter(username=email)
        if len(contactUserDetails)>0:
            return render(request,"contact.html",{"msg":"You have sent 1 message. Only 1 message allowed per Email Id...."})
        else: 
            p=models.Contact(name=name,username=email,mobile=mobile,message=message,dt=dt)
            p.save()
            return render(request,"contact.html",{"msg":"Message Sent Successfully...."})

def register(request):
     stclist=myadmin_models.State.objects.all()
     if request.method=="GET":
        return render(request,"register.html",{'msg':'','stclist':stclist})
     else:
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        stcatnm=request.POST.get("stcatnm")
        city=request.POST.get("city")
        pcode=request.POST.get("pcode")
        gender=request.POST.get("gender")
        

        userDetails=models.Register.objects.filter(username=email)
        if len(userDetails)>0:
            return render(request,"register.html",{"msg":"User already exists please try again...."})
        else: 
            p=models.Register(name=name,username=email,password=password,mobile=mobile,address=address,city=city,stcatnm=stcatnm,pcode=pcode,gender=gender,status=0,role="user",dt=dt)
            p.save()
            emailAPI.sendEmail(email,password)
            return render(request,"register.html",{"msg":"User register successfully....", "stclist":stclist})

def showCity(request):
    stcatnm=request.GET.get("stcnm")
    stsclist=myadmin_models.City.objects.filter(stcatnm=stcatnm)
    stsclist_options="<option>Select SubCategory</option>"
    for row in stsclist:
        stsclist_options+=("<option>"+row.city+"</option>")
        
    return HttpResponse(stsclist_options)


def login(request):
    if request.method=="GET":
        return render(request,"login.html",{'msg':''})
    else:
        email=request.POST.get("email")
        password=request.POST.get("password")

        userDetails=models.Register.objects.filter(username=email,password=password,status=1)
        #print(userDetails)
        if request.method=="GET":
            return render(request,"login.html",{'msg':''})
        else:
            if len(userDetails)>0:
            
            #Configuration to store userdetails in session
                request.session['sunm']=userDetails[0].username
                request.session['srole']=userDetails[0].role

                if userDetails[0].role=="user":
                    return redirect("/user/")        
                else:
                    return redirect("/myadmin/")
            else:
                return render(request,"login.html",{'msg':'Invalid user please try again....'})     

             




             
        