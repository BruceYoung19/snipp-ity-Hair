from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("Users:lists")
    else:
        form = UserCreationForm()
    return render(request,"register.html",{"form":form})    

def login(request):
    return render(request,"login.html")

def contact(request):
    return render(request,"contacts.html")

def haircuts(request):
    return render(request,"haircuts.html")
