from django.shortcuts import render
from .models import Summary


def summaries_home(request):
    summaries = Summary.objects.all()
    return render(request, 'summaries/summaries_home.html', {'summaries': summaries})


def summaries_detail(request):
    id = request.GET.get('id', '')
    try:
        summary = Summary.objects.get(pk=id)
    except Summary.DoesNotExist:
        summary = None

    return render(request, 'summaries/summaries_detail.html', {'summary': summary})