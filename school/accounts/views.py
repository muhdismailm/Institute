
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'accounts/home.html')


def admin_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:

            login(request, user)
            return redirect('admin_dashboard')

        else:
            messages.error(request, 'Invalid admin credentials')

    return render(request, 'accounts/admin_login.html')


def teacher_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if hasattr(user, 'profile') and user.profile.role == 'TEACHER':

                login(request, user)
                return redirect('teacher_dashboard')

        messages.error(request, 'Invalid teacher credentials')

    return render(request, 'accounts/teacher_login.html')


def student_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if hasattr(user, 'profile') and user.profile.role == 'STUDENT':

                login(request, user)
                return redirect('student_dashboard')

        messages.error(request, 'Invalid student credentials')

    return render(request, 'accounts/student_login.html')


def user_logout(request):

    logout(request)
    return redirect('home')
