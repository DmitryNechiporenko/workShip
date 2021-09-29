from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import *
from main.models import CompanyProfile
from summaries.models import Summary
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

    if request.method == 'POST':
        response_form = VacancyResponseForm(request.POST)
        if response_form.is_valid():
            response = VacancyResponses.objects.create(
                vacancy=vacancy,
                summary=response_form.cleaned_data['summary'],
                from_company=False
                )

    company = CompanyProfile.objects.filter(user=vacancy.user).get()
    summaries = Summary.objects.filter(user=request.user)

    context = {
        'vacancy': vacancy,
        'company': company,
        'summaries': summaries
    }

    return render(request, 'vacancies/vacancies_detail.html', context=context)


@login_required
def vacancies_responses(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id, user=request.user)
    responses = VacancyResponses.objects.filter(vacancy=vacancy, from_company=False)

    context = {
        'vacancy': vacancy,
        'responses': responses
    }

    return render(request, 'vacancies/vacancies_responses.html', context=context)


@login_required
def vacancies_response_detail(request, response_id):
    response = get_object_or_404(VacancyResponses, pk=response_id)

    context = {
        'response': response
    }

    return render(request, 'vacancies/vacancies_response_detail.html', context=context)


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