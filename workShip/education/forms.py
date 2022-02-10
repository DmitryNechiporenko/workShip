from django import forms
from .models import *


class StudyResponseForm(forms.ModelForm):
    study = forms.IntegerField(label='Направление', widget=forms.HiddenInput())
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    patronymic = forms.CharField(label='Отчество', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванович'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+70123456789'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))

    class Meta:
        model = StudyResponses
        fields = ('name', 'surname', 'patronymic', 'phone', 'email')
