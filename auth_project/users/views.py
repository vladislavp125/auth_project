from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging


@login_required
def user_dashboard(request):


    if request.user.is_superuser:
        return render(request, 'admin_dashboard.html')
    return render(request, 'user_dashboard.html')
