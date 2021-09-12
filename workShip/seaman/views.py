from django.shortcuts import render
from .models import SeamanDocument, SeamanBlank


def seaman_home(request):
    documents = SeamanDocument.objects.all()
    blanks = SeamanBlank.objects.all()
    return render(request, 'seaman/seaman_home.html', {'documents': documents, 'blanks': blanks})