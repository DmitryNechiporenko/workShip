from django import forms
from .models import *
from vacancies.models import VacancyResponses

class AddSummaryForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    job = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город'}))
    salary_min = forms.CharField(label='Зарплата от', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Зарплата от'}))
    salary_max = forms.CharField(label='Зарплата до', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Зарплата до'}))
    extra = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 3}))
    image = forms.ImageField(label='Изображение', required=False, widget=forms.FileInput())

    class Meta:
        model = Summary
        fields = ('name', 'job', 'city', 'salary_min', 'salary_max', 'extra', 'image')



class SummaryResponseForm(forms.ModelForm):
    class Meta:
        model = VacancyResponses
        fields = ('vacancy',)