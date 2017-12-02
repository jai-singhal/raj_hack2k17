from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UsersLoginForm
<<<<<<< HEAD
from case.forms import *
=======
from .forms import UsersRegisterForm

>>>>>>> 7d59336bce7c17d260927a30d6c9a915b4cd59f9

def login_view(request):

    if  str(request.user.__class__.__name__)=="Citizen":
        return redirect('/citizen/dashboard')


    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/citizen/dashboard")
    return render(request, "citizen/login.html")

def dashboard(request):
    if not request.user.is_authenticated() or not str(request.user.__class__.__name__)=="Citizen":
        raise Http404
    return render(request,'citizen/dashboard.html',{'citizen':request.user})


def citizen_logout(request):
    logout(request)

    return redirect("/")



def register_view(request):
    form = UsersRegisterForm(request.POST or None)
    print(request.POST)
    print('__________________________')
    print(form)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        print('Citizem',new_user,'successfully logged in')
        return redirect("/citizen/dashboard")
    return render(request, "citizen/register.html",{"form" : form,})




def create_case(request):
    form=case_form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect("/citizen/dashboard")
    return render(request, "citizen/case.html",{"form" : form,})
