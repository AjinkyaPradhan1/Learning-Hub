from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from myadmin import models as myadmin_models
from studyapp import models as studyapp_models

from .import models

from django.db.models import Q

import time

media_url=settings.MEDIA_URL

# Create your views here.

def sessioncheckuser_middleware(get_response):
  def middleware(request):
    if request.path=='/user/' or request.path=='/user/ncertsolution/' or request.path=='/user/paper/' or request.path=='/user/practiceque/'  or request.path=='/user/videos/' or request.path=='/user/books/' or request.path=='/user/addbooks/' or request.path=='/user/subcatviewbooks/' or request.path=='/user/showSubject/' or request.path=='/user/editprofileuser/' or request.path=='/user/changepassworduser/' or request.path=='/user/updateDataUser/':
      if request.session['sunm']==None or request.session['srole']!='user':
        response=redirect('/login/')
      else:
        response=get_response(request)
    else:
      response=get_response(request)
    return response
  return middleware

def userhome(request):
    return render(request,"userhome.html",{"sunm":request.session['sunm']})

def ncertsolution(request):
    clist=myadmin_models.Class.objects.all()  
    return render(request,"ncertsolution.html",{"media_url":media_url,"clist":clist,"sunm":request.session['sunm']})

def paper(request):
    clist=myadmin_models.Class.objects.all()  
    return render(request,"paper.html",{"media_url":media_url,"clist":clist,"sunm":request.session['sunm']})

def practiceque(request):
    return render(request,"practiceque.html",{"media_url":media_url,"sunm":request.session['sunm']})

def videos(request):
    return render(request,"videos.html",{"media_url":media_url,"sunm":request.session['sunm']})



def editprofileuser(request):
  userDetails=studyapp_models.Register.objects.filter(username=request.session['sunm'])
  m,f="",""
  if userDetails[0].gender=="male":
    m="checked"
  else:
    f="checked"   
  return render(request,"editprofileuser.html",{"msg":"","sunm":request.session['sunm'],"userDetails":userDetails[0],"m":m,"f":f})

def updateDataUser(request):
  name=request.POST.get("name")
  email=request.POST.get("email")
  mobile=request.POST.get("mobile")
  address=request.POST.get("address")
  city=request.POST.get("city")
  pcode=request.POST.get("pcode")

  studyapp_models.Register.objects.filter(username=email).update(name=name,mobile=mobile,address=address,city=city,pcode=pcode)
   
  return redirect("/user/editprofileuser/") 

def changepassworduser(request):
  if request.method=="GET":
      return render(request,"changepassworduser.html",{"sunm":request.session['sunm'],"msg":""})
  else:
    oldpass=request.POST.get("oldpass")
    newpass=request.POST.get("newpass")
    confirmnewpass=request.POST.get("confirmnewpass")
    userDetails=studyapp_models.Register.objects.filter(username=request.session['sunm'],password=oldpass)

    if len(userDetails)>0:
      if newpass==confirmnewpass:
        studyapp_models.Register.objects.filter(username=request.session['sunm']).update(password=confirmnewpass)
        msg="Password Changed Successfully, Please Login Again!!!!"
      else:
        msg="New and Confirm New Password not matched!!!!!"
    else:
      msg="Invalid Old Password, Please try again!!!!!"
    return render(request,"changepassworduser.html",{"sunm":request.session['sunm'],"msg":msg})

def books(request):
  clist=myadmin_models.Class.objects.all()
  return render(request,"books.html",{"media_url":media_url,"clist":clist,"sunm":request.session['sunm']})

def subcatviewbooks(request):

  catnm=request.GET.get("catnm")
  sclist=myadmin_models.Subject.objects.filter(catnm=catnm)
  return render(request,"subcatviewbooks.html",{"media_url":media_url,"sclist":sclist,"catnm":catnm,"sunm":request.session['sunm']})

def addbooks(request):
  clist=myadmin_models.Class.objects.all()
  if request.method=="GET":
    return render(request,"addbooks.html",{"clist":clist,"sunm":request.session['sunm'],"msg":""})
  else:
    title=request.POST.get("title")
    catnm=request.POST.get("catnm")
    subcatnm=request.POST.get("subcatnm")
    baseprice=request.POST.get("baseprice")
    description=request.POST.get("description")
    author=request.POST.get("author")
    edition=request.POST.get("edition")
    publisher=request.POST.get("publisher")

    file1=request.FILES['file1']        
    fs=FileSystemStorage()
    file1_nm=fs.save(file1.name,file1)

    file2=request.FILES['file2']        
    fs=FileSystemStorage()
    file2_nm=fs.save(file2.name,file2)

    file3=request.FILES['file3']        
    fs=FileSystemStorage()
    file3_nm=fs.save(file3.name,file3)

    file4=request.FILES['file4']        
    fs=FileSystemStorage()
    file4_nm=fs.save(file4.name,file4)

    if request.POST.get('file2')==None:
      file2=request.FILES['file2']        
      fs=FileSystemStorage()
      file2_nm=fs.save(file2.name,file2)
    else:
      file2_nm="default.jpg"

    if request.POST.get('file3')==None:
      file3=request.FILES['file3']        
      fs=FileSystemStorage()
      file3_nm=fs.save(file3.name,file3)
    else:
      file3_nm="default.jpg"

    if request.POST.get('file4')==None:
      file4=request.FILES['file4']        
      fs=FileSystemStorage()
      file4_nm=fs.save(file4.name,file4)
    else:
      file4_nm="default.jpg" 
    uid=request.session['sunm']
    bstatus=0
    dt=time.asctime()
  
  p=models.Products(title=title,catnm=catnm,subcatnm=subcatnm,baseprice=baseprice,description=description,author=author,edition=edition,publisher=publisher,file1=file1_nm,file2=file2_nm,file3=file3_nm,file4=file4_nm,uid=uid,bstatus=bstatus,dt=dt)
  p.save() 
  return render(request,"addbooks.html",{"clist":clist,"sunm":request.session['sunm'],"msg":"Book to be sold added successfully!!!!"})

def showSubject(request):
  catnm=request.GET.get("cnm")
  sclist=myadmin_models.Subject.objects.filter(catnm=catnm)
  sclist_options="<option>Select Subject</option>"
  for row in sclist:
    sclist_options+=("<option>"+row.subcatnm+"</option>")
  return HttpResponse(sclist_options)


def viewbooksuser(request):
  paypalURL="https://www.sandbox.paypal.com/cgi-bin/webscr"
  paypalID="sb-8y7jv4990175@business.example.com"
  pDetails=models.Products.objects.filter(uid=request.session['sunm'])
  return render(request,"viewbooksuser.html",{"sunm":request.session['sunm'],"pDetails":pDetails,"media_url":media_url,"paypalURL":paypalURL,"paypalID":paypalID})


def payment(request):
  pid=request.GET.get('pid')
  price=request.GET.get('price')
  uid=request.GET.get('uid')
  dt=time.time()

  p=models.Payment(pid=int(pid),price=int(price),uid=uid,dt=dt)
  p.save()
    
  models.Products.objects.filter(pid=int(pid)).update(bstatus=1,dt=dt)
    
  return redirect("/user/viewbooksuser/")

def cancel(request):
  return render(request,"cancel.html",{'sunm':request.session['sunm']})


def viewbuybooks(request):
  scnm=request.GET.get("scnm")
  sunm=request.session["sunm"]
  pDetails=models.Products.objects.filter(~Q(uid=sunm),subcatnm=scnm)    
  return render(request,"viewbuybooks.html",{'media_url':media_url,'sunm':request.session['sunm'],'pDetails':pDetails})




