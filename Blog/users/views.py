from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogs:home'))

def register(request):
    if request.method !='POST':
        form = UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            LoginView()
            return HttpResponseRedirect(reverse('users:login'))
    context={'form':form}
    return render(request,'users/register.html',context)
        