from django import forms
from .models import *


class AddVacancyForm(forms.ModelForm):
    title = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'}))
    salary = forms.CharField(label='Зарплата', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Зарплата'}))
    vessel_type = forms.CharField(label='Тип судна', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип судна'}))
    date_start = forms.DateField(label='Дата посадки', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    landing = forms.CharField(label='Место посадки', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Место посадки'}))
    contract_term = forms.CharField(label='Срок контракта', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Срок контракта'}))
    image = forms.ImageField(label='Изображение', required=False, widget=forms.FileInput())
    user = forms.Field(required=False)

    class Meta:
        model = Vacancy
        fields = ('title', 'salary', 'vessel_type', 'date_start', 'landing', 'contract_term', 'image')


