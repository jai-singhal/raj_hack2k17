from django.shortcuts import render, redirect
from .models import AnonymousTip
from .forms import AnonymousTipForm

def anonymous_tip(request):
    form = AnonymousTipForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return redirect('')
    return render(request,'anonymous_tip.html',{'form':form})