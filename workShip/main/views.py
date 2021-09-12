from django.shortcuts import render

from vacancies.models import Vacancy

def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'main/index.html', {'vacancies': vacancies})


def register(request):
    return render(request, 'main/register.html')


def in_develop(request):
    return render(request, 'main/in_develop.html')