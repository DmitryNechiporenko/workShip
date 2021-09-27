from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from main.models import Profile

from .forms import AddSummaryForm
from .models import Summary
from .utils import DataMixin


class summaries_home(DataMixin, ListView):
    paginate_by = 2
    model = Summary
    template_name = "summaries/summaries_home.html"
    context_object_name = 'summaries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Резюме")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Summary.objects.filter(is_published=True)


def summaries_detail(request, summary_id):
    summary = get_object_or_404(Summary, pk=summary_id)
    profile = Profile.objects.filter(user=summary.user).get()

    context = {
        'summary': summary,
        'profile': profile
    }

    return render(request, 'summaries/summaries_detail.html', {'summary': summary})


@login_required
def summary_add(request):
    if request.method == 'POST':
        summary_form = AddSummaryForm(request.POST)
        summary_form.instance.user = request.user

        if summary_form.is_valid():
            summary_form.save(commit=False)
            #vacancies_form.cleaned_data['user'] = request.user
            summary_form = summary_form.save()
            return redirect('summaries_home')
        else:
            print(summary_form.errors)
    else:
        summary_form = AddSummaryForm
    context = {
        'summary_form': summary_form
    }
    return render(request, 'summaries/summary_add.html', context=context)