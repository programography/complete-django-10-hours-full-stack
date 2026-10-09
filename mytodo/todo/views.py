from django.shortcuts import render, redirect
from todo.models import MyAllTodos
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def maintodopage(request):
    
    for_update = request.GET.get("id")
    
    todo = None
    
    if for_update:
        todo = MyAllTodos.objects.get(id = for_update)
    
    query = request.GET.get("q")
    
    if query:
        data = MyAllTodos.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
        # data = MyAllTodos.objects.filter(title__icontains = query) | MyAllTodos.objects.filter(description__icontains = query)
    else:
        data = MyAllTodos.objects.filter(user = request.user.id)
    
    return render(request, "pages/todopage.html", {"todos" : data, "u_todo" : todo})

def savingtodo(request):
    if request.method == "POST":
        tt = request.POST.get("t")
        pp = request.POST.get("p")
        im = request.FILES.get("img")
        dd = request.POST.get("desc")
        
        MyAllTodos.objects.create(
            user = request.user,
            title = tt, priority = pp, todo_pic = im,
            description = dd
        )
        
        messages.success(request, "Todo added sucessfully in our daily task...")
        
        return redirect("todo")
        
        
        
def deletetodo(request, myid):
    todo = MyAllTodos.objects.get(id = myid)
    todo.delete()
    messages.warning(request, "Todo deletd sucessfully from the list of todos...")
    return redirect("todo")
    
    
def donetodo(request, todoid):
    todo = MyAllTodos.objects.get(id = todoid)
    todo.is_deleted = True
    todo.save()
    messages.warning(request, "Todo done sucessfuly saved in db nice work.")
    return redirect("todo")

def updatenow(request, u_id):
    todo = MyAllTodos.objects.get(id = u_id)
    
    if request.method == "POST":
        tt = request.POST.get("t")
        pp = request.POST.get("p")
        im = request.FILES.get("img")
        dd = request.POST.get("desc")
        
        todo.title = tt
        todo.priority = pp
        todo.description = dd
        
        if im == None:
            todo.todo_pic = todo.todo_pic
        else:
            todo.todo_pic = im
        
        todo.save()
        
        messages.success(request, "todo updated sucessfuly!!")
        return redirect("todo")
        
    
    
def loginhere(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        check = authenticate(username = username, password = password)
        
        if check is not None:
            login(request, check)
            messages.success(request, "Login Sucessfully done! start adding your todos")
            return redirect("todo")

        else:
            messages.warning(request, "Username and password are not valid please try again")
            return redirect("login")
    
    
    
    return render(request, "auth/login.html")
    
def signuphere(request):
    return render(request, "auth/signup.html")


def signupherenw(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        f_name = request.POST.get("f_name")
        email = request.POST.get("email")
        password = request.POST.get("p")
        co = request.POST.get("cp")
        
        if password != co:
            messages.warning(request, "Password are't match..!")
            return redirect("signup")
        
        if User.objects.filter(username = username).exists():
            messages.warning(request, "User with this username alrady exist! try anoter")
            return redirect("signup")
        
        User.objects.create_user(username = username, 
                                 email = email, first_name = f_name,
                                 password = password)
        
        messages.success(request, "registration sucessfuly done! please login..!")
        return redirect("login")

def logoutuser(request):
    logout(request)
    messages.success(request, "Logouts sucessfully done! pleas eplogin for futer todos")
    return redirect("login")