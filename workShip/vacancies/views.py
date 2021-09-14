from django.shortcuts import render, get_object_or_404
from .models import Vacancy


def vacancies_home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/vacancies_home.html', {'vacancies': vacancies})


def vacancies_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)

    context = {
        'vacancy': vacancy
    }

    return render(request, 'vacancies/vacancies_detail.html', context=context)