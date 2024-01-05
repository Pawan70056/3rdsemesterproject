from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from course.models import MyCourses

from .models import Profile


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Corrected the login function call
            messages.success(request, 'Login successful')
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






from .models import Profile


@login_required
def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Count the courses associated with the user's profile
    mycourses_count = MyCourses.objects.filter(user=request.user).count()


    context = {
        'profile': profile,
        'mycourses_count': mycourses_count,
    }
    
    return render(request, 'view_profile.html', context)



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
        print(profile_pic)
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
        messages.success(request, "Profile Updated successfully")

        return redirect('profile')  # Redirect to profile page after update

    # Pass the profile data to the template context to pre-fill the form
    context = {
        'profile': profile
    }

    return render(request, 'edit_profile.html', context)




@login_required
def settings(request):
    if request.method == 'POST':
        if 'delete_account' in request.POST:
            entered_username = request.POST.get('username', '')
            if entered_username == request.user.username:
                # Delete the user or mark the user as inactive
                request.user.delete()
                # Redirect to a different page after account deletion
                return redirect('register')
            else:
                messages.error(request, 'Please, check the username and user correct username to delete account')
                return redirect
        elif 'change_password' in request.POST:
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important to update the session
                messages.success(request, 'Your password was successfully updated!')
                logout(request)  # Log out the user after changing the password

                return redirect('login')
            else:
                messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'settings.html', {'form': form})





def logout_view(request):
    logout(request)
    return redirect('dashboard')
