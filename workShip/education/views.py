from django.shortcuts import render, redirect
from .models import Study, Practice
from .forms import *

def education_home(request):
    studies = Study.objects.all()
    return render(request, 'education/education_home.html', {'studies': studies})


def study_detail(request):
    if request.method == 'POST':
        study_form = StudyResponseForm(request.POST)
        study_id = request.POST.get('study_id', 0)
        try:
            study = Study.objects.get(pk=study_id)

        except Study.DoesNotExist:
            study = None

        if study_form.is_valid():
            if study_id:
                study_response = study_form.save(commit=False)
                study_response.study = study
                study_response.save()

                context = {
                    'study': study,
                    'study_form': StudyResponseForm,
                    'success': True
                }
        else:
            context = {
                'study': study,
                'study_form': study_form,
                'success': False
            }
    else:
        id = request.GET.get('id', '')
        try:
            study = Study.objects.get(pk=id)

        except Study.DoesNotExist:
            study = None

        study_form = StudyResponseForm
        context = {
            'study': study,
            'study_form': study_form
        }

    return render(request, 'education/study_detail.html', context=context)


def study_responses_add(request):
    if request.method == 'POST':
        study_form = StudyResponseForm(request.POST)

        if study_form.is_valid():
            study_form.save()
            return redirect('study_detail')
        else:
            print(study_form.errors)
    else:
        study_form = StudyResponseForm
    context = {
        'study_form': study_form
    }
    return redirect('education_home')


def practice_detail(request):
    id = request.GET.get('id', '')
    try:
        practice = Practice.objects.get(pk=id)
    except Practice.DoesNotExist:
        practice = None

    return render(request, 'education/practice_detail.html', {'practice': practice})