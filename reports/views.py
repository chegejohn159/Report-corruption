from django.shortcuts import render, redirect
from .forms import signup,eaccsignup,reportchallenge,corruptions
# from django.contrib.auth.decorators import login_required,superuser_required,police_required,eacc_required
from .decorators import *
from .models import *


def index(request):
    return render(request, 'index.html', {})


def corrupt(request):
    if request.method == 'POST':
        form = corruptions(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/')
    else:
        form = corruptions()
    return render(request, 'report.html', {'form': form})

@police_required
def challenge(request):
    if request.method == 'POST':
        form = reportchallenge(request.POST)
        if form.is_valid():
            reportchallenges=form.save(commit=False)
            reportchallenges.police=request.user
            reportchallenges.save()

            return redirect('/')
    else:
        form = reportchallenge()
    return render(request, 'challenges.html', {'form': form})
@superuser_required
def signu(request):
    if request.method == 'POST':
        form = signup(request.POST)
        if form.is_valid():

            user = form.save()
            user.is_police=True
            user.set_password(user.password)
            user.save()
            return redirect('/')
    else:
        form = signup()
    return render(request, 'signup.html', {'form': form})
@superuser_required
def Eaccsignup(request):
    if request.method == 'POST':
        form = eaccsignup(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_Eacc=True
            user.set_password(user.password)
            user.save()
            return redirect('/')
    else:
        form = eaccsignup()
    return render(request, 'Eaccsignup.html', {'form': form})

@police_required
def cases(request):
    case=corruption.objects.filter(police=request.user,done=False)
    return render(request, 'case.html', {"case":case})

@eacc_required
def checks(request):
    check=reportchallenges.objects.all()
    return render(request, 'check.html', {"check":check})