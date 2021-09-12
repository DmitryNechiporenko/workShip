from django.shortcuts import render


def company_home(request):
    return render(request, 'company/company_home.html')