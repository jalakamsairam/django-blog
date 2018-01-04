import os
from django.http import HttpResponse
from django.shortcuts import  render,redirect
from .forms import  RegisterForm, LoginForm
# from passlib.hash import
# from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth  import  authenticate
from django import forms

def index(request):
    print("i am being hit index")
    return render(request, '../templates/index.html')

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form);
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            Repassword = form.cleaned_data['Repassword']
            email = form.cleaned_data['email']
            if password == Repassword:
                u = User(username=username,email=email)
                u.set_password(password)
                u.save()
                return redirect('signin')
            else:
                return forms.ValidationError("passwords dont match")
    else:
        form  = RegisterForm()
        print("i am being hit signup")
        return render(request, "../templates/signup.html",{'form':form})

def home(request):
    print("i am being hit home")
    return HttpResponse("login successful  you are in the home page");

def signin(request):
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            print('form is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticated = authenticate(username = username,password = password)
            print(authenticated);
            if not (authenticated == None):
                print('inside the authenticated loop')
                return HttpResponse(" you are successfully logged in as user")
            else:
                return HttpResponse(" User not found")

    else:
        form = LoginForm()
        return render(request,"../templates/signin.html",{'form':form})

def welcome(request):
    return render(request,"../templates/welcome.html")