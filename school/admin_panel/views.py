from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    if not request.user.is_superuser:
        return render(request, 'accounts/access_denied.html')

    return render(request, 'admin_panel/dashboard.html')