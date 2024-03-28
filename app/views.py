from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

from .services import extract_transcript_from_youtube

@api_view(["GET"])
def ping(request):
    return JsonResponse({"msg":"Hello from youtube timestamp generator"},safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password) 
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect("/")
        else:
            messages.error(request,"Invalid login credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return render(request,"login.html")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return render(request,"login.html")
        else:
            user = User.objects.create_user(username,email,password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user = authenticate(request,username=username, password=password) 
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/")
    else:
        return render(request,"login.html")

@csrf_exempt    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/login")

@csrf_exempt
@login_required(login_url="/login/")
def dashboard(request):
    return render(request,"dashboard.html")

# youtube link
@csrf_exempt
@login_required(login_url="/login/")
def generate_transcript(request):
    if request.method == 'POST':
        youtube_link = request.POST.get('youtube_link')

        # Extract transcript from YouTube
        transcript = extract_transcript_from_youtube(youtube_link)
        if not transcript:
            messages.error(request,"Transcript not found for this video")
            return render(request, 'dashboard.html', {'error': 'Transcript not found'})
        
        # messages.success(request, "Transcript generated successfully")
        return render(request, 'transcript.html', {"transcript": transcript})
    else:
        return render(request, 'transcript.html', {'error': 'Only POST requests are allowed'})
