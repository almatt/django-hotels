from django.shortcuts import render, redirect
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('dashboard:index')
    return render(request,'hotels/login.html',{'form':form})


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        print(form.save(commit=False))
    return render(request,'hotels/index.html',{'form':form})
