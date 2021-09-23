from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from main.models import Profile, CompanyProfile
from vacancies.models import *

@login_required
def personal_account_home(request):
    seaman_profile = Profile.objects.filter(user=request.user)
    company_profile = CompanyProfile.objects.filter(user=request.user)

    if seaman_profile:
        context = {
            'profile': seaman_profile.get()
        }

        return render(request, 'personal_account/personal_account_home.html', context=context)
    elif company_profile:
        vacancies = Vacancy.objects.filter(user=request.user)

        context = {
            'profile': company_profile.get(),
            'vacancies': vacancies
        }

        #print(company_profile[0])
        return render(request, 'personal_account/personal_company_account.html', context=context)
