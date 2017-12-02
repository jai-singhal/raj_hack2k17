from django.contrib.auth import authenticate, login
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from .forms import AnonymousTipForm, AnonymousUsersLoginForm
from .forms import EvidenceForm
from home.models import Evidence
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def anonymous_tip(request):
    form = AnonymousTipForm(request.POST or None)
    if form.is_valid():
        upload_evidence = form.cleaned_data.get("upload_evidence")
        instance = form.save(commit = False)
        instance.save()
        if not upload_evidence:
            return redirect('/')
        else:
            return redirect("/evidence/upload")

    return render(request,'anonymous/tip.html',{'form':form})



def anonymous_user_login(request):
    form = AnonymousUsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        upload_evidence = form.cleaned_data.get("upload_evidence")
        user = authenticate(username=username, password=password)

        login(request, user)
        if(upload_evidence):
            return redirect("/anonymous/dashboard")
        else:
            return redirect("/evidence/upload")
    return render(request, "anonymous/login.html", {"form": form})


def anonymous_dashboard(request):
    if not request.user.is_authenticated() or not str(request.user.__class__.__name__)=="AnonymousUser":
        raise Http404
    return render(request,'anonymous/dashboard.html',{'citizen':request.user})

import random
import string
from .models import AnonymousUser
def gen_uname_pass():
    return (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9)),
            ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
            )


def upload_evidence(request):
    form = EvidenceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        stay_in_touch = form.cleaned_data.get("stay_in_touch")
        if stay_in_touch:
            username, password = gen_uname_pass()
            new_user = AnonymousUser.objects.create(username = username, password = password)
            authenticate(new_user)
            context = {
                "username" : username,
                "password": password
            }
            return render(request, "anonymous/get_cred.html", context)
        else:
            return redirect("/")
    else:
        print("form invalid")
    return render(request, "anonymous/evidence.html", {"form": form})
