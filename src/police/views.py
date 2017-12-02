from django.http import Http404
from django.shortcuts import render,get_object_or_404
from case.models import *

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import UsersLoginForm


def login_view(request):
    # if request.user.is_authenticated():
    #     return redirect("/police/dashboard")
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/police/dashboard")
    return render(request, "police/login.html")

import json
from django.core.serializers import serialize
def get_case_categories(request):
    if request.method == "GET" and request.is_ajax(): 
        case_category_qset= CaseCategory.objects.all()
        cyber_case_category_qset= CyberCaseCategories.objects.all()
        cyber_data =  serialize("json", cyber_case_category_qset) 
        case_data =  serialize("json", case_category_qset) 
        data = {
            "cyber_data": cyber_data,
            "case_data":case_data,
        }

        return HttpResponse(json.dumps(data), content_type='application/json')




def dashboard(request):
    if request.user.is_authenticated() and str(request.user.__class__.__name__)=="Police":
        pass
    else:
        raise Http404
    

    print(request.user.__class__.__name__)
    ward_object=request.user.ward   



    context={"ward_object":ward_object}
    return render(request,'police/dashboard.html',context)


def cbcview(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    my_object = get_object_or_404(CaseCategory, pk=id)  
    cases_qset=Case.objects.filter(case_categories=my_object , ward_id=request.user.ward)    
     
    context={"my_object":my_object,"cases_qset":cases_qset}
    return render(request,'police/cases_by_cat.html',context)


def cybercbcview(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    my_cyber_object = get_object_or_404(CyberCaseCategories, pk=id)  
    cyber_cases_qset=Case.objects.filter(cyber_case_categories=my_cyber_object , ward_id=request.user.ward)    
     
    context={"my_object":my_cyber_object,"cases_qset":cyber_cases_qset}
    return render(request,'police/cases_by_cat.html',context)




def case_detail(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    my_object = get_object_or_404(Case, id=id)  
    wqset=Witness.objects.filter(case=my_object) 
    context={"my_object":my_object,"wqset":wqset}
    return render(request,'police/case_detail.html',context)




def person_detail_view(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    #api call get data and send it to a html

    context={}
    return render(request,'police/citizen_detail.html',context)



def police_logout(request):
    logout(request)
    
    return redirect("/")

