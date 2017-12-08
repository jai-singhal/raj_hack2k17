from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import logout

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UsersLoginForm
from case.forms import *
from .forms import UsersRegisterForm
from .models import Citizen

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
    return render(request, "citizen/login.html",{'form':form})

def dashboard(request):
    if not request.user.is_authenticated() :
        raise Http404
    return render(request,'citizen/dashboard.html',{'citizen':request.user})


def citizen_logout(request):
    logout(request)

    return redirect("/")

def create_case(request):
    form = case_form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect("/citizen/dashboard")
    return render(request, "citizen/case.html", {"form": form})


def cbcview(request):
    if not request.user.is_authenticated():
        raise Http404
    my_object = get_object_or_404(Citizen, pk=request.user.id)
    cases_qset=Case.objects.filter(userid=my_object)
    print(cases_qset)
    context={"my_object":my_object,"cases_qset":cases_qset}
    return render(request,'citizen/case_by_cat.html',context)

from comment.models import Comment

def user_case_detail(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    comments = Comment.objects.filter(case = id)
    my_object = get_object_or_404(Case, id=id)
    wqset=Witness.objects.filter(case=my_object)
    police_id = request.user.id
    ward_object = None
    context={"my_object":my_object,"wqset":wqset, "ward_object": ward_object, "police_id": police_id, "comments": comments}
    return render(request,'police/case_detail.html',context)




def create_cyber_case(request):
    form = cyber_case_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/citizen/dashboard")
    return render(request, "/citizen/case.html", {"form": form})

def register_view(request):
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/citizen/dashboard")
    return render(request, "citizen/register.html",{"form" : form,})



def create_case(request):
    form=case_form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect("/citizen/dashboard")
    return render(request, "citizen/case.html",{"form" : form,})



def create_cyber_case(request):
    form=cyber_case_form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect("/citizen/dashboard")
    return render(request, "citizen/case.html",{"form" : form, 'cyber':True})

