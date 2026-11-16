from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    if not hasattr(request.user, 'profile'):
        return render(request, 'accounts/access_denied.html')

    if request.user.profile.role != 'STUDENT':
        return render(request, 'accounts/access_denied.html')

    return render(request, 'student/dashboard.html')