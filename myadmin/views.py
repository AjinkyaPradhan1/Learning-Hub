from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from studyapp import models as studyapp_model 
from .import models

# Create your views here.

def sessioncheckmyadmin_middleware(get_response):
  def middleware(request):
    if request.path=='/myadmin/' or request.path=='/myadmin/manageusers/' or request.path=='/myadmin/addclass/' or request.path=='/myadmin/addsubject/':
      if request.session['sunm']==None or request.session['srole']!='admin':
        response=redirect('/login/')
      else:
        response=get_response(request)
    else:
      response=get_response(request)
    return response
  return middleware


def adminhome(request):
    return render(request,"adminhome.html",{})

def manageusers(request):
    userDetails=studyapp_model.Register.objects.filter(role="user") 
    return render(request,"manageusers.html",{"userDetails":userDetails})

def manageuserstatus(request):
 s=request.GET.get("s")
 regid=request.GET.get("regid")          

 if s=="block":     
    studyapp_model.Register.objects.filter(regid=regid).update(status=0)     
 elif s=="verify":     
    studyapp_model.Register.objects.filter(regid=regid).update(status=1)
 else:   
    studyapp_model.Register.objects.filter(regid=regid).delete()      
 return	redirect('/myadmin/manageusers/') 


def addclass(request):
    if request.method=="GET":
        return render(request,"addclass.html",{"msg":""})
    else:
        catnm=request.POST.get("catnm")
        clist=models.Class.objects.filter(catnm=catnm)

        if len(clist)>0:
            return render(request,"addclass.html",{"msg":"Subject Already Exists, Please try again........."})
        else:
            caticon=request.FILES["caticon"]
            fs=FileSystemStorage()
            caticonnm=fs.save(caticon.name,caticon)
            p=models.Class(catnm=catnm,caticonnm=caticonnm)
            p.save()
            return render(request,"addclass.html",{"msg":"Subject Added Successfully....."})


def addsubject(request):
    clist=models.Class.objects.all()      
    if request.method=="GET":   
        return render(request,"addsubject.html",{"msg":"","clist":clist})
    else:
        catnm=request.POST.get("catnm")
        subcatnm=request.POST.get("subcatnm")
        sclist=models.Subject.objects.filter(subcatnm=subcatnm)
        if len(sclist)>0:
            return render(request,"addsubject.html",{"msg":"Subject already exists please try again.....","clist":clist})
        else:
            caticon=request.FILES["caticon"]
            fs=FileSystemStorage()
            subcaticonnm=fs.save(caticon.name,caticon)
            p=models.Subject(catnm=catnm,subcatnm=subcatnm,subcaticonnm=subcaticonnm)
            p.save()
            return render(request,"addsubject.html",{"msg":"Subject added successfully.....","clist":clist}) 


def addstate(request):
    if request.method=="GET":
        return render(request,"addstate.html",{"msg":""})  
    else:
        stcatnm=request.POST.get("stcatnm")
        stclist=models.State.objects.filter(stcatnm=stcatnm)

        if len(stclist)>0:
          return render(request,"addstate.html",{"msg":"State Already Added........."})
        else:
          p=models.State(stcatnm=stcatnm)
          p.save()
          return render(request,"addstate.html",{"msg":"State Added Successfully....."})


def addcity(request):
  stclist=models.State.objects.all()      
  if request.method=="GET":   
    return render(request,"addcity.html",{"msg":"","stclist":stclist})
  else:
    stcatnm=request.POST.get("stcatnm")
    city=request.POST.get("city")
    stsclist=models.City.objects.filter(city=city)
    if len(stsclist)>0:
      return render(request,"addcity.html",{"msg":"City Already Added.....","stclist":stclist})
    else:
      p=models.City(stcatnm=stcatnm,city=city)
      p.save()
      return render(request,"addcity.html",{"msg":"City added successfully.....","stclist":stclist})

        
    