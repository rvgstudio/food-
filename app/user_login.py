from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
# from .models import Profile
# from app.emailbackend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')

        if password != con_password:
            messages.error(request,"Password are not same ")
            return redirect("register")

        user = User.objects.create_user(name,email,password)
        user.save()
        var = authenticate(request,username=name,email=email,password=password)
        if var is not None:
            login(request,var)
            return redirect("home")
    return render(request,'register.html')

def loginpage(request):
   if request.method == "POST":
    name = request.POST.get("name")
    password = request.POST.get("password")
    con_password = request.POST.get("con_password")
    if password != con_password:
        messages.error(request,"password are not match")
        return redirect("loginnpage")
    var = authenticate(request,username=name,password=password)
    if var is not None:
        login(request,var)
        return redirect("home")
   return render(request,'loginpage.html')


@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def profile_update(request):
   if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user_id = request.user.id

        user = User.objects.get(id = user_id)


        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
    
        user.save()
        return redirect("profile")
   return render(request, 'profile.html')