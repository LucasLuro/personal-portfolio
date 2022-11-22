import random
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# -------------------- Showroom Itself ---------------------------
def showroomhome(request):
    return render(request, 'showroom/home.html')

# -------------------- Password Generator ------------------------
def pghome(request):
    return render(request, 'showroom/pg.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()-+=_'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'showroom/generatedpw.html', {'password': thepassword})

# --------------------- Authentication System ----------------------------
def authhome(request):
    return render(request, 'showroom/authhome.html')
    
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'showroom/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('../loginuser/')
            except IntegrityError:
                return render(request, 'showroom/signupuser.html', {'form':UserCreationForm(),'error':'Username taken, please choose a new one'})
        else:
            return render(request, 'showroom/signupuser.html', {'form':UserCreationForm(),'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'showroom/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'showroom/loginuser.html', {'form':AuthenticationForm(), 'error':'Your credentials didn\'t match'})
        else:
            login(request, user)
            return redirect('../loggedinuser/')
            
@login_required
def loggedinuser(request):
    return render(request, 'showroom/loggedinuser.html')

@login_required        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('../')