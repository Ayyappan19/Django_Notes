from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,"Index.html")

def register(request):
    name = request.POST["name"]
    password = request.POST["password"]
    address = request.POST["address"]
    mail = request.POST["mail"]

    return render(request,"Output.html",{'Name':name, 'Password':password, 'Address':address, 'Mail':mail})
