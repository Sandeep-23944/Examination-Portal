from django.http import FileResponse, HttpResponse
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from .models import Profile

# Home page view
def homepage(request):
    return render(request, 'core/homepage.html')

# Signup page view
def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create profile for user with selected role (Student/Teacher)
            profile = Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type']
            )
            login(request, user)
            return redirect('profile')  # Redirect to profile after signup
    else:
        form = UserSignupForm()

    return render(request, 'core/signup.html', {'form': form})

# Profile page view - Requires login + admin approval + role-based redirect
@login_required
def profile_view(request):
    if request.user.is_superuser:
        # ✅ Redirect admin users to the admin panel
        return redirect('/admin/')

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('homepage')

    if not profile.is_approved:
        return render(request, 'core/not_approved.html')

    if profile.user_type == 'student':
        return redirect('student_dashboard')
    elif profile.user_type == 'teacher':
        return redirect('teacher_dashboard')
    else:
        return redirect('homepage')

# Student Dashboard
@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

# Teacher Dashboard
@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')

# View Admit Card
@login_required
def admit_card(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return render(request, 'core/admit_card.html', {'error': 'Profile not found'})
    
    # Set dummy exam details
    if profile.user_type == 'student':
        exam_name = 'Sample Exam for Students'
        exam_date = '2025-05-01'
        exam_location = 'Student Hall A'
    else:
        exam_name = 'Teacher Evaluation Exam'
        exam_date = '2025-05-02'
        exam_location = 'Teacher Meeting Room'

    return render(request, 'core/admit_card.html', {
        'profile': profile,
        'exam_name': exam_name,
        'exam_date': exam_date,
        'exam_location': exam_location
    })

def download_download_documents(request):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'static', 'pdf', 'Pre_examination_downloads.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Pre_examination_downloads.pdf')
    else:
        return HttpResponse("File not found.", status=404)
    
# Download Admit Card PDF
@login_required
def download_admit_card(request):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'static', 'pdf', 'admit_card_sample.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='admit_card_sample.pdf')
    else:
        return HttpResponse("File not found.", status=404)
  
    # View Results
from django.shortcuts import render
@login_required
def results(request):
    context = {
        'some_data': 'Hello, this is the results page!'
    }
    return render(request, 'core/results.html', context)  # ✅ Fixed path


# Logout View
def user_logout(request):
    logout(request)
    return redirect('homepage')  # ✅ This should match your URL name
