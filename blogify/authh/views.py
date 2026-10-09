from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup(request):
    if request.method == "POST":
        f = request.POST["f_name"]
        l = request.POST["l_name"]
        e = request.POST["em"]
        u = request.POST["u_name"]
        p = request.POST["passw"]
        cp = request.POST["c_p"]
        
        if User.objects.filter(username = u).exists():
            messages.warning(request, "please choose another unique username! this is already exists.")
            return redirect("signup")
    
        
        if p != cp:
            messages.warning(request, "Password are't macth..!")
            return redirect("signup")
        
        c_user = User.objects.create_user(
            first_name = f, last_name = l, username = u, email = e,
            password = p
        )
        
        c_user.save()
        
        messages.success(request, "User registration scessfully done...! please login to continue..")
        
        return redirect("login")
        
        
        
    
    return render(request, "auth/signup.html")


def login_page(request):
    if request.method == "POST":
        u = request.POST["u_name"]
        p = request.POST["passw"]
        
        check = authenticate(username = u, password = p)
        
        if check is not None:
            login(request, check)
            messages.success(request, "Login Sucessfully done.! Welcome to our blogify platform.!")
            
            return redirect("our_contact_forms")
        
        else:
            messages.warning(request, "Please enter valid username or password! authantication faild.")
            return redirect("login")
        
        
    return render(request, "auth/login.html")


def userlogout(request):
    logout(request)
    messages.info(request, "Logout sucessfully donr.. please login again to move one..")
    return redirect("login")