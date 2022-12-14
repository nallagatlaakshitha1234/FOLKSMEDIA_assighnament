from django.shortcuts import render
from app.forms import * 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth  import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def registration(request):
    uf=UserForm()
    pf=BlogInfoForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        ud=UserForm(request.POST)
        pd=BlogInfoForm(request.POST,request.FILES)
        if ud.is_valid() and pd.is_valid():
            UI=ud.save(commit=False)
            pw=ud.cleaned_data.get('password')
            UI.set_password(pw)
            UI.save()
            PI=pd.save(commit=False)
            PI.user=UI
            PI.save()
    return render(request,'registration.html',d)



def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid User')

    return render(request, 'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def display_profile(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=BlogInfo.objects.filter(user=UO)
    d={'UO':UO,'PO':PO}
    return render(request, 'display_profile.html',d)







