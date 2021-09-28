from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from main.models import Profile, CompanyProfile
from vacancies.models import *
from summaries.models import *


@login_required
def personal_account_home(request):
    seaman_profile = Profile.objects.filter(user=request.user)
    company_profile = CompanyProfile.objects.filter(user=request.user)

    if seaman_profile:
        summaries = Summary.objects.filter(user=request.user)

        context = {
            'profile': seaman_profile.get(),
            'summaries': summaries
        }
        return render(request, 'personal_account/personal_seaman_account.html', context=context)
    elif company_profile:
        vacancies = Vacancy.objects.filter(user=request.user).annotate(Count('vacancyresponses'))


        context = {
            'profile': company_profile.get(),
            'vacancies': vacancies
        }
        return render(request, 'personal_account/personal_company_account.html', context=context)


@login_required
def personal_account_edit(request):
    seaman_profile = Profile.objects.filter(user=request.user)
    company_profile = CompanyProfile.objects.filter(user=request.user)

    if seaman_profile:
        context = {
            'profile': seaman_profile.get()
        }
        return render(request, 'personal_account/personal_company_edit.html', context=context)
    elif company_profile:
        context = {
            'profile': company_profile.get()
        }
        return render(request, 'personal_account/personal_company_edit.html', context=context)