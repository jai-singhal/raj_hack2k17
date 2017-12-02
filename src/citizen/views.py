from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm


def login_view(request):
    # if request.user.is_authenticated():
    #     return redirect("/citizen/dashboard")
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/citizen/dashboard")
    return render(request, "citizen/login.html")

def dashboard(request):
    if request.user.is_authenticated() and str(request.user.__class__.__name__)=="Citizen":
        pass
    else:
        raise Http404
    return render(request,'citizen/dashboard.html')


from .forms import UsersRegisterForm


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


# def register_view(request):
# 	flag = False
# 	aadharno = ''
# 	error = ''
# 	bah = ''
# 	if(request.method == 'POST'):
# 		bah = request.POST["bhamashah"]
# 		ada = request.POST["aadhaar"]
# 		if(bah == '' or ada == ''):
# 			error = "All the fields are required"
# 		bah=bah.upper()
#         string="https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofAndMember/ForApp/%s?client_id=ad7288a4-7764-436d-a727-783a977f1fe1" % (str(bah))
# 		with urllib.request.urlopen(string) as url:
# 		if 'hof_Details' in data.keys():
# 			data=data['hof_Details']
# 			if 'AADHAR_ID' in data.keys():
# 				if str(data['AADHAR_ID'])==str(ada):
# 					flag=True
# 					request.session["prof"]=data
# 				else:
# 					error='Verification Failed, Check the entered FAMILY ID NO and Aadhar Id No and Try again..'
#                     data=json.loads(url.read().decode())
# 			else:
# 				error='Verification Failed, Check the entered FAMILY ID NO and Aadhar Id No and Try again..'
# 		else:
# 			error='Verification Failed, Check the entered FAMILY ID NO and Aadhar Id No and Try again..'
# 	# check with api if verified set flag = true else write into error
# 	if(flag):
# 		return redirect("/citizen/dashboard")
# 	if(error != '' and flag == False):
# 		return render(request,"citizen/register",{'error': error})
#     request.session["aadhar"] = bah
#     return render(request, "citizen/register.html",{"form" : form,})
#
#
#
# def accept(request):
# 	if("id" in request.session.keys()):
# 		return HttpResponseRedirect("/")
# 	if('aadhar' not in request.session.keys() and request.method == 'GET'):
# 		return HttpResponseRedirect("/")
# 	elif('aadhar' in request.session.keys() and request.method == 'GET'):
# 		return render(request,"citizen/accept.html")
# 	elif('aadhar'  in request.session.keys() and request.method == 'POST'):
# 		error = ''
# 		# request.session.pop("aadhar",None)
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		confirmation = request.POST['confirmation']
# 		if(username == '' or password == '' or confirmation == ''):
# 			error = "All the fields are required"
# 		elif(password != confirmation):
# 			error = "Password did not match..."
# 		if(error == ''):
# 			obj=Profile.objects.filter(uname=username)
# 			if len(obj)>0:
# 				error='Username already exists'
# 				return render(request,"citizen/accept.html",{"error":error})
#
#
# 			else:
#                 return HttpResponseRedirect("/")
# 				# return render(request,"kalyan/HE/public/accept.html",{"error":"Registration Successful"})
# 		else:
# 			return render(request,"citizen/accept.html",{"error":error})
