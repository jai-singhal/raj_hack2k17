from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm


def login_view(request):
    if request.user.is_authenticated():
        return redirect("/police/dashboard")
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/citizen/dashboard")
    return render(request, "citizen/login.html")

def dashboard(request):
    if not request.user.is_authenticated():
        raise Http404
    return render(request,'police/dashboard.html')


from .forms import UsersRegisterForm


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