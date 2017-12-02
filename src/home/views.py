from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import AnonymousTipForm, AnonymousUsersLoginForm


def anonymous_tip(request):
    form = AnonymousTipForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return redirect('/')
    return render(request,'anonymous/tip.html',{'form':form})



def anonymous_user_login(request):

    form = AnonymousUsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/anonymous/dashboard")
    return render(request, "anonymous/login.html", {"form": form})


def anonymous_dashboard(request):
    if not request.user.is_authenticated() or not str(request.user.__class__.__name__)=="AnonymousUser":
        raise Http404
    return render(request,'anonymous/dashboard.html',{'citizen':request.user})
