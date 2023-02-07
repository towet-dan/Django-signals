from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import UserForm, ProfileForm



# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            return render(request, 'home.html', {'img':img})

    else:
        form = ProfileForm()
    context = {
        'form':form
    }
    return render(request, 'home.html', context)
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
            
    else:
        form = UserForm()
    context = {
        'form':form
    }
    return render(request, 'index.html', context)