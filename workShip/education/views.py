from django.shortcuts import render
from .models import Practice

def education_home(request):
    practices = Practice.objects.all()
    return render(request, 'education/education_home.html', {'practices': practices})


def practice_detail(request):
    id = request.GET.get('id', '')
    try:
        practice = Practice.objects.get(pk=id)
    except Practice.DoesNotExist:
        practice = None

    return render(request, 'education/practice_detail.html', {'practice': practice})