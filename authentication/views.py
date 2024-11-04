from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User

def user_login(request):
    context={
            "error":""
        }
    if request.method== "POST":
        
        user=authenticate(username=request.POST["Username"], password=request.POST["Password"])
        if user is not None:
            login(request,user)
            return redirect('/Internlink')
        else:
            context={
                "error":"Invalid Username or Password"
            }
            return render(request,'login.html',context)
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/')

def adduser(request):
    context={
        "error":""
    }
    if request.method=="POST":
        user_check = User.objects.filter(username=request.POST['userid'])


        if len(user_check)>0:
            context={
                "error":"User Already Exists"
            }
            return render (request,'adduser.html',context)
        
        else:
            new_user=User(username=request.POST["userid"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], department=request.POST["userdept"])

            new_user.set_password(request.POST["password"])
            new_user.save()
            return redirect('/Internlink')
    return render(request,"adduser.html",context)