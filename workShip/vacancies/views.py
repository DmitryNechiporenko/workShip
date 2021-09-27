from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Vacancy
from main.models import CompanyProfile
from .utils import DataMixin
from .forms import *


class vacancies_home(DataMixin, ListView):
    paginate_by = 2
    model = Vacancy
    template_name = "vacancies/vacancies_home.html"
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вакансии")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Vacancy.objects.filter(is_published=True)


def vacancies_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    company = CompanyProfile.objects.filter(user=vacancy.user).get()

    context = {
        'vacancy': vacancy,
        'company': company
    }

    return render(request, 'vacancies/vacancies_detail.html', context=context)


@login_required
def vacancies_add(request):
    if request.method == 'POST':
        vacancies_form = AddVacancyForm(request.POST)
        vacancies_form.instance.user = request.user

        if vacancies_form.is_valid():
            vacancies_form.save(commit=False)
            #vacancies_form.cleaned_data['user'] = request.user
            vacancies_form = vacancies_form.save()
            return redirect('vacancies_home')
        else:
            print(vacancies_form.errors)
    else:
        vacancies_form = AddVacancyForm
    context = {
        'vacancies_form': vacancies_form
    }
    return render(request, 'vacancies/vacancies_add.html', context=context)