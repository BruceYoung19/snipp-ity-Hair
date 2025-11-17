from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def contact(request):
    return render(request,"contacts.html")

def haircuts(request):
    return render(request,"haircuts.html")
