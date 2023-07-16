from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth # type: ignore
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from itertools import chain
import random

# Create your views here.
@login_required(login_url='login')
def home(request, *args, **kwargs):
    
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)
    
    context = {
        'profile': profile,
        'user': user,
    }
    
    return render(request, 'index.html', context)

def signup(request, *args, **kwargs):
    
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken.")
                return redirect("signup")
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "This Account already exists.")
                    return redirect("signup")
                else:
                    new_user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                    new_user.save()
                    new_profile = Profile.objects.create(id_user=new_user.id, user=new_user) # type: ignore
                    new_profile.save()
                    
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)
                    
                    return redirect("settings")
        else:
            messages.info(request, "Passwords do not match.")
            return redirect("signup")
        
    else:
        return render(request, 'signup.html', {})

def login(request, *args, **kwargs):
    
    if request.method == 'POST':
        usernoremail = request.POST['usernoremail']
        password = request.POST['password']
        
        if '@' in usernoremail:
            try:
                get_user = User.objects.get(email=usernoremail)
                username = get_user.username
            except:
                messages.info(request, "Invalid Credentials")
                return redirect("login")
        else:
            username = usernoremail
            
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
            
    else:
        return render(request, 'signin.html', {})

@login_required(login_url='login')
def logout(request, *args, **kwargs):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def settings(request, *args, **kwargs):
    prof = Profile.objects.get(user=request.user)
    cuser = User.objects.get(username=request.user.username)
        
    if request.method == 'POST':
        profileimg = request.FILES.get('image')
        firstname = request.POST['firstn']
        lastname = request.POST['lastn']
        username = request.POST['usern']
        bio = request.POST['bio']
        location = request.POST['loc']
        private = request.POST.get('priv')
        commenting = request.POST.get('commenting')
        notifications = request.POST.get('notifications')
        
        if private is not None:
            prof.private = True
        else:
            prof.private = False
        
        if commenting is not None:
            prof.allowcomments = True
        else:
            prof.allowcomments = False
            
        if notifications is not None:
            prof.notificationson = True
        else:
            prof.notificationson = False
        
        if profileimg is not None:
            prof.profileimage = profileimg
            
        if location is not None:
            prof.location = location
        
        if firstname is not None:
            cuser.first_name = firstname
        
        if lastname is not None:
            cuser.last_name = lastname
        
        if username is not None:
            cuser.username = username
        
        if bio is not None:
            prof.bio = bio
        
        prof.save()
        
        return redirect('settings')
    else:
        context = {
            'profile': prof,
        }
        
        return render(request, 'setting.html', context)

@login_required(login_url='login')
def profile(request, username, *args, **kwargs):
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        
        # posts display
        if profile.posts < 1000:
            profile.dposts = f"{profile.posts}"
        
        if profile.posts >= 1000 and profile.posts < 1000000:
            calc = round(profile.posts / 1000, 1)
            profile.dposts = f"{calc}K"
        
        if profile.posts >= 1000000 and profile.posts < 1000000000:
            calc = round(profile.posts / 1000000, 1)
            profile.dposts = f"{calc}M"
            
        if profile.posts >= 1000000000 and profile.posts < 1000000000000:
            calc = round(profile.posts / 1000000000, 1)
            profile.dposts = f"{calc}B"
        
        # followers display
        if profile.followers < 1000:
            profile.dfollowers = f"{profile.followers}"
        
        if profile.followers >= 1000 and profile.followers < 1000000:
            calc = round(profile.followers / 1000, 1)
            profile.dfollowers = f"{calc}K"
        
        if profile.followers >= 1000000 and profile.followers < 1000000000:
            calc = round(profile.followers / 1000000, 1)
            profile.dfollowers = f"{calc}M"
            
        if profile.followers >= 1000000000 and profile.followers < 1000000000000:
            calc = round(profile.followers / 1000000000, 1)
            profile.dfollowers = f"{calc}B"
            
        # following display
        if profile.following < 1000:
            profile.dfollowing = f"{profile.following}"
        
        if profile.following >= 1000 and profile.following < 1000000:
            calc = round(profile.following / 1000, 1)
            profile.dfollowing = f"{calc}K"
        
        if profile.following >= 1000000 and profile.following < 1000000000:
            calc = round(profile.following / 1000000, 1)
            profile.dfollowing = f"{calc}M"
            
        if profile.following >= 1000000000 and profile.following < 1000000000000:
            calc = round(profile.following / 1000000000, 1)
            profile.dfollowing = f"{calc}B"
            
        profile.save()
        
        context = {
            'user': user,
            'profile': profile,
        }
        
        if request.method == 'POST':
            pass
        else:
            return render(request, 'profile.html', context)
    else:
        return HttpResponse("404: Page not Found")