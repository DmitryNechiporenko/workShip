from django.shortcuts import render
from .models import Vacancy


def vacancies_home(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/vacancies_home.html', {'vacancies': vacancies})


def vacancies_detail(request):
    id = request.GET.get('id', '')
    try:
        vacancy = Vacancy.objects.get(pk=id)
    except Vacancy.DoesNotExist:
        vacancy = None

    return render(request, 'vacancies/vacancies_detail.html', {'vacancy': vacancy})