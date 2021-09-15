from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Vacancy
from .utils import DataMixin


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

    context = {
        'vacancy': vacancy
    }

    return render(request, 'vacancies/vacancies_detail.html', context=context)