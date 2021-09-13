from django.shortcuts import render
from .models import Vacancy


def vacancies_home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/vacancies_home.html', {'vacancies': vacancies})


def vacancies_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(pk=vacancy_id)
    except Vacancy.DoesNotExist:
        vacancy = None

    return render(request, 'vacancies/vacancies_detail.html', {'vacancy': vacancy})