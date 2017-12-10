from django.http import Http404
from django.shortcuts import render,get_object_or_404
from case.models import *
from .models import *
import urllib.request, json 

from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout

from case.models import CaseCategory, CyberCaseCategories,Case, Witness

from citizen.models import Citizen
from .forms import UsersLoginForm,criminal_form

from home.models import AnonymousTip

from decouple import config

def login_view(request):

    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/police/dashboard")
    return render(request, "police/login.html", {"form": form})



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
    if not request.user.is_authenticated() or not str(request.user.__class__.__name__)=="Police":
        raise Http404

    ward_object=request.user.ward

    total_cases_count=Case.objects.all().count()
    approved_cases_count=Case.objects.filter(approved=True).count()
    solved_cases_count=Case.objects.filter(solved=True).count()
    pending_cases_count=total_cases_count-approved_cases_count

    pqset=Police.objects.filter(ward=request.user.ward)

    desig={
        'DGP': 'Director General of Police',
        'ADGP': 'Addl. Director General of Police',
        'IGP': 'Inspector General of Police',
        'DIGP': 'Deputy Inspector General of Police',
        'SPDCP': 'Superintendent of police Deputy Commissioner of Police(Selection Grade)',
        'SPDCPJ': 'Superintendent of police Deputy Commissioner of Police(Junior Management Grade)',
        'ASPADCP': 'Addl. Superintendent of police Addl.Deputy Commissioner of Police',
        'ASP': 'Assistant Superintendent of Police',
        'INSP': 'Inspector of Police',
        'SUB_INSP': 'Sub Inspector of Police.',
        'HVLDRM': 'Asst. Sub. Inspector/Havildar Major',
        'HVLDR': 'Havildar.',
        'LN': 'Lance Naik.',
        'CONS': 'Constable.',
        }
    res=[]
    for obj in pqset:
        res.append([obj.get_full_name(),desig[obj.designation]])




    context={
    "total_cases_count":total_cases_count,
    "approved_cases_count":approved_cases_count,
    "pending_cases_count":pending_cases_count,
    "solved_cases_count":solved_cases_count,
    "res":res,
    "ward_object":ward_object


    }
    return render(request,'police/dashboard.html',context)


def cbcview(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    my_object = get_object_or_404(CaseCategory, pk=id)
    cases_qset=Case.objects.filter(case_categories=my_object )


    context={"my_object":my_object,"cases_qset":cases_qset}
    return render(request,'police/cases_by_cat.html',context)


def cybercbcview(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    my_cyber_object = get_object_or_404(CyberCaseCategories, pk=id)
    cyber_cases_qset=Case.objects.filter(cyber_case_categories=my_cyber_object )
    cyber_cases_qset=Case.objects.filter(cyber_case_categories=my_cyber_object)

    context={"my_object":my_cyber_object,"cases_qset":cyber_cases_qset}
    return render(request,'police/cases_by_cat.html',context)


from comment.models import Comment

def case_detail(request,id=None,approved=None):
    if not request.user.is_authenticated():
        raise Http404
    app=approved
    comments = Comment.objects.filter(case = id)
    my_object = get_object_or_404(Case, id=id)
    if app=='1':
        my_object.approved=True
        print("yppppppppppppppp")
        my_object.save()
    wqset=Witness.objects.filter(case=my_object)
    ward_object=request.user.ward
    police_id = request.user.id
    files = my_object.evidence_set.all()
    print(files)
    context={"my_object":my_object,"wqset":wqset, "ward_object": ward_object, "police_id": police_id, "comments": comments,'files':files}
    return render(request,'police/case_detail.html',context)

def atip_detail(request,id=None):
    if not request.user.is_authenticated():
        raise Http404
    my_object = get_object_or_404(AnonymousTip, id=id)
    
    context={"my_object":my_object}
    return render(request,'police/atip_detail.html',context)

def b(b_id):
    try:
        string="https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofAndMember/ForApp/%s?client_id=%s" % (str(b_id),config('client_id'))
        with urllib.request.urlopen(string) as url:
            data=json.loads(url.read().decode())
        data=data['hof_Details']
        return data
    except:
        return None




def person_detail_view(request,id=None):
    if not request.user.is_authenticated():
        raise Http404

    user = get_object_or_404(Citizen,id=id)
    b_id = user.bhamashah
    photo_flag=1
    detail_flag=1
    d64={}
    data={}
 
    data = b(b_id)
    print(data)

    if data is None:
        detail_flag=0


    try:

        string="https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofMembphoto/%s/%s?client_id=%s" % (str(data['BHAMASHAH_ID']),str(data['M_ID']),config('client_id'))  
        with urllib.request.urlopen(string) as url:
            d64=json.loads(url.read().decode())
        d64=d64["hof_Photo"]["PHOTO"]
    except:
        photo_flag=0




    context={

        "data":data,
        "d64":d64,
        "detail_flag":detail_flag,
        "photo_flag":photo_flag


    }
  






    return render(request,'police/citizen_detail.html',context)



def police_logout(request):
    logout(request)

    return redirect("/")



def create_criminal_details(request):
    form=criminal_form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect("/police/criminal_directory")
    return render(request, "police/cdform.html",{"form" : form,})





def atips(request):
    if not request.user.is_authenticated():
        raise Http404
    aqset = AnonymousTip.objects.all()
    context={"aqset":aqset}
    return render(request,'police/atips.html',context)

