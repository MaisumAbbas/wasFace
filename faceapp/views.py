from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def instructions(request):
    return render(request, 'instructions.html')

def camera(request):
    return render(request, 'camera.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active and user.is_superuser:
                login(request,user)
                return redirect('/faceapp/dashboard/', pk=user.username) 
        else:
            print("Login Failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Details")
    else:
        return render(request, 'login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
def photos_database(request):
    return render(request, 'admin/photos_database.html')

@login_required
def add_audio(request):
    return render(request, 'admin/add_audio.html')

@login_required
def audio_track_list(request):
    return render(request, 'admin/audio_track_list.html')

@login_required
def profile(request):
    return render(request, 'admin/profile.html')