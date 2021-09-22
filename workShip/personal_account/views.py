from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from main.models import Profile

@login_required
def personal_account_home(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'personal_account/personal_account_home.html', context=context)