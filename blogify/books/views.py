from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pythonbook(request):
    return HttpResponse("this is my python bbok wala page..")

def javabook(request):
    return HttpResponse("this is my java book..")