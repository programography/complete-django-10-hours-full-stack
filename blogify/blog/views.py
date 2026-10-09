from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import ContactUsModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    # return HttpResponse("<h1>THis is my home page</h1>")
    return render(request, "home.html") 

@login_required(login_url = "login")
def about(request):
    # return HttpResponse("<h1>This is my about us page<h1>")
    return render(request, "about.html")

# @login_required(login_url = "login")
def contactus(request):
    return render(request, "contactus.html")

def services(request):
    return render(request, "services.html")


def saving_data(request):    
    if request.method == "POST":
        first_name = request.POST.get("f_name") # request.POST["f_name"]
        last_name = request.POST.get("l_name")
        email = request.POST.get("email")
        phon = request.POST.get("p_number")
        gen = request.POST.get("gender")
        date_of = request.POST.get("dob")
        addr = request.POST.get("address")
        my_msg = request.POST.get("msg")
        
        ContactUsModel.objects.create(
            first_name = first_name, last_name = last_name, email = email,
            phone_number = phon, gender = gen, dob = date_of,
            address = addr, message = my_msg
        )
        
        messages.success(request, "We recived and saved you request, will get back to you asap..!")
        messages.warning(request, "Be ready at evening 4:00 PM, will contact you.")
        
        return redirect("contactus")
    
    return HttpResponse(request)


def our_contact_forms(request):
    
    if request.user.is_authenticated:
        
        data = ContactUsModel.objects.all().order_by("-id")
        
        return render(request, "our_contact_forms.html", {"mydata" : data})

    else:
        messages.warning(request, "Please login first! you are not authorized for this page for now..!")
        return redirect("login")


def deletequery(request, x):
    
    dt = ContactUsModel.objects.get(id = x)
    dt.delete()
    
    messages.success(request, "We successfult deleted contact us qyuery from Databsse !! Permanently..")
    
    return redirect("our_contact_forms")


def updatedata(request, myid):
    
    obj = ContactUsModel.objects.get(id = myid)
    
    if request.method == "POST":
        first_name = request.POST.get("f_name") 
        last_name = request.POST.get("l_name")
        email = request.POST.get("email")
        phon = request.POST.get("p_number")
        gen = request.POST.get("gender")
        date_of = request.POST.get("dob")
        addr = request.POST.get("address")
        my_msg = request.POST.get("msg")
        
        obj.first_name = first_name
        obj.last_name = last_name
        obj.email = email
        obj.phone_number = phon
        obj.gender = gen
        obj.dob = date_of
        obj.address = addr
        obj.message = my_msg
        
        obj.save()
        
        messages.success(request, "Data succesfully changed! condatct query from data is updated..")
        
        return redirect("our_contact_forms")
        
        
    return HttpResponse("data upayyed sucessfully....")