from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    if not hasattr(request.user, 'profile'):
        return render(request, 'accounts/access_denied.html')

    if request.user.profile.role != 'TEACHER':
        return render(request, 'accounts/access_denied.html')

    return render(request, 'teacher/dashboard.html')