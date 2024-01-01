from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Profile  # Import your Profile model

# views.py






def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Corrected the login function call
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    
    return render(request, 'register.html')





@login_required
def view_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)
    return render(request, 'view_profile.html', {'profile': profile})


def edit_profile(request):
    # Fetch the profile data for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Process the form submission
        # Retrieve data from the submitted form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        phone = request.POST.get('phone')
        university = request.POST.get('university')
        bio = request.POST.get('bio')
        street = request.POST.get('street')
        city = request.POST.get('city')
        # Process the profile picture separately
        profile_pic = request.FILES.get('profile_pic')

        # Update the profile fields with the new data
        profile.first_name = first_name
        profile.last_name = last_name
        profile.email = email
        profile.gender = gender
        profile.nationality = nationality
        profile.phone = phone
        profile.university = university
        profile.bio = bio
        profile.street = street
        profile.city = city
        if profile_pic:
            profile.profile_pic = profile_pic
        profile.save()

        return redirect('profile')  # Redirect to profile page after update

    # Pass the profile data to the template context to pre-fill the form
    context = {
        'profile': profile
    }

    return render(request, 'edit_profile.html', context)





def logout_view(request):
    logout(request)
    return redirect('dashboard')
