from django.shortcuts import render,redirect
from libraryapp.models import Library
from django.contrib.auth.decorators import login_required
from libraryapp.forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def showAll(request):
    librarydata=Library.objects.all()
    return render(request,'testapp/showall.html',{'librarydata':librarydata})

@login_required
def delete(request,id):
    librarydata=Library.objects.get(id=id)
    librarydata.delete()
    return redirect('home')

@login_required
def update(request,id):
    if request.method=='POST':
        librarydata=Library.objects.get(id=id)
        librarydata.bid=request.POST.get('BID')
        librarydata.bname=request.POST.get('BN')
        librarydata.bauthor=request.POST.get('BA')
        librarydata.bcost=request.POST.get('BC')
        librarydata.save()
        return redirect('home')
    librarydata=Library.objects.get(id=id)
    return render(request,'testapp/update.html',{'data':librarydata} )

@login_required
def adddata(request):
    if request.method=='POST':
        Library(
        bid=request.POST.get('bid'),
        bname=request.POST.get('bname'),
        bauthor=request.POST.get('bauthor'),
        bcost=request.POST.get('bcost')).save()
        return redirect('home')
    else:
        return render(request,'testapp/add.html')

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html', {'form':form} )
